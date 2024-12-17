## Helpers

Library provide classes and methods that helps with parsed tree manipulation and traversing.

These classes contain only fundamentals methods so far, but you can build your own on top of it. Pull requests are, of course, welcomed.

Helper functions are implemented as static methods on following classes.


## Manipulations

Class `Manipulation` can replace specific rule, nonterminal or terminal with your specified one. The new element will be added into parsed tree and correctly connected to rest of the elements.

```python
from grammpy.transforms import Manipulations

# define, create and modify the grammar, then parse the input
root = cyk(...)

# replace specific node or rule
new_root = Manipulation.replaceNode(root, MyNewNonterminal())
Manipulation.replaceRule(new_root.to_rule, MyNewRule())

# you can use automatic deduction
# replace nonterminal
new_root = Manipulation.replace(parsed, MyNewNonterminal())
# replace rule
Manipulation.replace(new_root.to_rule, MyNewRule())
```


## Traversing

Second class is `Traversing`. It contains static methods for traverse the parsed tree.
The following traverse methods are implemented:
- `pre_order` - traverse the tree in pre-order and DFS fashion.
- `post_order` - traverse the tree in post-order and DFS fashion.
- `print` - returns the parsed tree as a string. This method is usable for debugging.
- `traverse` - allows you to call callback on every node in the AST. Described into more depth bellow.
- `traverse_separated` - has same functionality as `traverse`, but allows you to specify different callbacks for nonterminals, terminals, and rules.

Methods traverse through nonterminals, terminals, and the rules. If you want to traverse just e.g. nonterminals, use the `filter` builtin function.

```python
from grammpy.transforms import Traversing

# post order all nodes including nonterminals
for n in Traversing.post_order(root):
    print(n.__class__)
    
# pre order iteration going through rules only
for r in filter(lambda x: isinstance(x, Rule), Traversing.pre_order(root)):
    print(r.__class__)
```

You can create your own traversing path by calling `traverse` static method. Method accept root of the parsed tree and function that will be called for every iterated node. The callback itself accepts node to process and callback to "expand" the iteration. If the function invoke callback on other node, it will be called again in a recursive fashion.

The function needs to yield the value (and possibly the return value of callback invocation).

> There is no direct recursion involved, so you don't need to be afraid of stack overflow for even very deep trees. The actual implementation is hidden within the library behind the callback function, so you don't need to worry about it.

You can see example bellow.

```python
from grammpy.transforms import Traversing

# traverse all nonterminals in post order
def post_order_traversing(item, callback):
    if isinstance(item, Nonterminal):
        for child in item.to_rule.to_symbols:
            yield callback(child)
        yield item

Traversing.traverse(root, post_order_traversing)
```

Alternatively, you can use `traverse_separated` static method. This method works same as `traverse`, except it uses different parameters to handle nonterminals, terminals and rules.

```python
def traverse_rule(item, callback):
    for symb in item.to_symbols:
        yield callback(symb)
    yield item
    
def traverse_nonterm(item, callback):
    yield callback(item.to_rule)
    yield item
    
def traverse_term(item, callback):
    yield item
    
Traversing.traverse_separated(
    root, 
    traverse_rule, 
    traverse_nonterm, 
    traverse_term,
)
```

Any additional parameters passed down `traverse` or `traverse_separated` are send down into the callback itself. You need pass these parameters down during the recursion.

```python
from grammpy.transforms import Traversing

# traverse all nonterminals in post order
def post_order_traversing(item, callback, parameter1, parameter2):
    # ...
    # pass parameters to the recursion
    yield callback(item, parameter1 + 1, parameter2 - 1)

# pass parameters
Traversing.traverse(root, post_order_traversing, 2, 4)

```


Class `Traverse` also provides `print` static method, that returns string representing the structure of the AST. The `print` method is mainly for debugging purpose. You can see example output below.

```text
(N)E
`--(R)RuleE
   |--(N)T
   |  `--(R)RuleT
   |     |--(N)F
   |     |  `--(R)RuleNum
   |     |     `--(T)id
   |     `--(N)Tcap
   |        `--(R)RuleTcapEps
   |           `--(T)EPSILON
   `--(N)Ecap
      `--(R)RuleEcap
         |--(T)+
         |--(N)T
         |  `--(R)RuleT
         |     |--(N)F
         |     |  `--(R)RuleNum
         |     |     `--(T)id
         |     `--(N)Tcap
         |        `--(R)RuleTcap
         |           |--(T)*
         |           |--(N)F
         |           |  `--(R)RuleNum
         |           |     `--(T)id
         |           `--(N)Tcap
         |              `--(R)RuleTcapEps
         |                 `--(T)EPSILON
         `--(N)Ecap
            `--(R)RuleEcapEps
               `--(T)EPSILON
```
