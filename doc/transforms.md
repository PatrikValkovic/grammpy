# Transformations

Module for transforming grammars. You can access it using `grammpy.transformations` import.

Currently only small subset of operations exists. However, all transformation to perform CYK and LL parsing are already there.

Subset of methods for each type of grammar is stored in separate object as a static methods. The inverse operation (if exists and make sense) are stored in separate object and again divided by grammar type. Right now, following classes exists:
- `ContextFree` - contains methods to transform context free grammars.
- `InverseContextFree` - contains methods to transform the parsed tree from context-free grammar parser.
- `InverseCommon` - contains methods to replaced any form of AST, currently only containing `SplitRule` backward transformation.

Each method modifying the grammar has option to either to modify or copy the grammar. Default behaviour is to copy grammar before each modification, making the operation
safer but a bit slower. You can modify the existing grammar when you pass `inplace=True` as a parameter.


## Context-Free grammars

Contains methods to transform grammar to Chomsky Normal Form (as this is mandatory for the CYK algorithm).

Contains also methods to prepare FIRST and FOLLOW tables for look-ahead or LL(k) parsers.

### Prepare for CYK

The main function in the class is `prepare_for_cyk` method. This method contains all the necessary calls on the grammar when you want to use CYK algorithm. You can skip some steps (if you are sure about the grammar type) using some of the methods below.

```python
from grammpy.transforms import ContextFree
from grammpy.parsers import cyk

new_g = ContextFree.prepare_for_cyk(g)
# now you can use the grammar in the CYK algorithm
root = cyk(new_g, input_data)
```

### Removing useless symbols

Removes unreachable and non-generating symbols. You can call `remove_useless_symbols` directly or split it to `remove_unreachable_symbols` and `remove_nongenerating_nonterminals`.

You can check if the grammar is generating (have at least one output sequence) using `is_grammar_generating` method. This method may also modify the grammar when `remove=True` as parameter.

```python
from grammpy.transforms import ContextFree

new_g = ContextFree.remove_unreachable_symbols(g)
new_g = ContextFree.remove_nongenerating_nonterminals(g)
new_g = ContextFree.remove_useless_symbols(g)
ContextFree.is_grammar_generating(g)
```

### Epsilon rules elimination

Method creates new rules that will replace the ones generating epsilon.

Note that this operation may cause some nonterminal to be useless, you should call `remove_useless_symbols` after this operation.

```python
from grammpy import *
from grammpy.transforms import ContextFree

class OldRules(Rule):
    rules = [([A], [B, C]), ([B], [EPS])]

ContextFree.find_nonterminals_rewritable_to_epsilon(g) # list of nonterminals
new_g = ContextFree.remove_rules_with_epsilon(g)

class NewRules(Rule):
    rules = [([A], [B, C]), ([A], [C])]
    
assert NewRules in new_g.rules
```

Library creating own type of rule, so you can backtrack the changes. The type is `ContextFree.EpsilonRemovedRule`.

```python
class CreatedRule(Rule):
    rule = ([A], [C])

# define grammar g as in the example above and call
# remove_rules_with_epsilon on it returning new_g 
# as copy of g without epsilon rules
    
created = new_g.get_rule(CreatedRule)
assert issubclass(created, ContextFree.EpsilonRemovedRule)
assert created.from_rule.rule == ([A], [B, C])
assert created.replace_index == 0
```

You don't need to backtrack the changes manually, there is method `epsilon_rules_restore` on `InverseContextFree` class that will do it for you.

### Removing of unit rules

As with epsilon rules, method for removing unit (or chain) rules create new rules. You can then backtrack the changes, however, this functionality is already in the `InverseContextFree` class.

```python
from grammpy import *
from grammpy.transforms import ContextFree

class OldRules(Rule):
    rules = [([A], [B]), ([B], [C]), ([B], [0]), ([C], [1])]

new_g = ContextFree.remove_unit_rules(g)

class NewRules(Rule):
    rules = [([A], [0]), ([A], [1]), ([B], [0]), ([C], [1])]
    
assert NewRules in new_g.rules
```

The parsed result will have, similar to epsilon rules, own type of rule that will rewrite unit rules. The type is `ContextFree.ReducedUnitRule`. You can use `InverseContextFree` method to transform the parsed AST back into the original rules.

```python
parsed = cyk(new_g, input_data)

new_root = unit_rules_restore(parsed)
```

