---
redirect_from:
  - "/04-functions/debugging-errors"
interact_link: content/04-functions/debugging_errors.ipynb
kernel_name: python3
title: 'Debugging & Errors'
prev_page:
  url: /04-functions/functions
  title: 'Functions'
next_page:
  url: /04-functions/nampespaces_scope
  title: 'Namespaces & Scope'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Debugging and  Errors

While you've likely gotten an error or two in your programming journey thus far (we all have!), as you start writing functions, having strong debugging skills and understanding the error messages you receive while debugging will be critical.

In this chapter, we'll discuss the various types of errors you'll encounter in Python, introduce the idea of `try` and `except` while debugging and work through an example of the thought process behind debugging upon ecountering an error.

<div class="alert alert-success">
<b>Debugging</b> is the process of finding and fixing errors in a computer program.
</div>

## Motivating Example #1

To start thinking about debugging, let's consider an example. Here we have a function. The pieces of this function should all look familiar at this point. There's variable assignment, a for loop, some use of the addition operator (`+`), indexing, and a `return` statement. Take a look at this code and ask yourself: Will I be able to define and execute this function? 

In other words, is this a valid function in Python?



{:.input_area}
```python
def example_function(input_list):
    
    running_sum = 0
    for item in input_list:
        running_sum = running_sum + item
    
    special_value = input_list[3]
    
    return running_sum + special_value
```


Well, to answer this question you could consider the following call of the function:



{:.input_area}
```python
example_function([1, 2, 3, 4])
```





{:.output .output_data_text}
```
14
```



The above example of the function executes and returns the value 14, the sum of all the values in the input list plus the value stored in the fourth position of the input list. 

But, what about the following function call:



{:.input_area}
```python
example_function([1, 2, 3])
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-3-b2899b84d137> in <module>()
    ----> 1 example_function([1, 2, 3])
    

    <ipython-input-2-a4fb5262d9d1> in example_function(input_list)
          5         running_sum = running_sum + item
          6 
    ----> 7     special_value = input_list[3]
          8 
          9     return running_sum + special_value


    IndexError: list index out of range


```

Here, we get an `IndexError`, as there is no fourth index of the input list. Python runs into an error when trying to execute the following line of the function:  `special_value = input_list[3]`

So, the successful execute of the function is dependent upon the input provided. 

Let's look at one more example:



{:.input_area}
```python
example_function(['s', 'h', 'a', 'n'])
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-6a097b693a7c> in <module>()
    ----> 1 example_function(['s', 'h', 'a', 'n'])
    

    <ipython-input-1-a4fb5262d9d1> in example_function(input_list)
          3     running_sum = 0
          4     for item in input_list:
    ----> 5         running_sum = running_sum + item
          6 
          7     special_value = input_list[3]


    TypeError: unsupported operand type(s) for +: 'int' and 'str'


```

The following example will also error; however, this time it's a `TypeError` rather than an `IndexError`. This occurs when Python tries to execute the `running_sum = running_sum + item` line of the function. In this case, a string is attempted to be added to an integer, which is not something Python can do. 

Thus, another error.

Being able to adapt your code so that it does what you want it to do requires that you both understand these errors *and* know how to fix it. So, let's get started understanding what each of these errors means.

## Errors

Errors are enountered when the code you've tried to execute is unable to run. These interruptions can occur for a number of different reasons. We'll explore each of these now.

<div class="alert alert-success">
<b>Errors</b> are problems with code definition or execution that interrupt running Python code.
</div>

### Syntax Errors

Syntax errors occur when the code you've written fails to follow the rules of Python. It will fail under any and all circumstances. These include `SyntaxErrors` and `IndentationErrors`.

<div class="alert alert-success">
Syntax & Indentation Errors reflect code that doesn't follow Python structure, and will necessarily fail. 
</div>

### Syntax Errors

For example, if you try to execute the following conditional statement, it will fail. This will happen regardless of the code you include within your conditional or what conditional you specify becuase a colon is missing after your `if` statement. 

Notice in the output that Python does it's best to point you in the right direction using a `^` to highlight where in your code Python encoungered an error. And, Python lets you know this is a `SyntaxError`, so you're clued into the fact that there's something wrong with your code's structure.



{:.input_area}
```python
# will produce a syntax error
if True 
    print('Yep.')
```


{:.output .output_traceback_line}
```

      File "<ipython-input-5-a91490a26c37>", line 2
        if True
                ^
    SyntaxError: invalid syntax



```

### Indentation Errors

Indentation errors occur when Python was expecting something to be have a certain indentation level but instead encountered something different. Remember, Python cares about whitespace, so if you fail to adhere to what Python is expecting, you will get an `IndentationError`.



{:.input_area}
```python
# will produce a syntax error
# and specifically an indentation error
my_list = [1, 2]
for value in my_list:
print(value)
```


