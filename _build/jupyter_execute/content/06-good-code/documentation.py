# Documentation

Documentation is a second piece on your path to writing strong code. Code style is the first, and code testing - to be discussed in the next chapter is the third. Together, these make up the strong code trifecta. 

In this chapter we'll discuss how to move beyond having good code style (which is important!) to have well-documented and well-commented code.

<div class="alert alert-success">
Code documentation is text that accompanies and/or is embedded within a software project, that explains what the code is and how to use it. 
</div>

Documentation is text that accompanies and/or is embedded within a software project that explains what the code is and how to use it. While there are many levels of documentations beyond what we'll discuss here, we'll focus on adding docstrings and code comments to your code. Documenting your code by including helpful comments and docstrings will take your code to the next level. As a rule, good code has good documentation - but code documentation should _not_ be used to try and fix unclear names, or bad structure, so we can't forget about code style and everything discussed in the last chapter. Specifically, *comments* should add any additional context and information that helps explain what the code is, how it works, and why it works that way to developers, whereas *docstrings* should make how to use the code clear to users. In this chapter we'll discuss both docstrings and comments, which together lead to well-documented code.

Most simply, documentation is incredibly important, undervalued, and underrated. Documentation is stuff written for humans in human language to help the humans. It does not affect the functionality of the code, but it does help the humans reading and using the code.

## Comments

Comments are string literals written directly in the code, typically directed at developers - people reading and potentially writing or editing the code.

As noted in the code style chapter, code comments should use `#`, followed by a space before the comment, and be written at the same indentation level of the code it describes. 

But, when exactly should you include comments in yoru code? Well, generally it's best for comments to focus on the *how* and *why*, over literally explaining what the code does. This is because you can expect individuals reading your code to have an understnding of the basic code constructs in Python. As such a comment that reads "`# this is a for loop`" will be distracting and uniformative.

Instead, good code comments should explain any context needed to understand the task at hand, give a broad overview of what approach you are taking to perform the task, and, if you're using any unusual approaches, explain what they are, and why you're using them.

As noted previously, comments *must* be maintained. Be sure to keep them up-to-date, meaning the comments included should apply to the code that is actually there. Out-of-date comments are worse than no comments at all.

Note that people new to writing code comments and documentation generally sometimes get hung up on questions like "How many comments do I need?" and "Should I comment every line?" Rather than ask these questions, we encourage you to keep in mind that comments should add context without being distracting. Typically, commenting every line makes your code *harder* to read and understand, which is to be avoided. Similarly, having *no comments* across all code in a project should also typically be avoided, as some explanation or context to those reading your code (including future you) would likely be beneficial.

**What to avoid**

Specifically, comments that explain what the code construct does literally, should be avoided. 

# This is a loop that iterates over elements in a list
for element in list_of_elements:
    pass

**How to improve**

Intead, you'd want to explain your thinking, along the general lines of what you see here (where X, Y, and Z would be replaced with specifics applicable to your project):

# Because of X, we will use approach Y to do Z
for element in list_of_elements:
    pass

## Docstrings

Unlike comments, which are intermingled among the code directly and included for developers (people reading the code), docstrings are descriptions and guides written alongside the code itself for code *users*. 

**Docstrings** are used to describe how to use the code stored in modules, classes and/or functions. Specifically, they describe the *operation* of the code.

<div class="alert alert-success">
<b>Docstrings</b> describe modules, classes and functions. They describe the operation of the code.
</div>



### `numpy`-style docsstrings

While there are a handful of different common approaches to writing docstrings in Python, we'll focus on writing `numpy`-style docstrings.


[Numpy style docs](https://numpydoc.readthedocs.io/en/latest/format.html) are a particular specification for docstrings. The documentation is extensive, so for more detail we encourage you to delve into their documentation...about docstrings. Here, we'll only ocver the basics. 

#### Docstring: `add()`

To introduce the syntax and formatting for a `numpy`-style docstring, we'll document a *very* simple function `add`. You'll notice a few things in the docstring below:

1. Docstrings begin and end with triple quotes.
2. Docstrings are added write beneath the line of code defining the function or class they're describing.
3. Jupyter notebooks will format docstrings using a red color.
4. The docstring below includes three parts: 1) a string describing what the function accomplishes, 2) the inputs (Parameters) to the function, and 3) the outputs (Returns) from the function.

def add(num1, num2):
    """Add two numbers together. 
    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    
    Returns
    -------
    answer : int or float
        The result of the addition. 
    """
    
    answer = num1 + num2
    
    return answer

Using the example above, we'll describe each of these three components above in a bit more details

**General Description**

`"""Add two numbers together."""` provides the user with a general description of what the function does. This can be a multi-line string and should describe generally the task accomplished by or goals of the function.

**Parameters**

The parameters section opens with "Parameters' with a line of dashes on the following line. Within this section, each input/argument to the fucntion, its corresponding type, and a description of the input is included.

For example `num1` is the parameter name. Separated by a colon (`:`), the type of that parameter is described (`int or float`). On the following line and indented, a short description of that parameter is included. The same pieces of information are included for the second parameter `num2`)

```python
    """    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    """
```

**Returns**

The formatting for the returns section mirrors that of the Parameters section; however, the information included reflects the variable or variables `return`ed from the function (or method).
```python
    """
    Returns
    -------
    answer : int or float
        The result of the addition. 
    """
```

In the `add()` function, there is a single output `answer`, which will be either an `int or float`, and can be described as "The result of the addition." 

As a reminder, complete docstrings can and should include even more information than what is described here. However, to get in the practice of documenting your code, including these three aspects is a great place to start. But, we encourage you to dig into the `numpy` docstring documentation to expand on your docuementation understanding. For one example of a complete docstring, you can check out the information included in the docstring for [`numpy.array`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html).

#### Accessing Docstrings.

Importantly, **docstrings** are available to you *outside* of the source code in a number of ways. 

**Aproach #1: `?`**

In a Jupyter notebook, documentation for an object can be accessed by adding a quesiton mark (`?`) after the object name: `add?`. This would pull the documentation up as a pop-up at the bottom of a Jupyter notebook. 

**Aproach #2: `help()`**

The `help()` function can be used to pull up the documentation in-line for any object:

help(add)

**Aproach #3: `__doc__`**

`__doc__` is also an attribute stored in an ocject. As with all attributes, the information stored can be accessed using `obj.__doc__`. Note that `__` is a dunder, or a double underscore. There are two leading and two trailing underscores around `doc`.

print(add.__doc__)

## Additional Documentation

As mentioned above, a complete software project will have documentation beyond code comments and docstrings. While we won't go into details here, we'll describe a few of the most common additional components of a well-documented software project briefly here:

- A `README` is a file that provides an overview of the project to potential users and developers
- A `LICENSE` file specifies the license under which the code is available (the terms of use)
- An `API Reference` is a collection of the docstrings, listing public interfaces, parameters and return values
- Tutorials and/or Examples show examples and tutorials for using the codebase

Full project documentation are often included on documentation sites, which host all of this information online, in a format accessible to and searchable by code users. An example of a well-documented code project is **scikit learn**, or as it's often abbreviated [`sklearn`](https://scikit-learn.org/stable/index.html).

## Exercises

Q1. **Docstrings are...**

A) written for code users  
B) written for developers  
C) to be read only by the author of the code  
D) essential for code execution

Q2. **Comments are...**

A) written for code users  
B) written for developers  
C) to be read only by the author of the code  
D) essential for code execution

Q3. **What is the difference between code comments and docstrings?**