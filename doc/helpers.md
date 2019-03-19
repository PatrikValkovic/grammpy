## Helpers

Library provide classes, that helps with parsed tree manipulation and traversing.

These classes contains only small subset of methods so far. 
We are expecting to implement other methods soon.
Pull requests are, of course, welcomed.


## Manipulations

Class `Manipulation` can replace specific rule, nonterminal or terminal with different one.
The new element will be added into parsed tree and correctly connected to rest of the elements.

```python
from grammpy.transforms import Manipulations

# define, create and modify the grammar, then parse the input
root = cyk(...)

# replace specific node or rule
Manipulation.replaceNode(root, MyNewNonterminal())
Manipulation.replaceRule(root.to_rule, MyNewRule())

# you can use automatic deduction
# replace nonterminal
Manipulation.replace(parsed, MyNewNonterminal())
# replace rule
Manipulation.replace(parsed.to_rule, MyNewRule())
```


## Traversing

Second class is `Traversing`. 
It contains static methods for traverse the parsed tree.
The following traverse methods are implemented:
- `pre_order` - traverse the tree in pre-order and DFS fashion.
- `post_order` - traverse the tree in post-order and DFS fashion.
- `print` - returns the parsed tree as a string. This method is usable for debugging.

Methods traverse through nonterminals, terminals, and the rules. 
If you want to traverse just nonterminals, use the `filter` builtin function.

```python
from grammpy.transforms import Traversing

# post order all nodes
for n in Traversing.post_order(root):
    print(n.__class__)
    
# pre order only rules
for r in filter(lambda x: isinstance(x, Rule), Traversing.pre_order(root)):
    print(r.__class__)
```

You can create your own traversing path by calling `traverse` static method.
Method accept root of the parsed tree and function that will be called for every node.
The function itself accepts node to process and callback.
If the function invoke callback on other node, it will be called again in a recursion.
The function needs to yield the value (and possibly the invocation of the callback).

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

Alternatively, you can use `traverse_separated` static method.
This method works same as `traverse` one, expect it uses different parameters to handle nonterminals, terminals and rules.

```python
def traverseRule(item, callback):
    for symb in item.to_symbols:
        yield callback(symb)
    yield item
    
def traverseNonterm(item, callback):
    yield callback(item.to_rule)
    yield item
    
def traverseTerm(item, callback):
    yield item
    
Traversing.traverse_separated(root, 
                             traverseRule, 
                             traverseNonterm, 
                             traverseTerm)
```

Moreover, both `traverse` and `traverse_separated` accepts additional parameters.
These parameters are then passed to the callback itself.
You can pass these parameters as well during the recursion using same approach.

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


Class `Traverse` also provides `print` static method, that returns string representing the structure of the AST.
The `print` method is mainly for debugging purpose.
You can see example output below.

```text
(R)ChomskySplitTempRule81
|--(N)NoBracketExpression
|  `--(R)ChomskySplitRule20
|     |--(T)<class 'lambda_cli.terminals.LeftBracket'>
|     `--(N)ChomskyGroupNonterminal20
|        `--(R)ChomskySplitTempRule20
|           |--(N)NoBracketExpression
|           |  `--(R)ReducedSplitRules6
|           |     |--(T)<lambda_cli.terminals.Variable object at 0x060818D0>
|           |     `--(N)ExpressionBody
|           |        `--(R)SplitRules7
|           |           `--(T)<lambda_cli.terminals.Variable object at 0x060817D0>
|           `--(T)<class 'lambda_cli.terminals.RightBracket'>
`--(T)<class 'lambda_cli.terminals.RightBracket'>
```
