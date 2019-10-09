---
interact_link: content/02-basics/variables.ipynb
kernel_name: python3
title: 'Variables'
prev_page:
  url: /02-basics/basics
  title: 'Python Basics'
next_page:
  url: /02-basics/operators
  title: 'Operators'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Variables

When programming in Python, you'll become very comfortable with creating variables. This is because *everything* in Python is implemented as an **object**. This means that whether you're working wither numbers, words, or booleans (we'll talk about these soon!, you're working with object.s These objects are stored in what we call **variables**.

In this chapter, we'll introduce how to define variables, a few different *types* of variables, and get you working with variables in Python. 

## Defining Variables

Variables are defined with a single equals sign (`=`). When variables are defined, we say that they are **assigned**. This is because, the information you want the variable to store (the information to the right of the `=`) is *assigned* to the variable (the thing on the left). This will always be true in Python - the variable will be to the left of the `=` and the information you want it to store on the right.

You can think of variables like a container. Containers store things, the same way variables store information. The label on the container is similar to the *name* of the variable. For example, let's define our first variable!

<div class="alert alert-success">
In programming, variables are things that store values. <b>Variables</b> are defined with <code>name = value</code>.
</div>



{:.input_area}
```python
# define the variable 'var_1'
var_1 = 6
```


With our container analogy, the variable `var_1` is the container. Like containers, variables store some information. The information stored in `var_1` is, in this case, the number 6. So, the name of the variable is `var_1` and the information assigned to it (or stored in it) is the number 6. You can store lots of different *types* of inrormation in variables. We'll discuss a few of them in this chapter and introduce even more later.

For example, variables can store words or letters, as you see here:



{:.input_area}
```python
# define the variable 'var_2'
var_2 = 'string'
```


This second variable - `var2` - has a different name than our first variable and stores different information. Here, it stores the word 'string'. We'll get to the different *types* of variables in just a second.

## Code Variables != Math Variables

An important point to discuss is that many people are familiar with the word **variable** from mathematics. However, variables in *code* are not the same thing as variables in math.

For example, in mathematics `=` refers to equality. It's a *statement of truth*. It states that whatever is to the left of the `=` is equal to whatever is to the right of the `=`.

This is not the case when it comes to code. Instead, `=` refers to assignment. It states that whatever is to the right of the `=` should be assigned - *or stored in* the variable to the left.

For example, when it comes to mathematics and algebra, we're familiar with the concept of solving for x. If you were asked 'What is $x$?' and given the expression $y = x + 2$, you would subtract 2 from the right side so that $x = y -2$. The same logic does *not* follow in programming.

For example, if you were asked 'What is `x`?' and given the following two lines of code:

```python
x = 2
x = x + 1
```

you would tell me that `x` is 1 more than its previous value of 2, so `x = 3`.

That line of code there: `x = x + 1` wouldn't make sense in mathematics, but it makes perfect sense in code. This is because code variables use `=` for assignment, and not as a statement of truth and equality.

### Reminders

- In programming `=` means assignment
- Anything to the right of the `=` is evaluated before assignment
- Names are always on the left of the `=`, values are always on the right

## Naming Variables

So far, we've only defined a few variables, and we haven't yet specified the *rules* for variable assignment. There are a whole bunch of options for how you name your variables and only a few rules.

The rules are:
1. Names are case sensitive
2. Variables must start with letters
    - After that, they can include numbers, and underscores
    - They cannot include special characters (like &, *, #, etc)
3. Python doesn't care what you name your variables
    - Humans do care. Pick names that describe the data / value that they store
    
### Names are case-sensitive

In programming, capitalization matters *a lot*. `VAR_1` and `var_1` are interpreted as two *different* variables when it comes to code. Be mindful of capitalization. Capital and lower-case letters are interpreted by the computer as two different characters.

### Variables must start with letters

We saw that variables can contain numbers and underscores when we created `var_1` earlier, and while they can *contain* numbers or underscores, they cannot *begin* with anything other than a letter. So, `_var1` or `1_var` would not be acceptable variable names. If you try to create a variable that starts with anything other than a letter, Python will give you a `NameError`.

Additionally, Python does not allow variables names to contain a few special characters (ie. &, \*, #, etc). If you try to create a variable with a special character, Python will give you a `SyntaxError`. Thus, it's best to limit variable names to include letters, underscores, and numbers.

### Python doesn't care what you name your variables

Python doesn't care whether your variable name is `a` or `heights`; however, humans do. So, pick variable names that are informative about the information stored within the variable. For example, `a` doesn't clue the human reader of the code into what information is stored in the variable. However, `heights` lets the person reading the code (which could be you in the future or someone else). 




## Reserved Words

Beyond those three rules, here are 33 words that are not allowed to be used for variable assignment in Python. These are words that have a particular meaning in Python and thus you're not allowed to use them for variable assignment. If you try to define a variable with one of these names, you'll get a `SyntaxError`.

<table type="text/css">
  <tr>
      <td><code>False</code></td>
      <td><code>None</code></td>
      <td><code>True</code></td>
      <td><code>and</code></td>
      <td><code>as</code></td>
      <td><code>assert</code></td>
      <td><code>break</code></td>
  </tr>
  <tr>
      <td><code>class</code></td>
      <td><code>continue</code></td>
      <td><code>def</code></td>
      <td><code>del</code></td>
      <td><code>elif</code></td>
      <td><code>else</code></td>
      <td><code>except</code></td>
  </tr>
  <tr>
      <td><code>finally</code></td>
      <td><code>for</code></td>
      <td><code>from</code></td>
      <td><code>global</code></td>
      <td><code>if</code></td>
      <td><code>import</code></td>
      <td><code>in</code></td>
  </tr>
  <tr>
      <td><code>is</code></td>
      <td><code>lambda</code></td>
      <td><code>nonlocal</code></td>
      <td><code>not</code></td>
      <td><code>or</code></td>
      <td><code>pass</code></td>
      <td><code>raise</code></td>
  </tr>    
  <tr>
      <td><code>return</code></td>
      <td><code>try</code></td>
      <td><code>while</code></td>
      <td><code>with</code></td>
      <td><code>yield</code></td>
  </tr>    
</table>




{:.input_area}
```python
# you will get an error if you try to assign a variable to one of these words
try = 6
```


{:.output .output_traceback_line}
```

      File "<ipython-input-4-1c44ba76d8f9>", line 2
        try = 6
            ^
    SyntaxError: invalid syntax



```

## How Code Executes

So far we've been writing and executing code within a Jupyter notebook. But, what does that mean? What is the notebook and how does it know that I want to execute code?

### Kernel

<div class="alert alert-success">
The <b>kernel</b> is the thing that executes your code. It is what connects the notebook (as you see it) with the part of your computer that runs code. 
</div>

Your kernel also stores your **namespace** - all the variables and code that you have declared (executed). 

It can be useful to clear and re-launch the kernel. You can do this from the 'kernel' drop down menu, at the top of your Jupyter notebook, optionally also clearing all outputs. Note that this will erase any variables that are stored in memory. 

### Namespace

<div class="alert alert-success">
The <b>namespace</b> is the 'place' where all your currently defined code is declared - all the things you have stored in active memory. 
</div>

For example, when code is typed, nothing happens and the variable does *not* exist *until* the code is executed. Once executed, the variable is stored in memory within your **namespace**.



{:.input_area}
```python
# once you create a variable it's stored in your namespace
my_variable = 6
```


Within a Jupyter notebook, you can always use the `%whos` magic command to get information about what variables have been defined in your current Namespace. For example, here, you'll see all the variables currently in our namespace. In other words, all the cells where we've run code and created variables in this Jupyter Notebook will show up when we execute `%whos`. 

Note that variables created in a *different* notebook are stored in their own, separate namespace. The variables created in this notebook are the only ones stored in its namespace.



{:.input_area}
```python
# You can list everything declared in the namespace with '%whos'
%whos
```


{:.output .output_stream}
```
Variable      Type    Data/Info
-------------------------------
a             int     6
my_variable   int     6
var_1         int     6
var_2         str     string

```

There are a number of **magic commands** available from within Jupyter notebooks that would not be avaialable in an interactive Python notebook. You'll be able to identify these as they always start with `%`.

## Variable Types

<div class="alert alert-success">
Every variable has a <b>type</b>, which refers to the kind of variable that it is, and how the computer stores that data.
</div>

To check what the type of any variable is, we'll use the `type()` function.

This is the first Python function we're using, but there will be many throughout this content. So, it's best to get familiar with the syntax now. When running a function the syntax is: `function_name()` This means that the call begins with the function name, followed by parentheses. Within the parenthesis, you'll provide information. 

Here, the `type()` function requires a variable that you've defined. This code will return the `type` of the information stored within `variable_name`:



{:.input_area}
```python
# Declare a variable
variable_name = 1

# You can always ask Python 'what type is this variable' using:
type(variable_name)
```





{:.output .output_data_text}
```
int
```



Here, Python returns `int`. This means that the information stored in `variable_name`, the value 1, is an integer.

### Int

Int is the variable type for storing and working with integers. Here, your mathematics training will not steer you wrong.

<div class="alert alert-success">
<b>Integers</b> store whole numbers.
</div>



{:.input_area}
```python
my_integer = 1
another_integer = 321
```


Integers can be positive or negative. Integers less than zero can be defined by putting a `-` before the integer during assignment:



{:.input_area}
```python
# integers can be signed
yet_another_integer = -4
type(yet_another_integer)
```





{:.output .output_data_text}
```
int
```



As a reminder, you can always check the type of an integer using the `type()` function.

### Float

Similar to integers, floats also store numeric information; however, floats store decimal-point numbers (rather than whole numbers).

<div class="alert alert-success">
<b>Floats</b> store signed, decimal-point numbers.
</div>



{:.input_area}
```python
my_float = 1.0
another_float = -231.45
```


Float type variables will return 'float' when using the `type()` function.



{:.input_area}
```python
type(another_float)
```





{:.output .output_data_text}
```
float
```



### String

Not all variable types require quantitative or numeric information. Character information are stored as strings.

<div class="alert alert-success">
<b>Strings</b> store characters, as text. 
</div>



{:.input_area}
```python
# declare string variables
my_string = 'words, words, words'
another_string = 'more words'
```


Note that strings are declared by placing *quotation marks around the characters*. In Jupyter notebooks, strings are colored red to visually indicate that this information is a string. If you look above, numeric information is colored green, with negative signs being purple. These visual clues are meant to help you keep track of information when coding more easily. 

When declaring the first string variables above, we used single quotation marks. However, Python interprets single and double quotes the same way. So, you *could* define strings using double quotes:



{:.input_area}
```python
# Note that strings can be defined with either '' or ""
and_another = "and some more"
```


String type variables will return 'str' when using the `type()` function.



{:.input_area}
```python
type(and_another)
```





{:.output .output_data_text}
```
str
```



#### Quotation Marks

A quick note to further clarify about quotation marks and how they work within strings. Above, we saw that strings are declared by placing the characters of the string within single or double quotation marks. 

For example:



{:.input_area}
```python
my_string = 'This is a single-quoted string.'
my_string
```





{:.output .output_data_text}
```
'This is a single-quoted string.'
```





{:.input_area}
```python
my_string = "This is a double-quoted string."
my_string
```





{:.output .output_data_text}
```
'This is a double-quoted string.'
```



Note that Jupyter will put single quotes around the string when printed, even if you specify double quotes in the output. This is because the quottaion marks are interpreted equivalently by Python.

A general principle is to *pick something and be consistent*. This applies across all of programming. It's best to be consistent in how you name your variables, how you assign your strings, how you align and comment your code, etc. Consistency makes your code easier to read. 

The best advice here is to pick something and stick to it. 

#### What if you *want* a quotation mark within your string?

But, what if you *wanted* a quotation in the string you're delcaring? For example, what if your string had a contraction like 'don't' or 'won't'? What would you do then? Well, there are a few options:

- use double quotes outside with apostraphe inside quotes
- use an escape `\` (backslash) before charater

Here is an example of what you can do to get your apostrophe to show up. If you declare your string with double quotes, Python will wait until it sees another set of double quotes to end your string. Thus, your apostrophe gets interpreted as an apostrophe.



{:.input_area}
```python
# double quotes on outside; single quote inside
my_string = "I wan't to see a quote."
my_string
```





{:.output .output_data_text}
```
"I wan't to see a quote."
```



Alternatively, whenever you want to specify for Python to interpret a special character (such as `"`) as a string literal, you can use the escape character `\` before the special character. This tells Python to interpret the character following the backslash as the character it is, not how Python would normally interpret it.



{:.input_area}
```python
# backslash to "escape" quotation mark
string_quote = "And she said, \"Please teach me Python!\""
string_quote
```





{:.output .output_data_text}
```
'And she said, "Please teach me Python!"'
```



## Boolean

Booleans are a special type of variable used to help control the flow of your code. They can only store two different values: `True` and `False`.

<div class="alert alert-success">
<b>Booleans</b> store only two values: <code>True</code> or <code>False</code>. 
</div>

While there are only two values this type of variable can take, they are very powerful! Specifically, booleans are named after the British mathematician - George Boole. He first formulated Boolean algebra, which are a set of rules for how to reason with and combine these values. This is the basis of all modern computer logic!

To define a boolean, assign the value `True` or `False` to your variable.



{:.input_area}
```python
my_bool = True
another_bool = False
```


Boolean type variables will return 'bool' when using the `type()` function.



{:.input_area}
```python
type(another_bool)
```





{:.output .output_data_text}
```
bool
```



## None

Last but not least (for now!), `None` type variables are used to store the concept of nothing. This is the type of Python variable used to specify an empty or null value.

<div class="alert alert-success">
<b>None</b> is a special type that stores the concept of nothing. It is used to denote a null or empty value.
</div>



{:.input_area}
```python
the_concept_of_nothing = None
```


None type variables will return 'NoneType' when using the `type()` function.



{:.input_area}
```python
type(the_concept_of_nothing)
```





{:.output .output_data_text}
```
NoneType
```



### Mutable vs Immutable

The variable types we've talked about so far are all **immutable**. This means they cannot be altered after they're created. 

<div class="alert alert-success">
<b>Immutable</b> variable types cannot be altered once defined.
</div>

In this example here, we declare a string, calling it `immutable_string`. The second line of code looks unfamiliar. For now, know that `[4]` indicates that I want to know what the fifth character in the string is. So, `immutable_string[4]` returns the fifth character in the string - the `i` in 'Pythin'.



{:.input_area}
```python
# cannot change part of the string after creation
immutable_string = 'Pythin is the best!'
immutable_string[4]
```





{:.output .output_data_text}
```
'i'
```



As strings are *immutable*, if we try to assign the letter 'o' to the fifth position in our string, we'll get a `TypeError`. Python is letting us know that `str` type objects cannot be modified once created.



{:.input_area}
```python
immutable_string[4] = 'o'
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-31-97c531a4a087> in <module>()
    ----> 1 immutable_string[4] = 'o'
    

    TypeError: 'str' object does not support item assignment


```

To change an immutable type variable, you would have to redefine the variable.

For example, if we wanted to change the above string to read 'Python is the best!', we would have to re-define the variable `immutable_string`:



{:.input_area}
```python
# redefine variable
immutable_string = 'Python is the best!'
immutable_string
```





{:.output .output_data_text}
```
'Python is the best!'
```



Whatever variable was most recently defined is what will be stored in your namespace. This means that you *can* overwrite variables without even noticing. The best way to avoid overwriting variables is to use informative and memorable variable names that specify what information is stored in the variable. 

Note: Python does have **mutable** types. We'll talk about these soon!

## Aside: Whitespace

Just a quick word on indentation before we get any deeper into Python

Python *does* care about whitespace. This means that indentation matters. You *will* get an error if it Python runs into unanticipated whitespace.

In the example here, there is an unexpected tab before `print(b)`. Python returns and `IndentationError` and points to this line of code.



{:.input_area}
```python
a = 1
b = a
    
    print(b) 
```


{:.output .output_traceback_line}
```

      File "<ipython-input-27-b7d7efbb406d>", line 2
        b = a
        ^
    IndentationError: unexpected indent



```

There *are* times when indentation will be required and expected. We'll discuss these in detail soon.

However, there are times when whitespace isn't *required* but is *preferred*. Just like when it comes to writing, there are different *styles* of writing. Writing code has it's own *style* too!

For example, when assigning variables, we've been leaving a space on either side of the `=`. This is *not* required, but does make for easier reading on the viewer.



{:.input_area}
```python
# good style spacing
my_variable = 6
```


Python interprets the following *exactly* the same as the previous line of code. However, it's harder for the humans to read. 



{:.input_area}
```python
# less ideal spacing
my_variable=6
```


The same goes for lines between code. Python doesn't care if there are spaces between lines of code. However, it can be helpful to leave spaces between different "chunks" of code. This visually spaces things out for those reading you. code! You'll see examples of this soon as we start writing longer bits of code.

We encourage you to pay attention to the spacing used throughout this book and in others code. We'll also try to be explicit about Python code style preferences throughout the book so you can learn good habits right off the bat!

## Exercises

1. **What is the value of `a` after executing the following code?**

```python
a = 'string'
b = a
a = 6
```


2. **After executing the following code, what will be the value of `my_var`?**

```python
my_var = 2 
my_var = my_var + 1
```

3. **What would be the value of `b` after running hte following code?**

```python
a = 16
b = 'string'
c = a
b = 72
my_variable = True
print(b)
```

A) 'string'  
B) 88  
C) 72  
D) This code will fail  

4. **After executing the following code, what will be the value of `var_2`?**

```python
var_2 = var_1 = 1
print(var_2)
```

A) 'var_1'  
B) 1  
C) 2  
D) This code will fail 

5. **For each of the following variables, identify what `type` of variable was defined.**

```python
var_a = -17.5
var_b = '-17.5'
var_c = 'python'
var_d = 29
var_e = True
var_f = 'True'
var_g = None
```

6. **After executing the following code, what will the values stored in `a` and `b` be?**

```python
a = 1
b = a
a = 2

print(a)
print(b)
```

A) `a` and `b` both store 1  
B) `a` and `b` both store 2  
C) `a` stores 2 `b` stores 1  
D) `a` stores 1 `b` stores 2  
