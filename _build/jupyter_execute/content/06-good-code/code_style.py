# Code Style

In this chapter, we'll discuss a number of important considerations to make when styling your code. If you think of writing code like writing an essay, considering code style improves your code the same way editing an essay improves your essay. Often, considering code style is referred to as making our code *pythonic*, meaning that it adheres to the foundational principles of the Python programming language. 

Learning how to consider and improve your code style up front has a number of benefits. First, your code will be more user-friendly for anyone reading your code. This includes you, who will come back to and edit your code over time. Second, while considering code style and being pythonic is a bit more work up-front on developers (the people writing the code), it pays off on the long run by making your code easier to maintai. Third, by learning this now, early on in your Python journey, you avoid falling into bad habits. It's much easier to learn something and implement it than it is to unlearn bad habits. 

Note that what we're discussing here will not affect the functionality of your code. Unlike *programmatic errors* (i.e. errors and exceptions that require debugging for your code to execute properly), *stylistic errors* do not affect the functionality of your code. However, *stylistic errors* are considered bad style and are to be avoided, as they make your code harder to understand.

## Style Guides

Programming lanugages often have style guides, which include a set of conventions for how to write good code. While many of the concepts we'll cover here are applicable for other programming languages (i.e. being consistent), some of the specifics (i.e. variable naming conventions) are more specific to programming in Python.

<div class="alert alert-success">
Coding style refers to a set of conventions for how to write good code. 
</div>

### The Zen of Python

To explain the programming philosophy in Python, we'll first introduce what's known as *The Zen of Python*, which lays out the design principles of the individuals who developed the Python programming language. *The Zen of Python* is included as an easter egg in Python, so if you `import this` you're able to read its contents: 

import this

While we won't discuss each of these above we'll highlight two of these tenantsthat are particularly pertinent to the considerations in this chapter. Specifically, **beautiful is better than ugly** and **readability counts** together indicate that how one's code looks matters. Python prioritizes readability in its syntax (relative to other programming languages) and adheres to the idea that "code is more often read than it is written." As such, those who program in Python are encouraged to consider the beauty and readability of their code. To do so, we'll cover a handful of considerations here.

### Code Consistency

For very understandable and good reasons, beginner programmers often focus on getting their code to execute without throwing an error. In this process, however, they often forget about code style. While we'll discuss specific considerations to write well-styled python code in this chapter, the most important overarching concept is that **consistency is the goal**. Rules help us achieve consistency, and so we'll discuss a handful of rules and guidelines to help you write easy-to-read code with consistent code style. However, in doing so, we want you to keep the idea of consistency in mind, as programming is (at least partly) subjective. Since it's easier to recognize & read consistent style, do your best to follow the style guidelines presented in this chapter and once you pick a way to style your code, it's best to use that consistently across your code.

### PEP8

