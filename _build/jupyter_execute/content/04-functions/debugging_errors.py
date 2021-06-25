# Debugging & Errors

While you've likely gotten an error or two in your programming journey thus far (we all have!), as you start writing functions, having strong debugging skills and understanding the error messages you receive while debugging will be critical.

In this chapter, we'll discuss the various types of errors you'll encounter in Python, introduce the idea of `try` and `except` while debugging and work through an example of the thought process behind debugging upon ecountering an error.

<div class="alert alert-success">
<b>Debugging</b> is the process of finding and fixing errors in a computer program.
</div>

## Motivating Example #1

To start thinking about debugging, let's consider an example. Here we have a function. The pieces of this function should all look familiar at this point. There's variable assignment, a for loop, some use of the addition operator (`+`), indexing, and a `return` statement. Take a look at this code and ask yourself: Will I be able to define and execute this function? 

In other words, is this a valid function in Python?

def example_function(input_list):
    
    running_sum = 0
    for item in input_list:
        running_sum = running_sum + item
    
    special_value = input_list[3]
    
    return running_sum + special_value

Well, to answer this question you could consider the following call of the function:

example_function([1, 2, 3, 4])

The above example of the function executes and returns the value 14, the sum of all the values in the input list plus the value stored in the fourth position of the input list. 

But, what about the following function call:

example_function([1, 2, 3])

Here, we get an `IndexError`, as there is no fourth index of the input list. Python runs into an error when trying to execute the following line of the function:  `special_value = input_list[3]`

So, the successful execute of the function is dependent upon the input provided. 

Let's look at one more example:

example_function(['s', 'h', 'a', 'n'])

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

# will produce a syntax error
if True 
    print('Yep.')

### Indentation Errors

Indentation errors occur when Python was expecting something to be have a certain indentation level but instead encountered something different. Remember, Python cares about whitespace, so if you fail to adhere to what Python is expecting, you will get an `IndentationError`.

# will produce a syntax error
# and specifically an indentation error
my_list = [1, 2]
for value in my_list:
print(value)

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

# produces ZeroDivisionError
1 / 0

However, more likely you'll encounter a `ZeroDivisionError` when looping through a list or using a conditional. In these cases, you'll have to dig through your code and how you tried to execute that code to determine where your code tried to divide by zero.

For example, in the following cell, you see code that is syntactically fine. However, when the loop gets to the third index in my_list, the `temp = val / (val - 4)` attempts to divide by zero, leading Python to return a `ZeroDivisionError`

# produces a ZeroDivisionError
running_sum = 0
my_list = [1, 2, 3, 4, 5]

for val in my_list:
    
    if val % 2 == 0:
        temp = val / (val - 4)
        running_sum += temp 
        

### NameError

A `NameError` occurs when you try to access a name that Python does not know.

For example, if you define a variable with the name `variable` and then try to access `varaible` (`variable` with a typo), you will receive a `NameError`. 

# Define a variable
variable = 12

# If you typo a name, you will get a NameError
varaible

Whenever you see a `NameError`, consider whether you've misspelled or mistyped something. Look through your code carefully as they can somteimes be hard to spot visually. 

And, while it's annoying, it's helpful that Python doesn't just _guess_ that you _meant_ 'variable'....because sometimes Python would guess wrong. It's better for Python to just give us the error.

Finally, you'll also get a `NamerError` if you try to use the equality operator (`==`) when you meant to use the assignment operator (`=`). Here, since `new_variable` hasn't yet been defined, when Python tries to determine if it is equl to `1`, a `NameError` is returned, as `new_variable` does not exist.

# You also get a name error if you try to use the wrong operator for assignment
new_variable == 1

### IndexError

Similarly, an `IndexError` occurs when you try to access an index that doesn't exist.

For example, the following list has three elements, if you try to access the fourth element (index position 5), you'll recieve an `IndexError` with a note that the index is out of range:

my_list = [1, 2, 3]
my_list[5]

Note that this applies to any collection where indexing applies, such as tuples, dictionaries, or strings.

If you try to access the value for a key that does not exist in a dictionary, for example, you will again receive an Error. Here, it is specifically a `KeyError`.

# Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
my_dictionary = {'name1' : 1, 'name2' : 2}
my_dictionary['name3']

### ValueError

A `ValueError` occurs when you try to use an illegal value for something.

For example, if you try to make an integer out of a string, you'll receive a `ValueError`:

int('cat')

### TypeError

Finally, a `TypeError` occurs when you try to operate on a variable in a way that Python is unabe to interpret given its type.

For example, `+` concatenates strings and adds integers. When you try to combine those two types of variables, Python is unable to determine whether it shoudl concatenate or add. As such, a `TypeError` is returned.

