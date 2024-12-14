# Transformations

Module for transforming grammars.
You can access it using `grammpy.transformations` import.

Currently only small subset of operations exists.
However, all transformation to perform CYK algorithm are already there.

Subset of methods for each type of grammar is stored in separate object.
The inverse operation (if exists) are stored in separate object (still divided by the grammar type)
Right now, following classes exists:
- `ContextFree` - contains methods to transform context free grammars.
- `InverseContextFree` - contains methods to transform the parsed tree.
- `InverseCommon` - contains only method to replaced `SplitRule` instances with their original rule.


For each method modifying the grammar you can decide to modify or copy the grammar. 
Default behaviour is to copy grammar before each modification.
You can disable it for every method by passing `inplace=True` as parameter.


## Context-Free grammars

Contains only methods to transform grammar to Chomsky Normal Form (as this is mandatory for the CYK algorithm).

### Prepare for CYK

The main function in the class is `prepare_for_cyk` method.
This method contains all the necessary calls on the grammar, when you want to use CYK algorithm.
You can skip some steps (if you are sure about the grammar type) using some of the methods below.

```python
from grammpy.transforms import ContextFree
from grammpy.parsers import cyk

new_g = ContextFree.prepare_for_cyk(g)
# now you can use the grammar in the CYK algorithm
root = cyk(new_g, input_data)
```



### Removing of useless symbols

Including removing of unreachable and non-generating symbols.
You can call `remove_useless_symbols` directly
or split it to `remove_unreachable_symbols` and `remove_useless_symbols`.
You can as well check, if the grammar is generating (have at least one output sentence)
using `is_grammar_generating` method.

```python
from grammpy.transforms import ContextFree

new_g = ContextFree.remove_unreachable_symbols(g)
new_g = ContextFree.remove_nongenerating_nonterminals(g)
new_g = ContextFree.remove_useless_symbols(g)
ContextFree.is_grammar_generating(g)
```

### Epsilon rules elimination

Method create new rules that will replace rules with nonterminal rewritable to epsilon.
You can only search for nonterminals, that are rewritable epsilon at some point.

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

Library creating own type of rule, so you can backtrack the changes.
The type is `ContextFree.EpsilonRemovedRule`.

```python
class CreatedRule(Rule):
    rule = ([A], [C])

created = new_g.get_rule(CreatedRule)
assert created.from_rule.rule == ([A], [B, C])
assert created.replace_index == 0
assert issubclass(created, ContextFree.EpsilonRemovedRule)
```

### Removing of unit rules

As with epsilon rules, method for removing unit rules create new rules.
You can then backtrack the changes, however this functionality is already in the `InverseContextFree` class.
You can transform the grammar or just find reachable symbols.

```python
from grammpy import *
from grammpy.transforms import ContextFree

class OldRules(Rule):
    rules = [([A], [B]), ([B], [C]), ([B], [0]), ([C], [1])]

reachable = ContextFree.find_nonterminals_reachable_by_unit_rules(g) # instance of ContextFree.UnitSymbolRechablingResults
assert reachable.reach(A, B) is True
assert reachable.reachables(A) == [B, C]
path = reach.path_rules(B, C) # list of unit rules
assert path[0].rule == ([B], [C])

new_g = ContextFree.remove_unit_rules(g)

class NewRules(Rule):
    rules = [([A], [0]), ([A], [1]), ([B], [0]), ([C], [1])]
    
assert NewRules in new_g.rules
```

### Transformation to Chomsky Normal Form

Method transfer grammar into Chomsky normal form.

These operations create a lot of own types to allow easy backtracking.

Base classes are `ContextFree.ChomskyNonterminal` and `ContextFree.ChomskyRule`, that are base classes for others.

As nonterminals method use `ContextFree.ChomskyTermNonterminal` that represent nonterminal rewritable to terminal (A->a). Nonterminal have property `for_term`, where it stores terminal (as Terminal class).
Second class is `ContextFree.ChomskyGroupNonterminal`, that represent group of symbols (for example in rule A->BCD will this nonterminal represent CD). This nonterminal have property `group`, where it stores list of symbols, that represent.

For rules method create list of classes, where each class have different meaning:
- `ContextFree.ChomskySplitRule`: Represent rule, that was split to contain only two symbols. In property `from_rule` is stored original rule.
- `ContextFree.ChomskyRestRule`: Represent right part after splitting of rule. As previous, in `from_rule` property is stored original rule. 
When splitting, ChomskySplitRule and ChomskyRestRule represent original whole rule: `A->BCDE ==> A->BX and X->CDE`.
- `ContextFree.ChomskyTerminalReplaceRule`: This class is used in situations, where rule contains nonterminal with terminal. Rule is transformed into state, where terminal is replaced with nonterminal rewritable to that terminal.
Class have `from_rule` property that stores original rule and `replace_index` property, that indicate which terminal were replace.
- `ContextFree.ChomskyTermRule`: It is class for rule, that directly rewrite nonterminal to terminal.

You don't need to care about these types, as `InverseContextFree` class implements the backtracking automatically.


## Inverse context free operations

Eliminating of epsilon rules, removing of unit rules and transforming into Chomsky normal form have their inverse operations.
They are implemented on `InverseContextFree` class.

That functions accept root nonterminal of parsed tree as a parameter. 
They then traverse the parse tree and replace rules (or nonterminals) created by transformations by their original equivalent.

### CYK transformations

You can call `reverse_cyk_transforms` method to reverse affect of transformation made by `prepare_for_cyk` method.
Alternatively, you can call methods `transform_from_chomsky_normal_form`, `unit_rules_restore`, `epsilon_rules_restore`
to perform just some of the actions. Note that the methods needs to be call in correct order.

```python
from grammpy.transforms import InverseContextFree

# restore all the rules and nonterminals
root = InverseContextFree.reverse_cyk_transforms(root)
``` 

### Split rules

Because grammar split rule classes, which represents more than one rule,
there is need for algorithm, that replace `SplitRule` class with the original one.
This algorithm is implemented on `InverseCommon` class as `splitted_rules` static method.

This call must be call as the last transformation. 
Also, you don't need to call this, if all of your rule classes have just single rule defined.

Algorithm is for now implemented only for Context-Free grammars.