Python Enhancement Proposals (PEPs) are proposals for how something should be or how something shoudl work in the Python programming language. These are written by the people responsible for writing and maintaining the Python programming language. And, PEPs are voted on before incorporation. **[PEP8](https://www.python.org/dev/peps/pep-0008/)**, specfiically, is an accepted proposal that outlines the style guidelines for the Python programming language.

<div class="alert alert-info">
<b><a href="https://www.python.org/dev/peps/pep-0008/">PEP8</a></b> is an accepted proposal that outlines the style guide for Python.
</div>

The general concepts laid out in PEP8 (and in *The Zen of Python*) are as follows:
- Be *explicit & clear*: prioritize readability over cleerness
- There should be a *specific, standard way to do things*: use them
- Coding Style are *guidelines*: They are designed to help the code, but are not laws

#### PEP8: Structure

Throughout this section we'll highlight the PEP8 guideline, provide an example of what to avoid and hten demonstrate an improvement on the error. Note that for each "what to avoid" the code *will* execute without error. This is because we're discussing *stylistic* rather than *programmatic* errors here.

##### Blank Lines

- Use 2 blank lines between functions & classes and 1 between methods
- Use 1 blank line between segments to indicate logical structure

This allows you to, at a glance, identify what pieces of code are there. Using blank lines to separate out components in your code and your code's overall structure improves its readability.

**What to avoid**

In this example of what to avoid, there are no blank lines between segments within your code, making it more difficult to read. Note that if two functions were provided here, there would be 2 blank lines between the different function definitions. 

def my_func():
    my_nums = '123'
    output = ''
    for num in my_nums:
        output += str(int(num) + 1)
    return output

**How to improve**

To improve the above example, we can use what you see here, with variable definition being separated out from the `for` loop, being separated from the `return` statement. This code helps separate out the logical structures within a function. Note that we do *not* add a blank line between each line of code, as that would *decrease* the readability of the code.

# Goodness
def my_func():
    
    my_nums = '123'
    output = ''
    
    for num in my_nums: 
        output += str(int(num) + 1)
    
    return output

##### PEP8: Indentation

Use spaces to indicate indentation levels, with each level defined as 4 spaces. Programming languages differ on the speicfics of what constitutes a "tab," but Python has settled on a tab being equivalent to 4 spaces. When you hit "tab" on your keyboard within a Jupyter notebook, for example, the 4 spaces convention is implemented for you automatically, so you may not have even realized this convention before now!

**What to avoid**

Here, you'll note that, while the `print()` statement is indented, only *two* spaces are used. Jupyter will alert you to this by making the word `print` red, rather than its typical green.

if True:
  print('Words.')

**How to improve**

Conversely, here we see the accepted four spaces for a tab/indentation being utilized. Again, remember that the functionality of the code in this example is equivalent to that above; only the style has changed.

if True:
    print('Words.')

##### PEP8: Spacing

- Put one (and only one) space between each element
- Index and assignment don't have a space between opening & closing '()' or '[]'

**What to avoid**

Building on the above, spacing within and surrounding your code should be considered. Here, we see that spaces are missing around operators in the first line of code, whereas the second line has too many spaces around the assignment operator. We also see that there are unecessary spaces around the square brackets the list in line two and spaces after each comma missin in that same line of code. Finaly, in the third line of code there is an unecessary space between `my_list` and the square bracket being used for indexing.

my_var=1+2==3
my_list  =  [ 1,2,3,4 ]
el = my_list [1]

**How to improve**

The above spacingissues have all been resolved below: 

my_var = 1 + 2 == 3
my_list = [1, 2, 3, 4]
el = my_list[1]

##### PEP8: Line Length

- PEP8 recommends that each line be at most 79 characters long

Note that this specification is somewhat historical, as computers used to require this. As such, there are tools and development environments that will help ensure that no single line of code exceeds 79 characters. However, in Jupyter notebooks, the general guideline "avoid lengthy lines of code or comments" can be used, as super long lines are hard to read at a glance.

**Multi-line**

To achieve this, know that you can always separate lines of code easily after a comma. In Jupyter notebooks, if you hit return/enter on your keyboard after a comma, your code will be aligned appropriately. For example below you see that after the comma in the first line of code, the `6` is automatically aligned with the `1` from the line above. This visually makes it clear that all of the integers are part of the same list `my_long_list`. Using multiple lines to make your code easier to read is a great habit to get into.

my_long_list = [1, 2, 3, 4, 5, 
                6, 7, 8, 9, 10]

Further, note that you can explicitly state that the code on the following line is a continuation of the first line of code with a backlash (`\`) at the end of a line, as you see exemplified here:

my_string = 'Python is ' + \
            'a pretty great language.'

**One Statement Per Line**

While on the topic of line length and readable code, note that while you *can* often condense multiple statements into one line of code, you usually shouldn't, as it makes it harder to read.

**What to avoid**

For example, for loops *can* syntactically be specified on a single line, as you see here:

for i in [1, 2, 3]: print(i**2 + i%2)

**How to Improve**

However, in he code above, it's harder to read at a glance. Instead, what is being looped over should go on the first line with what code is being executed contained in an indented code block on lines underneat the `for` statement, as this is easier to read than the above example:

for i in [1, 2, 3]:
    print(i**2 + i%2)

##### PEP8: Imports

- Import one module per line
- Avoid `*` imports
- Use the import order: standard library; 3rd party packages; local/custom code

**What to avoid**

While you may still be learning which packages are part of the standard library and which are third party packages, this will become more second nature over time. And, we haven't yet discussed local or custom code, but this includes functions/classes/code you've written and stored in `.py` files. This should be imported last.

In this example here, there are a number of issues! First, `numpy` is a third party package, while `os` and `sys` are part of the standard library, so the order should be flipped. Second `*` imports are to be avoided, as it would be unclear in any resultant code which functionality came from the `numpy` package. Third, `os` and `sys` should be imported on separate lines to be most clear.

from numpy import *

import os, sys

**How to Improve**

The above issues have been resolved in this set of imports:

import os
import sys

import numpy as np

##### PEP8: Naming

- Use descriptive names for all modules, variables, functions and classes, that are longer than 1 character

**What to avoid**

Here, single character, non-descriptive names are used. 

a = 12
b = 24

**How to Improve**

Instead, python encourages object names that describe what is stored in the object or what the object is or does.

This is also important when you want to change an object name after the fact. If you were to "Find + Replace All" on the letter `a` that would change every single a in your code. However, if you "Find + Replace All" for `n_filters`, this would likely only change the places in your code you actually intended to replace.

n_filters = 12
n_freqs = 24

**Naming Style**

- CapWords (leading capitals, no separation) for Classes
- snake_case (all lowercase, underscore separator) for variables, functions, and modules

Note: snake_case is easier to read than CapWords, so we use snake_case for the things (variables, functions) that we name more frequently.

**What to avoid**

While we've been using this convention, it's important to state it explicitly here. Pythonistas (those who program in python) expect the above conventions to be used within their code. Thus, if they see a function `MyFunc`, there will be cognitive dissonance, as CapWords is to be used for classes, not functions. The same for `my_class`; this would require the reader of this code to work harder than necessary, as snake_case is to be used for functions, variables, and modules, not classes.

def MyFunc():
    pass
    
class my_class():
    def __init__():
        pass

**How to Improve**

Intead, follow the guideline above. Also, note that we've added two lines between the function and class definitions (to follow the guideline earlier in this chapter).

def my_func():
    pass


class MyClass():
    def __init__():
        pass

##### String Quotes

In Python, single-quoted strings and double-quoted strings are the same. Note that *PEP8 does not make a recommendation for this*. Rather, you are encouraged to be consistent: **pick a rule and stick to it.** (The author of this books is *exceptionally* bad at following this advice.)

One place, however, to choose one approach over another is when a string contains single or double quote character string literal. In this case, use the other one that's not included in the string to avoid backslashes in the string, as this improves readability. For example...

**What to avoid**

As you see below, you *could* use a backslash to "escape" the apostraphe within the string; however, this makes the string harder to read.

my_string = 'Prof\'s Project'

**How to Improve**

Instead, using double quotes to specify the string with the apostraphe (single quote) inside the string leads to more readable code, and is thus preferable.

my_string = "Prof's Project"

#### PEP8: Documentation

While documentation (including how to write docstrings and when, how and where to include code comments) will be covered more explicitly in the next chapter, we'll discuss the style considerations for including code comments and docstrins at this point. 

##### PEP8: Comments

First, out-of-date comments are worse than no comments at all. Keep your comments up-to-date. While we encourage writing comments to explain your thinking as you're writing the code, you want to be sure to re-visit your code comments during your "editing" and "improving code style" sessions to ensure that what is stated in the comments matches what is done in your code to avoid confusion for any readers of your code.

**Block comments**

Block comments are comments that are on their own line and come before the code they intend to describe. They follow the following conventions:

- apply to some (or all) code that follows them
- are indented to the same level as that code
- each line of a block comment starts with a # and a single space

**What to avoid**

In the function below, while the code comment does come before the code it describes (good!), it is not at the same level of indentation of the code it describes (not good!) *and* there is no space between the pound sign/hashtag and the code comment:

import random

def encourage():
#help try to destress students by picking one thing from the following list using random
    statements = ["You've totally got this!","You're so close!","You're going to do great!","Remember to take breaks!","Sleep, water, and food are really important!"]
    out = random.choice(statements)
    return out

encourage()

**How to Improve**

Intead, here, we see improved code comment style by 1) having the block comment at the same level of indentation as the code it describes, 2) having a space in between the `#` and the comment, and 3) breaking up the comment onto two separate lines to avoid having a too-long comment. 

The code style is also further improved by considering spacing within the `statements` list *and* considering line spacing throughout the function.

def encourage():
    
    # Randomly pick from list of de-stressing statements
    # to help students as they finish the quarter.
    statements = ["You've totally got this!", 
                  "You're so close!", 
                  "You're going to do great!",
                  "Remember to take breaks!",
                  "Sleep, water, and food are really important!"]
    
    out = random.choice(statements)
    
    return out

encourage()

**Inline comments**

Inline comments are those comments on the same line as the code they're describing. These are:

- to be used sparingly
- to be separated by at least two spaces from the statement
- start with a # and a single space

**What to avoid**

For example, we'll avoid inline comments that 1) are right up against the code they describe and 2) that fail to have a space after the `#`:

encourage()#words of encouragement

**How to Improve**

Instead, we'll have two spaces after the code, and a space after the `#`:

encourage()  # words of encouragement

##### PEP8: Documentation

We'll cover docstrings in the following chapter, so for now we'll just specify that PEP8 specifies that a descriptive docstring should be written and included for all functions & classes. We'll discuss how to approach this shortly!

## Exercises

Q1. **Considering code style, which of these is best - A, B, or C?**

A) 
```python
def squared(input_number):
    val = input_number
    power = 2    
    output = val ** power
    return output
```

B) 

