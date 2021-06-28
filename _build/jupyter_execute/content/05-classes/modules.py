# Modules 

Having now introduced the idea that objects can have attributes and associated methods, as we saw with `date` and `datetime` type objects, let's briefly discuss modules, which provide users access to functions and objects for carrying out particular tasks before we see how to define our own object types in the next chapter. 

## modules & imports

**Modules** are files that store python code that can be `import`ed into your Namespace for use. Specifically, in the last chapter we `import`ed from the `datetime` module without really discussing what that meant. We'll pause here to ensure that we understand what modules are, what modules are available to you, and how `import`s work.

<div class="alert alert-success">
A <b>module</b> is a set of Python code with functions, classes, etc. available in it. A Python <b>package</b> is a directory of modules.
</div>

In hte last chapter when we specified `from datetime import date` this indicated that we wanted to `import`, meaning make available in my current Namespace the `date` object. However, we need to indicate to python *where* t find the `class` definition for that object type. In this statement we indicated that it could be found in the `datetime` module. Upon executing this `import` statement, one can then use the `date` type object. 

### Why `import`? 

<div class="alert alert-success">
<code>import</code> is a keyword to import external code into the local namespace.
</div>

There is *a lot* of Python code out in the world, with different people using Python for vastly different tasks. For example, the functions/classes used by a neuroscientist analyzing brain imaging data would be vastly different than the functions/classes being used by a software engineer developing an app. Therefore, you wouldn't want Python to make *all* code ever written available on installation. First, that would take a long time, making python take a long time to open up. Second, there are only so many different function names. Certain modules/packages could have functions/classes with the same names. If they were all installed at once, it would be hard to figure out exactly which function/class had been imported most recently, and thus would break programs.

To avoid these issues, Python only front-loads those functions and object types that are commonly used across all Python programmers (i.e. `range`, `len`, `type`, `list`, `int`, etc.), requiring any additional functionality to be `import`ed prior to use.

### What's available? 

Some modules are available with every single python installation. These tend to be general use modules, or things that many different Python programmers will find useful, regardless of their specific field. These modules and the functionality within them can be `import`ed at any time so long as Python has been installed. These modules are said to be part of the Python **standard library**. All of these modules are listed [here](https://docs.python.org/3/library/); however, we'll note a few of the most-commonly used here and describe when they're helpful:

- `random` - to "generate psuedo-random numbers" and carry out tasks with randomness (i.e. selecting a value at random from a collection)
- `collections` - for common operations with collections (dict, tuple, list, etc.)
- `datetime` - for operating with dates
- `math` - for carrying out mathematical operations
- `os` - for interfacing with your operating system (including file system)
- `re` - for operating on regular expressions

These, and all modules that are part of the standard library can be `import`ed, after which their functionality is available in your current Namespace.

### How to `import`?

Prior to `import`ing a module, its functionality will not be available in your namespace. For example, prior to importing the `math` module if you ask what type of object `math` is, an error will be returned, as `math` is not yet in your current Namespace:

# we haven't imported the module yet
# this code fails if you haven't yet imported math
type(math)

To access the `math` module, it must first be imported into your current Namespace. Most simply this can be done with the general syntax: `import module_name`. For example, to import the `math` module, you could use the following:

import math

The above imports the `math` module into your current namespace, such that if you, at this point, check for the `type` of math, an error is no longer returned, as `math` has been `import`ed.

# Check the type of math
type(math)

By importing, we now have access to the functionality within this module. For example, the `math` module includes a function `sqrt` for calculating the square root of a number. 

To execute a function from a module, you must first specify the module name, followed by a `.` and then the function to be executed:

math.sqrt(9)

### What functionality is available?

While it can be intimidating at first, much of the functionality in these commonly-used modules will become familiar over time. However, you can always look up what's available within a module using the `dir()` function, which returns all available attributes, functions, and methods of a given module/function/class.

For example, for the `math` module, we see a handful of different functions/attributes, including `sqrt()`, which we used above. (We'll ignore the "dunder"s (double underscores) for now.)

dir(math)

### `import`s: `from` & `as`

Above we specified `import module_name` and then provided access to all functionality within the module specified. However, sometimes you know there's only a single function or single object type that you want to use in your code. In those cases, there's no need to `import` the *entire* module. Instead, we can use `from` to *only* `import` the objects we intend to use in our code. 

<div class="alert alert-success">
<code>from</code> allows us to decide exactly what objects to import into our Namespace
</div>

For example, if the *only* thing we wanted to use from the `random` module was the `choice` function, rather than using the `import` statement `import random`, which would provide access to the entire `random` module in our Namespace, we can instead use the general syntax `from module_name import function`:

from random import choice

When we specify specifically what it is we want to import, when we go to execute (use) this function, we no longer have to first specify the module name. Rather, we can call the function directly:

choice(['a', 'b', 'c', 'd', 'e'])

Note that the above function chooses a value at random from the list. Thus, if you're following along, you likely won't see the same specific output value; however, the value you see will be a character between 'a' and 'e' as those are the values from which `choice` is choosing one at random.

Similarly, `as` allows for users to specify what name should be used in your code for an object that is imported. This can be helpful when 1) the names of an object to be used is really long and 2) when there are multiple objects with the same name, avoiding confusion.

<div class="alert alert-success">
<code>as</code> allows us to decide exactly what name to use for a module's functionality in our Namespace.
</div>

For example, `collections` is a bit long. If you wanted to `import` all the functionality from that module into your Namespace, but didn't want to have to type `collections` every time you wanted to use an object from that module, you could instead `import` the module as follows: 

import collections as cols

The above would import all the functionality from the `collections` module into your Namespace; however, it would use the name `cols`, instead of `collections`. Thus, if you attempted to access the functionality by referring to `collections`, the following would error (as `collections` has not been imported by that name):

# this will produce an error
dir(collections)

However, the following would provide you with information about the functionality in the `collections` module, since it was imported using the short name `cols`:

dir(cols)

Note that `from` `import` and `as` can be used in concert. For example,

from string import punctuation as punc

the above statement `import`s the `punctuation` object from the `string` module, giving it the short name `punc` in our current Namespace.

<div class="alert alert-danger">
Warning: The order will always be `from` -> `import` -> `as`. <code>import ascii_letters from string</code>, for example, will provide an error, as the <code>from</code> statement comes <it>after</it> the <code>import</code> statement.
</div>

### `*` `imports`

Occasionally you will see `from module_name import *`, where the `*` acts as a wildcard, meaning "everything". The statement `from module_name import *` should be read as "import everything from module_name"; however, this is generally bad practice. The reason for this is because later in your code when you refer to and use an object from the module, it will be unclear *where* that function came from, given the use of the wildcard. 


<div class="alert alert-danger">
Warning: <code>*</code> <code>imports</code> are to be avoided.
</div>

import random 
dir(random)

## Exercises

Q1. **Which of the following is NOT a valid Python `import` statement?**

- A) `import collections as col`
- B) `from statistics import mean as average`
- B) `from os import path`
- D) `from random import choice, choices`
- E) `import ascii_letters from string`

Q2. **If the statement `import random` were used, how would one specify use of the `sample` function from that module?** 

- A) `import sample`
- B) `random.sample()`
- B) `sample()`
- D) `rand.sample()`
- E) `from random sample()`

Q3. **If the statement `from math import sqrt` were used, how would one specify use of the `sqrt` function from that module?** 

- A) `from math sqrt()`
- B) `import sqrt`
- B) `m.sqrt()`
- D) `math.sqrt()`
- E) `sqrt()`