{:.output .output_traceback_line}
```

      File "<ipython-input-6-45596487aa45>", line 5
        print(value)
            ^
    IndentationError: expected an indented block



```

In the above example, Python again gives you a readout about what it was expecting and where you appear to have gone wrong, letting you know that it encountered an `IndentationError` as it expected `print(value)` to be indented within your `for` loop.

For `SyntaxError`s and `IndentationError`s, the rest of your code may very well be fine. Once you fix the structure or syntax of your code, the error will likely be resolved.

## Exceptions

Unlike syntax errors, exceptions are errors that occur due to the specific code you tried to execute. In these cases, the syntax or structure of your code looks fine, but an error occurred when Python tried to execute your code, resulting in an error.

<div class="alert alert-success">
Exceptions are errors that occur when a code is executed.
</div>

### ZeroDivisionError

A `ZeroDivisionError` occurs when you try to divide by zero. 

Sometimes this will be very obvious, such as if you directly try to divide by zero, as Python does not know how to divide by zero.



{:.input_area}
```python
# produces ZeroDivisionError
1 / 0
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-7-79e900a17bd3> in <module>()
          1 # produces ZeroDivisionError
    ----> 2 1 / 0
    

    ZeroDivisionError: division by zero


```

However, more likely you'll encounter a `ZeroDivisionError` when looping through a list or using a conditional. In these cases, you'll have to dig through your code and how you tried to execute that code to determine where your code tried to divide by zero.

For example, in the following cell, you see code that is syntactically fine. However, when the loop gets to the third index in my_list, the `temp = val / (val - 4)` attempts to divide by zero, leading Python to return a `ZeroDivisionError`



{:.input_area}
```python
# produces a ZeroDivisionError
running_sum = 0
my_list = [1, 2, 3, 4, 5]

for val in my_list:
    
    if val % 2 == 0:
        temp = val / (val - 4)
        running_sum += temp 
        
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-5-67ebb73a2ad8> in <module>()
          6 
          7     if val % 2 == 0:
    ----> 8         temp = val / (val - 4)
          9         running_sum += temp
         10 


    ZeroDivisionError: division by zero


```

### NameError

A `NameError` occurs when you try to access a name that Python does not know.

For example, if you define a variable with the name `variable` and then try to access `varaible` (`variable` with a typo), you will receive a `NameError`. 



{:.input_area}
```python
# Define a variable
variable = 12
```




{:.input_area}
```python
# If you typo a name, you will get a NameError
varaible
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-4acade15292f> in <module>()
          1 # If you typo a name, you will get a NameError
    ----> 2 varaible
    

    NameError: name 'varaible' is not defined


```

Whenever you see a `NameError`, consider whether you've misspelled or mistyped something. Look through your code carefully as they can somteimes be hard to spot visually. 

And, while it's annoying, it's helpful that Python doesn't just _guess_ that you _meant_ 'variable'....because sometimes Python would guess wrong. It's better for Python to just give us the error.

Finally, you'll also get a `NamerError` if you try to use the equality operator (`==`) when you meant to use the assignment operator (`=`). Here, since `new_variable` hasn't yet been defined, when Python tries to determine if it is equl to `1`, a `NameError` is returned, as `new_variable` does not exist.



{:.input_area}
```python
# You also get a name error if you try to use the wrong operator for assignment
new_variable == 1
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-4f05423dede6> in <module>()
          1 # You also get a name error if you try to use the wrong operator for assignment
    ----> 2 new_variable == 1
    

    NameError: name 'new_variable' is not defined


```

### IndexError

Similarly, an `IndexError` occurs when you try to access an index that doesn't exist.

For example, the following list has three elements, if you try to access the fourth element (index position 5), you'll recieve an `IndexError` with a note that the index is out of range:



{:.input_area}
```python
my_list = [1, 2, 3]
my_list[5]
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-11-2c2a83518cf2> in <module>()
          1 my_list = [1, 2, 3]
    ----> 2 my_list[5]
    

    IndexError: list index out of range


```

Note that this applies to any collection where indexing applies, such as tuples, dictionaries, or strings.

If you try to access the value for a key that does not exist in a dictionary, for example, you will again receive an Error. Here, it is specifically a `KeyError`.



{:.input_area}
```python
# Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
my_dictionary = {'name1' : 1, 'name2' : 2}
my_dictionary['name3']
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-12-84a1c00e4833> in <module>()
          1 # Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
          2 my_dictionary = {'name1' : 1, 'name2' : 2}
    ----> 3 my_dictionary['name3']
    

    KeyError: 'name3'


```

### ValueError

A `ValueError` occurs when you try to use an illegal value for something.

For example, if you try to make an integer out of a string, you'll receive a `ValueError`:



{:.input_area}
```python
int('cat')
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-13-1c6b28888bbe> in <module>()
    ----> 1 int('cat')
    

    ValueError: invalid literal for int() with base 10: 'cat'


```

