# Reverse regex generator

This example is application, that generates strings based on the regex.
You type regular expression, and the application generates strings that match that expression.
The application doesn't support standard regular expressions (although it would be easy to extend it),
but just a basic operations.


## Usage

You need grammpy library installed before running the example.
Type one of the following command.
```text
pip install grammpy
# or
pip install -r requirements.txt
```

You can then run the application by executing *run.py* script.

```text
python ./run.py
```

It will show you command line, where you type your regular expressions.

## Operations

The regex supports following operations.
- Concatenation by leaving expressions next to each other. 
For example output of `ab` will be "ab".
- Alternation using `+` operator. 
For example `a+b` will output "a" ad "b".
- Iteration (also called Kleene Star) generates concatenation of repetition.
Note that epsilon (empty value) is situation, where the repetition is made 0 time. 
For example `a*` will output "", "a", "aa", "aaa" and so on.
Because there can be infinity number of repetition, the repetition is controlled by `IterateRule.MAX_ITERATIONS` constant.
By default maximum of 6 iteration is generated.
- Brackets to prioritize the regular expression.
For example `(a+b)(c+d)` will generate "ac", "ad", "bc", "bd".

Please note, that some entries can be in the output multiple time, if there are multiple ways how to construct them.

## More complicated example

Let's look at more complicated example.
For example the regular expression `ab*(def+xy*z)` will have following output
(when number of iterations is set to 4).

```text
adef
axz
axyz
axyyz
axyyyz
axyyyyz
abdef
abxz
abxyz
abxyyz
abxyyyz
abxyyyyz
abbdef
abbxz
abbxyz
abbxyyz
abbxyyyz
abbxyyyyz
abbbdef
abbbxz
abbbxyz
abbbxyyz
abbbxyyyz
abbbxyyyyz
abbbbdef
abbbbxz
abbbbxyz
abbbbxyyz
abbbbxyyyz
abbbbxyyyyz
```

-----

Author: Patrik Valkovič

Licence: MIT