'a_string' + 12

## Stack Trace

The **stack trace** is a log of what Python did as it went through your code. This ets printed out if Python runs into an error.

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

Sometimes these get really complex. With practice, you'll get better at interpreting these traces, but for now notice that there is often either an arrow (`---->`) or a caret (`^`) indicating at which line or at which point in your code Python encountered the error. Focusing at these points in the error message and reading the error message at the end (i.e. `ZeroDivisionError: division by zero` in the example above) is a good place to start when trying to decipher what the error means.

As you're learning, do your very best to read the message and try to understand it. It can be tempting to be overwhelmed and ignore these if you don't understand the error at first glance. Spending a few seconds longer to understand it can save you a lot of time in the long run.

## Try / Except

While *syntax errors* will necessarily fail, *exceptions* do not necessarily have to lead to breaking the program - they can be programmatically dealt with, using `try` and `except`. A `try`/`except` block allows you to try some code. If, in attempting to execute that code, an exeption is encountered, Python will instead execute the code in the `except` code block.

### `try`/`except` Block

The general structure of a `try`/`except` blog is as follows:

```python
try:
    # Tries to do this code
    pass # pass just says is not an operation; carry on
except:
    # If there is an error (an exception), keep going and do this instead
    pass
```

For example, if, we wanted to ask the user to input a number, we could do so using `input()`. The string inside the `input` function ('Please type a number: ') is what is displayed to the left of the box where the user enters their input. Whatever the user types will, in the code example below, be stored in the variable `my_num`. In the example below, if the user were to type 'shannon', the code would print `my_num is: shannon`. And, that doesn't make a ton of sense...since 'shannon' is not a number. Fortunately, we can use a `try`/`except` block to handle this and only accept the input from the user once it is, in fact, a number.

# Example: we want to get an input number from the user
my_num = input('Please type a number: ')
print('\nmy_num is: ', my_num)

To build up to this, we first need to think about the logic. We want to *first* `try` to get the `input` from the user. And, we want to typecast (meaning specify the type that input should be) that input into an integer using `int()`. However, what if we input the string 'shannon' again? As we saw above `int('shannon')` would raise an exception. 

# this raises an error
int('shannon')

This is where `try`/`except` comes in handy! We can first `try` to run the code in the `try` code block; however, *if an exception is raised* (which will happen if we type 'shannon' as input), the code in the `except` block will execute instead.

# with a string as input
try:
    int(input('Please type an integer: '))
except:
    print('nahhh')

In the above example, we see that rather than raising a `ValueError`, instead, the code in the `except` block has executed instead, printing 'nahhh'.

Note that if the user input a number, like 29, for example, the `except` block would never execute, since the `try` block would not have raised an exception, as we see here, where 'nahhh' is not printed:

# with a number as input
try:
    int(input('Please type an integer: '))
except:
    print('nahhh')

In the above example, the code terminates even when the user has not followed instructions. What if we wanted to keep asking the user until they get it right? This sounds like the time for a `while` loop, where we'll loop until the user input is valid!

In the example here we see that `as_for_num` is `True` to start, so our `while` loop will continue to loop until `as_for_num` becomes `False`. We see that happens inside the `try` block, but only after `my_num` stores an integer. If, in trying to get an input from the user, the code raises an exception `'Oops!  That was no valid number. Try again'` will instead be printed, and the loop will execute again asking for the user's input once more. The `print()` statement at the end of this code cell will only execute once the `while` loop has terminated.

ask_for_num = True

while ask_for_num:
    try:
        my_num = int(input('Please enter a number: '))
        ask_for_num = False
    except ValueError:
        print('Oops!  That was no valid number. Try again!')
        
print('\nmy_num is: ', my_num)

### Example: `try`/`except` 

In the above worked example, we saw how a `try`/`except` works, specifically seeing its functionality within a `while` loop. However, this code construct can be used in combination with various code constructs we've discussed thus far, including within functions. 

For example, if you were to define the function `divide()` as you see here...

def divide(num1, num2):
    return num1 / num2

...you would likely quickly intuit that this function would execute without issue for some input values, but raise a `ZeroDivisionError` whenever `num2` was zero. 

# executes without issue
divide(2, 2)

# raises an error
divide(2, 0)

What if we want our function to execute, even if `num2` is zero? In this case, we could include a `try`/`except` within our function. Here, we'll call our function `safe_divide`. Note that it still takes in two parameters (`num1`, `num2`); however, if `output = num1 / num2` raises an exception, `output` will store `None`. Whatever is stored in `output` after the `try`/`except` block will be returned from the function.

