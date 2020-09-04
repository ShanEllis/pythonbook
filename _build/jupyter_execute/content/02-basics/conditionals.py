# Conditionals 

Conditionals are a code structure that help you control whether a certain line of code executes. We'll discuss three ways in which you can control code execution: `if`, `elif` (which stands for 'else if'), and `else`.

##  `if` statements

Conditional statements begin with an `if` statement. They can optionall have `elif` and `else`, which we'll get to in just a second, but they *must* have an `if` statement and that `if` statement must come first. The code within an `if` statement will execute if the condition following `if` evaluates as True.

<div class="alert alert-success">
Conditionals are statements that check for a condition, using the <code>if</code> statement, and then only execute a set of code if the condition evaluates as <code>True</code>.
</div>

The general syntax for a conditional `if` statments requires an `if` followed by a condition and a `:`. Subsequent lines that you want to execute if the condition are true go on indented lines beneath the `if` conditional statement:

```python
if condition:
    # execute this code
```

For example, if we define `condition` to store the boolean `True`, the conditional `if` statement, will then execute the `print()` statement within the condition.

condition = True

if condition:
    print('This code executes if the condition evaluates as True.')

Note that if condition were to store the Boolean `False`, this conditional statement would produce no output, as the conditional `if` statement did *not* evaluate as True. The code within the conditional is _only_ executed if the condition evaluates as `True`.

condition = False

if condition:
    print('This code executes if the condition evaluates as True.')

## `else` statements

After an `if` statement you can add an optional `else` statement. The code within this conditional will execute if the `if` conditional statement did *not* evaluate as `True`.

<div class="alert alert-success">
After an <code>if</code>, you can use an <code>else</code> that will run if the conditional(s) above have not run.
</div>

For example, below we see that condition is defined as `False`. Therefore, the `if` condtional statement evaluates as False. The code within the `if` conditional is ignored, moving onto the `else` statement. The code within that statement is evaluated, printing the code within the `else` statement.

condition = False

if condition:
    print('This code executes if the condition evaluates as True.')
else: 
    print('This code executes if the condition evaluates as False')

Note that the syntax for both the `if` and the `else` statements require a colon at the end of the line and the lines of code within the `if` or `else` statement to be indented. Python requires this because visually makes it clear to readers of your code which lines of code will be executed under which conditions.

Futher, it's important to note that only one condition can be met, so either the code for the `if` statement *or* the code for the `else` statement will execute, but not both.

## `elif` statements

The final type of conditional statement is the `elif` statement. These too are optional, and are read as "else if". After an `if` statment, an `elif` statement can be used to check additional conditions. As with `if` statements, the code within an `elif` statement will only execute if the condition specified evaluates as `True`.

<div class="alert alert-success">
After an <code>if</code> statement, you can have any number of <code>elif</code>`s (meaning 'else if') to check other conditions.
</div>

Here, we have two variables `condition_1` storing `False` and `condition_2` storing `True`. We then see an `if`, `elif` and `else` statement. As before, the code for only one of these conditions will execute. If the `if` condition evaluates as `True`, the code within that statement will execute. Else, if (`elif`) the condition in the `elif` statement evaluates as `True`, the code within the `elif` statement will execute. Finally, if neither the `if` or `elif` evaluate as `True`, the code within the `else` statment will execute.

As before, the syntax requires colons after each `if`, `elif`, and `else` statement and indentation for the lines of code within each statement.

condition_1 = False
condition_2 = True

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')

In the example above, as `condition_1` is `False`, the code beneath the `if` statement does not execute. However, the `elif` condition (`condition_2`) evaluates as `True`, printing the string within the `elif` statement. 

### `elif` without an `else`

An `else` statement is *not* required, but if both the `if` and the `elif` condtions are not met (both evaluate as `False`), then nothing is returned.

For example below both conditions evaluate as `False` and thus the code passes silently, returning nothing.

condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')

### `elif` *after* an `else` does not make sense

Finally, the order will always be `if`-`elif`-`else`...with only the `if` being required. If the `elif` is at the end...it will never be tested, as the `else` will have already returned a value once reached (and thus Python will throw an error).

## THIS CODE WILL PRODUCE AN ERROR
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')

In the example above, there is an `elif` at the end. By definition, there is no way the `elif` will ever be tested. Accordingly, Python indicates that there is a `SyntaxError`.

## Conditionals With Value Comparisons

Beyond providing Booleans directly, conditionals can be used with any expression that evaluates as a Boolean. The operators discussed in an earlier chapter can be used in your conditional statements.

<div class="alert alert-success">
Any expression that can be evaluated as a boolean, such as value comparisons, can be used with conditionals.
</div>

For example, below the condition `language == "Python"` evaluates as `True` because the string "Python" has been declared in the variable `language`. Thus, the code prints "Yay!"

language = "Python"

if language == "Python":
    print("Yay!")
elif language == "English":
    print("Not a programming language.")
else:
    print("Get yourself a programming language!")

Beyond testing for variable equality, mathematical operators can be very helpful when working with condtionals. For example, you can have different code execute depending upon the value stored in a variable.

Here we have an example where `number` stores the integer 4. The conditional tests whether the value stored in `number` is less than 5. As 4 is less than 5, the code within the `if` statement executes, printing 'if statement execution'.

number = 4
 
if number < 5:
    print('if statement execution')
elif number > 5:
    print('elif statement execution')


## Summary

To finish here, we'll summarize a number of the key points in this chapter:

- All conditionals start with an `if`, can have an optional and variable number of `elif`'s and an optional `else` statement
- Conditionals can take any expression that can be evaluated as `True` or `False`. 
- At most one component (`if` / `elif` / `else`) of a conditional will run
- The order of conditional blocks is always `if` then `elif`(s) then `else`
- Code is only ever executed if the condition is met

## Exercises

Q1. **Replace `---` below with something that will print 'True'**

```python
math = ---

if math:
    print('True')
```

Q2. **Replace `---` below with something that will print 'False'.**

```python
my_value = ---

if my_value:
    print('True')
else: 
    print('False')
```

Q3. **What will the following code snippet print out?**

```python
if False:
    print("John")
elif True:
    print("Paul")
elif True:
    print("George")
else:
    print("Ringo")
```

A) John  
B) Paul, George, Ringo  
C) Paul  
D) Paul, George  
E) Ringo 

Q4. **What will the following code snippet print out?**

```python
if 1 + 1 == 2:
    print("I did Math")
elif 1/0:
    print("I broke Math")
else:
    print("I didn't do math")
```

A) I did Math   
B) I broke Math  
C) I didn't do math  
D) This code won't execute. 

Q5. **What will the following code snippet print out?**

```python
conditional = False
python = "great"

if conditional:
    if python == "great":
        print("Yay Python!")
    else:
        print("Oh no.")
else:
    print("I'm here.")
```

A) Yay Python!  
B) Oh no.  
C) I'm here.  
D) This code won't execute.  

Q6. **What would be the output of running the following code?**

```python
condition = 5 < 7

if condition: 
    print('SO GOOD!')
else:
    print('NOT SO GOOD.')
```

A) SO GOOD!  
B) NOT SO GOOD.  
C) True  
D) False  
E) SyntaxError  