You can want to only find reachable symbols, or find out if some nonterminal is reachable from another one.

```python
class OldRules(Rule):
    rules = [([A], [B]), ([B], [C]), ([B], [0]), ([C], [1])]

# instance of ContextFree.UnitSymbolRechablingResults
reachable = ContextFree.find_nonterminals_reachable_by_unit_rules(g)
assert reachable.reach(A, B) is True
assert reachable.reachables(A) == [B, C]
path = reach.path_rules(B, C) # list of unit rules
assert path[0].rule == ([B], [C])
```

### Transformation to Chomsky Normal Form

The method `transform_to_chomsky_normal_form` can be used to transform grammar (already clean-up by the methods above) into Chomsky normal form.

The resulting grammar can then be passed directly into the `cyk` method.

This operation creates a lot of own types to allow easy backtracking.

Classes `ContextFree.ChomskyNonterminal` and `ContextFree.ChomskyRule` are base classes for rest of the classes bellow.

If nonterminal is rewritable to terminal (A -> a) the `ContextFree.ChomskyTermNonterminal` class is used. It has `for_term` property where it stores terminal.
Second class is `ContextFree.ChomskyGroupNonterminal` that represent group of symbols after the split (for example in rule A->BCD will this nonterminal represent CD). This nonterminal have property `group`, where it stores list of symbols the class represents.

The rules are rewritten into various classes, where each class have different meaning:
- `ContextFree.ChomskySplitRule`: Represent rule that was split to contain only two symbols. In property `from_rule` is stored original rule.
- `ContextFree.ChomskyRestRule`: Represent right part after splitting of rule. Traditionally there is `from_rule` property with the original rule. During splitting the ChomskySplitRule and ChomskyRestRule represent original and whole rule. For example `A->BCDE` splits into`A->BX and X->CDE` where `X` is `ChomskyGroupNonterminal`, `A->BX` is `ChomskySplitRule` and `X->CDE` is `ChomskyRestRule`.
- `ContextFree.ChomskyTerminalReplaceRule`: This class is used in situations where rule contains nonterminal with terminal. Rule is transformed into state, where terminal is replaced with nonterminal rewritable to that terminal.
Class have `from_rule` property that stores original rule and `replace_index` property, that indicate which terminal were replace.
- `ContextFree.ChomskyTermRule`: It is class for rule that directly rewrites nonterminal to terminal.

You don't need to care about these types, as `InverseContextFree` class implements the backtracking for you.

### First and Follow tabl

There are methods to create FIRST and FOLLOW table for arbitrary look-ahead or LL(k) grammars.

As these methods do not directly manipulate the grammar, but rather generate new structures from them, they are described into more detail in [parsers](parsers.md) documentation.


## Inverse context free operations

Eliminating of epsilon rules, removing of unit rules and transforming into Chomsky normal form have their inverse operations transforming the parsed AST into the form reflecting the original definition. They are implemented on `InverseContextFree` class.

That functions accept root nonterminal of parsed tree as a parameter. They then traverse the parse tree and replace rules (or nonterminals) created by transformations by their original equivalent. They return the new root.

> ⚠️ The AST is modified in-place.

### CYK transformations

You can call `reverse_cyk_transforms` method to reverse affect of transformation made by `prepare_for_cyk` method.
Alternatively, you can call methods `transform_from_chomsky_normal_form`, `unit_rules_restore`, `epsilon_rules_restore`
to perform just subset of actions. Note that the methods needs to be call in correct order.

```python
from grammpy import Grammar
from grammpy.transforms import InverseContextFree, ContextFree
from grammpy.parsers import cyk

g = Grammar() # grammar definition

g_modified = ContextFree.prepare_for_cyk(g)

root = cyk(g_modified, [1,2,3])

# restore all the rules and nonterminals
root = InverseContextFree.reverse_cyk_transforms(root)
``` 

### Split rules

Because grammar split rule classes, which represents more than one rule (see [grammar](grammars.md) documentation for more in-depth view), there is need for algorithm that replace `SplitRule` class with the original one. This algorithm is implemented on `InverseCommon` class as `splitted_rules` static method.

This call must be call the last transformation.  Also, you don't need to call this, if all of your rule classes have just single rule defined.

> ⚠️ Algorithm is for now implemented only for Context-Free grammars.