# define a function safe_divide
def safe_divide(num1, num2):
    
    try:
        output = num1 / num2
    except ZeroDivisionError:
        output = None
    
    return output

# same output as above
safe_divide(2, 2)

# no longer raises an error
safe_divide(2, 0)

## Debugging Strategies

When you've encountered an error of some sort in your code and you aren't sure where to go next to fix your code, the following strategies/approach could help.


For example, what if you've been asked to "write code that will check whether the value stored in `my_val` is both positive and even. If it is, store the integer `1` in the variable `output`"

And, you think to yourself: *How do I check whether a variable stores an even value?*

You've got *some idea* of how to approach this, but you aren't quite ready to write actual python code with correct syntax. Instead you attempt **strategy #1: write some pseudocode**. Pseudocode helps structure your thinking and gets your ideas written down, but doesn't have to have correct syntax. The psedocode (here just a bunch of comments) you start with is below:

# variable my_val

# if my_val is positive (> 0) and even:
    # output stores 1

With the pseudocode above you've got something that looks a little like python, but wouldn't execute. However, the ideas are there. We can see that `if` whatever is stored in `my_val` is positive and even, `output` will store the value 1. Okay, that's a start.

And, while you know how to determine if a variable is positive (defined as greater than zero), you aren't totally sure how to determien if a variable stores an even value. So, you turn to **strategy #2**: **add "in python" to your search on the Internet**

Your search term: "How to check whether a variable stores an even value _in python_."

The Internet comes through for you explaining that if you check if the remainder after dividing a number by 2 is equal to zero, that number is even...and likely even gives you some python code in the example (`val % 2 == 0`). With this, you try to incorporate it into what you've already started.

# this code errors
my_val = 6

if my_val > 0 and my_val % 2 = 0:
    output == 1

So, you've now got some code written, and you really thought it was going to be correct, but you've now got an error. So, you read the SyntaxError and you're not really sure what the issue is. So, you consider **strategy #3: adding `print()` statements**. You think through the logic of your code and you say to yourself "OK, if `my_val` is 6, then the condition `my_val > 0` should be true, because `my_val` is greater than zero and `my_val % 2 = 0` should be true, since 6 is even. If those are both true, the code within the conditional code block should execute. If that happens, we could add a `print()` statement within the conditional, knowing that it would only print() something if my logic were true!" With that thought, you add a `print()` statement and re-execute your code: 

# this code errors
my_val = 6

if my_val > 0 and my_val % 2 = 0:
    print('this should print!')
    output == 1

You see that you still get the `SyntaxError`, which makes sense, since we didn't actually change the code yet, but you *also* notice that the `print()` statement was never executed. At this point you know the error in your code happens *before* that `print()` statement...since nothing `print`ed. So, you revisit your conditional and the error message, and at this point you realize that the caret (`^`) is indicating there's some issue with the statement `my_val % 2 = 0`. Suddenly it finally hits you! You wanted to check for equality (`==`), not assign (`=`). You fix your code changing the assignment operator to an equality operator.

# this code errors
my_val = 6

if my_val > 0 and my_val % 2 == 0:
    print('this should print!')
    output == 1

At this point, we *still* get an error *but*, you'll notice 1) it's a *different* error and 2) our `print()` statement is now encountered. We know here that the conditional is now correct! So, we read our error message and see it says "'output' is not defined." And, you look at your code and realize, ah - the same mistake in reverse. The final statement `output == 1` is a statement of assignment, storing `1` in `output`. You fix your code and re-execute:

my_val = 6

if my_val > 0 and my_val % 2 == 0:
    print('this should print!')
    output = 1

Note that your `print()` statement will `print()` unless it's removed, so your last step to clean up your code now that you're done with debugging is to remove it. With that, you've accomplished your task!

my_val = 6

if my_val > 0 and my_val % 2 == 0:
    output = 1

output

## Exercises

Q1. **What type of error would each of the following return?**

```python
int('six')

if num > 0
    print("Greater than 0")
    
if num > 0:
    print("Greater than 0")
```

Q2. **Given the function `my_function` provided, understand the function and then debug the function so that each of the following test cases pass without producing an error**:

```python
def my_function(input_1, input_2):
    """A long function that might error."""
    
    if len(input_1) > 1
        if input_1[0] = 0:
        answer = 0
    
    elif len(input_2) == 2:
        answer = input_2[1] / input_1[0]
        
    elif len(input_1) == len(input_2):
        answer = input_1[0] + input_2[0]
        
    print(answer)
```

Test cases:

```python
my_function([0, 1], [0])
my_function([0], [0, 1])
my_function([1], [1])
my_function([1], ['1'])
```