```python
def squared(input_number, power=2):
    
    output = input_number ** power
    
    return output
```

C) 

```python
def squared(input_number):
    
    val = input_number
    power = 2
    
    output = val ** power
    
    return output
```

Q2. **Which of the following uses PEP-approved spacing?**

A) `my_list=[1,2,3,4,5]`  
B) `my_list = [1,2,3,4,5]`  
C) `my_list  =  [1, 2, 3, 4, 5]`  
D) `my_list=[1, 2, 3, 4, 5]`  
E) `my_list = [1, 2, 3, 4, 5]`

Q3. **If you were reading code and came cross the following, which of the following would you expect to be a class?**

A) `Phillies_Game`  
B) `PhilliesGame`  
C) `phillies_game`  
D) `philliesgame`  
E) `PhIlLiEsGaMe`  

Q4. **If you were reading code and came cross the following, which of the following would you expect to be a function or variable name?**

A) `Phillies_Game`  
B) `PhilliesGame`  
C) `phillies_game`  
D) `philliesgame`  
E) `PhIlLiEsGaMe`  

Q5. **Which of the following would not cause an error in Python and would store the string *You're so close!* ?**

A) `my_string = "You're so close!"`  
B) `my_string = "You"re so close!"`  
C) `my_string = 'You''re so close!'`  
D) `my_string = "You\\'re so close"`  
E) `my_string = 'You're so close!'`  

Q6. **Identify and improve all of the PEP8/Code Style violations found in the following code**:

```python
def MyFunction(input_num):
    
    my_list = [0,1,2,3]
    if 1 in my_list: ind = 1
    else:
      ind = 0
    qq = []
    for i in my_list [ind:]:
        qq.append(input_num/i)
    return qq
```

Q7. **Identify and improve all of the PEP8/Code Style violations found in the following code**:

```python
def ff(jj):
    oo = list(); jj = list(jj) 
    for ii in jj: oo.append(str(ord(ii)))
    return '+'.join(oo)
```