### TypeError

Finally, a `TypeError` occurs when you try to operate on a variable in a way that Python is unabe to interpret given its type.

For example, `+` concatenates strings and adds integers. When you try to combine those two types of variables, Python is unable to determine whether it shoudl concatenate or add. As such, a `TypeError` is returned.



{:.input_area}
```python
'a_string' + 12
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-15-57c293ee5895> in <module>()
    ----> 1 'a_string' + 12
    

    TypeError: must be str, not int


```

## Stack Trace

The **stack trace** is a log of what Python did as it went through your code. This ets printed out if Python runs into an error.



{:.input_area}
```python
running_sum = 0
my_list = [1, 2, 3, 4, 5]

for val in my_list:
    
    if val % 2 == 0:
        temp = val / (val - 4)
        #+= allows you to add the value on the right to the variable on the left 
        # and assign it to the variable on the left
        running_sum += temp 
        # equivalent to:
        # running_sum = running_sum + temp
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-21-5d11a706076f> in <module>()
          5 
          6     if val % 2 == 0:
    ----> 7         temp = val / (val - 4)
          8         #+= allows you to add the value on the right to the variable on the left
          9         # and assign it to the variable on the left


    ZeroDivisionError: division by zero


```

Sometimes these get really complex. We're here to get better at interpreting these traces.

Note that if external functions are being used, these will get longer.

## Try / Except

<div class="alert alert-success">
Exceptions do not necessarily have to lead to breaking the program - they can be programmatically dealt with, using 'try' and 'except'. 
</div>

### Try / Except Block



{:.input_area}
```python
# Try / Except Block
try:
    # Tries to do this code
    pass # pass just says is not an operation; carry on
except:
    # If there is an error (an exception), keep going and do this instead
    pass
```


### Try / Except Example



{:.input_area}
```python
# Example: we want to get an input number from the user

my_num = input("Please type a number: ")

print('\nmy_num is: ', my_num)
```


{:.output .output_stream}
```
Please type a number: shannon

my_num is:  shannon

```

### Example with Try / Except



{:.input_area}
```python
try:
    int(input('Number'))
except:
    print("nahhh")
```


{:.output .output_stream}
```
Numbershannon
nahhh

```

#### Try / Except within a While Loop



{:.input_area}
```python
ask_for_num = True

while ask_for_num:
    try:
        my_num = int(input("Please enter a number: "))
        ask_for_num = False
    except ValueError:
        print("Oops!  That was no valid number. Try again!")
        
print('\nmy_num is: ', my_num)
```


{:.output .output_stream}
```
Please enter a number: shannon
Oops!  That was no valid number. Try again!
Please enter a number: 29

my_num is:  29

```

### More Try / Except



{:.input_area}
```python
# define a function divide
def divide(num1, num2):
    return num1 / num2
```




{:.input_area}
```python
print(divide(2, 0))
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-29-0cdf54a076ec> in <module>()
    ----> 1 print(divide(2, 0))
    

    <ipython-input-28-62d4f4a69b89> in divide(num1, num2)
          1 # define a function divide
          2 def divide(num1, num2):
    ----> 3     return num1 / num2
    

    ZeroDivisionError: division by zero


```



{:.input_area}
```python
# define a function safe_divide
def safe_divide(num1, num2):
    
    try:
        output = num1 / num2
    except ZeroDivisionError:
        output = None
    
    return output
```




{:.input_area}
```python
print(safe_divide(2, 0))
```


{:.output .output_stream}
```
None

```

## Raising Errors

<div class="alert alert-success">
You can also write code to raise an Exception if something unexpected happens.
</div>

### Raise Exception Examples

`raise` is a keyword that tells Python you want to create your own error.



{:.input_area}
```python
my_int = input('An integer please: ')
if not my_int.isnumeric():
    raise ValueError('I wanted a number! :(')
    
print('My integer is: ', my_int) 
```


{:.output .output_stream}
```
An integer please: shannon

```

{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-33-bc64f24647db> in <module>()
          1 my_int = input('An integer please: ')
          2 if not my_int.isnumeric():
    ----> 3     raise ValueError('I wanted a number! :(')
          4 
          5 print('My integer is: ', my_int)


    ValueError: I wanted a number! :(


```

### Clicker Question #5

Edit the code below (replacing `---` with either values or variable names) so that when executed, this cell returns `None`.



{:.input_area}
```python
num1  = 1
num2 = 0

try:
    output = num1 / num2
except ZeroDivisionError:
    output = None
    
print(output)
```


{:.output .output_stream}
```
None

```

- A) I did it!
- B) I _think_ I did it...
- C) I'm totally lost.



{:.input_area}
```python
m
```


## Debugging Process

## Exercises

1. **What type of error would each of the following return?**

```python
int('six')

if num > 0
    print("Greater than 0")
    
if num > 0:
    print("Greater than 0")
```

2. ****
