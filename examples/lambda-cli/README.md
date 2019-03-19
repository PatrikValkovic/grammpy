# Lambda CLI

This example is application, that can evaluate lambda expressions.
For more about lambda calculus, see [wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus).
The application output each reduction step by step.


## Usage

You need some library installed before running the example.
Type the following command to install them.
```text
pip install -r requirements.txt
```

You can then run the application by executing *run.py* script.

```text
python ./run.py
```

It will show you command line, where you type your lambda expressions to evaluate.

## Example

For example take this lambda expression.

```text
((lambda var y. ((lambda z. ((lambda f. (z f)) z)) var)) 3 7)
```

The program will output following lines.

```text
((lambda var y. ((lambda z. ((lambda f. (z f)) z)) var)) 3 7)
((lambda y. ((lambda z. ((lambda f. (z f)) z)) 3)) 7)
((lambda z. ((lambda f. (z f)) z)) 3)
((lambda f. (3 f)) 3)
(3 3)
```

-----

Author: Patrik Valkovič

Licence: GPLv3
