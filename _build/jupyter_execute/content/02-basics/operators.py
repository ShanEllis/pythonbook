# Operators

Very generally, programming with Python - at its core - is a way to ask computer to store values and do things with them. We've now discussed variable definition and a number of the types of  variables that exist in Python. But we haven't *really* started doing thins with them yet. Doing things with code requires carrying out **operations**. This is accomplished by using a number of types of **operators**. We'll introduce the different types of operators here and demonstrate how they're used when writing code.

<div class="alert alert-success">
<b>Operators</b> are special symbols in Python that carry out arithmetic or logical computation.
</div>

We'll discuss assignment, math, comparison and identity operators here.

## Assignment Operator

You're already familiar with the Python operator you'll use most often - the **assignment operator**. The aassignment operator is what you've been using for assignment - the `=`. It allows you to store information in a variable!

<div class="alert alert-success">
Python uses <code>=</code> for <b>assignment</b>.
</div>

# assignment operator
my_var = 1

## Math Operators

Beyond assignment, **math operators** will be very helpful whenever you want to carry out a calculation. At its simplest, Python is a calculator. It allows you to carry out calculations using these math operators. 

The first four math operators we'll introduce are `+`, `-`, `*`, and `/`, which are used for addition, subtraction, multiplication, and division, respectively. 

These operators return *numbers*.

<div class="alert alert-success">
Python uses the <b>mathematical operators</b> <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code> for 'sum', 'substract', 'multiply', and 'divide', repsectively.
</div>

Values can be added directly using the mathematical operators.

# addition
8 + 4

However, math operators can also be carried out using variables that store numbers. This is likely how you'll utilize math operators more often.

# addition using variables
var_a = 8 
var_b = 4

var_a + var_b

Once defined, these variables can be used for all types of calculations, such as for subtraction, multiplation, or division:

# subtraction
var_a - var_b

# multiplcation
var_a * var_b

# division
var_a / var_b

In addition to the four math operators introduced, Python also has math operators for exponentiation (`**`), floor division (`//`), and returning the remainder, using what is known as the modulus (`%`).

<div class="alert alert-success">
Python also has <code>**</code> for exponentiation,<code>%</code> for floor division (or integer division), and <code>%</code> for remainder (called modulus). These also return numbers.
</div>

To raise the number 2 to the power 3, carrying out the calculation that in mathematics would be denoted $2^3$, you would use the exponent operator (`**`):

# exponentiation
2 ** 3

To carry out floor division, which returns only the integer value from dividing two numbers, you would use the floor division operator (`//`):

# floor division 
17 // 6

Above you see that 6 goes into 17 twice. It ignores the fact that there's a remainder of 3, providing only the integer. Note that if we were to use the division operator (`/`), a float is returned and the value of 17 divided by 6 is approximately.

# division
17 / 6

It's important to keep in mind that floor division does *not* round. It only returns the integer from the division, which in this case is 2.

If you want the remainder of 17 divided by 6, there's an operator for that - the modulo `%`. This operator divides 17 by 6 and returns only the remainder, which is the value 5.

# remainder of 17 divided by 6
17 % 6

## Order of Operations

Mathematical operators follow the rules for order of operations you learned in mathematics class, learning PEMDAS or "Please Excuse My Dear Aunt Sally" to learn the following order of operations:

- Parentheses
- Exponents
- Multiplication & Division
- Addition & Subtraction

In this first example, we see that `16 / 2` is calculated first, as it is division, followed by the addition of the value 3, ultimately returning the value '11.0' when executed. 

# division before addition
order_operations = 3 + 16 / 2
order_operations

Note, that if you wanted addition to occur first, you would use parentheses:

# use parentheses to specify addition first
specify_operations = (3 + 16) / 2
specify_operations

## Recap: Math Operators


- `+`, `-`, `*`, `/` for addition, subtraction, multiplication, & division
- `**` for exponentiation & `%` for modulus (remainder)
- `//` for floor division (integer division)

## Logical (Boolean) operators

Logical or Boolean operators use what is known as **Boolean logic** to carry out logical operations on the computer. We'll review these rules and demonstrate how they operate in Python. 

The logical operators are `and`, `or`, and `not`.

As mentioned previously, booleans are named after the British mathematician - George Boole. He first formulated Boolean algebra, which are a set of rules for how to reason with and combine these values. This is the basis of all modern computer logic.

Unlike math operators, which return numbers, boolean operators return booleans.

<div class="alert alert-success">
Python has <code>and</code>, <code>or</code> and <code>not</code> for <b>boolean logic</b>. These operators return booleans.
</div>

Booleans adhere to the following logic:

- `and` : True if both are true
- `or` : True if at least one is true
- `not` : True only if false

Following this logic, all of the following return `True`:

True and True

True or True

True and not False

not False

# two nots cancel one another out
not (not True)

### Capitalization matters

As discussed previously, capitalization matters in programming. Booleans are specified with only the T in True and the F in False being capitalized. If you were to specify a different capitalization, you would get a `NameError`. 

In addition to the error, Jupyter provides you with a visual clue. Note that in the examples above, the Booleans and operators are all bold, green font. Below, `TRUE` is neither bold nor green, cluing you into the fact that these are not booleans.

# this will give you an error
# 'TRUE' is not a boolean
TRUE and TRUE

### Short-circuit evaluation

Before we move any further, let's discuss how Python interprets boolean operators. Python uses what is known as **short-circut evaluation**. This means that the second argument in the boolean expression is evaluated only if the first argument does not definitively determine the value of the expression. Let's look at an example:

Here, Python looks at `False and` and determines that, when using `and` both sides have to be True for the expression to evaluate as True. Given that the left-hand side is False, Python *knows* that it can stop and does not even have to look at or evaluate the right-hand side. The expression thus evaluates as `False`.

# python stops after False
# no need to check second expression
# since first is False
False and print("Hi")

Conversely, if Python encounters `True` on the left-hand side, when Python encounters the `and` operator it knows it still has an opportunity for both sides to evaluate as True. It thus continues on to evaluate the right-hand side and prints "Hi".

# Continues to evaluate the expression
True and print("Hi")

This leaves one final combination to discuss. Here, Python evaluates the left-hand side, printing "Hi" before it encounters the `and` operator. It continues on to encounter the `False` and finishes its evaluation of the code.

# evaluates print statement before and
print("Hi") and False

Python behaves in this way, using short-circuit evaluation, to save itself time. If it knows an expression will evaluate as False by only evaluating the left-hand side of the expression, there is no need for it to continue on to look at and use computational power to evaluate the right-hand side of the expression. Overall, this makes Python more efficient.

## Comparison Operators

Comparison operators compare the values on either side of the operator, returning a boolean from the comparison. 

Python uses the following **comparison operators**:

- `==` : values are equal
- `!=` : values are not equal
- `<` : value on left is less than value or right
- `>` : value on left is greater than value on right
- `<=` : value on left is less than *or equal to* value on right
- `>=` : value on left is greater than or equal to value on the right

<div class="alert alert-success">
Python has comparison operators <code>==</code>, <code>!=</code>, <code><</code>, <code>></code>, <code><=</code>, and <code>>=</code> for <b>value comparisons</b>. These operators return booleans.
</div>

We mentioned previously that `=` is used for assignment rather than equality. However, there is a way to test whether two values are equal. To test equality, you'll use the `==` comparison operator. This determines whether the left-hand side of the expression is equal to the right-hand side, returning hte boolean `True` if they are equal, and `False` otherwise.

# compare equality
True == True

Note that you are not limited to comparing booleans with comparison operators. Here we determine whether two strings are equal.

'aa' == 'aa'

The same logic follows for the other comparison operators, which allow you to determine whether two things are *not* equal:

True != False

and whether a value is less than or equal to another value:

12 <= 13

## Understanding Boolean logic

When first learning booleans, we sometimes *think* we know what we're asking the computer to do, but our logic can be flawed.

We present these details now so that you don't fall into a trap that many beginners make early on in their journey to understand Booleans. 

To do so, there are three rules you'll have to understand.

**Rule #1**: Python considers empty strings as having boolean value of `False`. Non-empty string as having boolean value of `True`.

We see this play out in the examples here:

# empty string
empty_string = ''
bool(empty_string)

Above we see an empty string, created with two quotation marks, evaluates as False. We can determine how a variable will evaluate using `bool()` with the variable name of interest inside the parentheses. 

On the other hand, below, we see that a string with characters in it, will evaluate as `True`:

nonempty_string = 'string has something in it'
bool(nonempty_string)

bool(None)

**Rule #2** For the `and` operator, if left value is `True`, then right value is checked and returned. If left value is `False`, then that left value is returned.

This follows with the short-circuit evaluation we've already discussed. If the left-hand side of the expression is True and Python encounters an `and`, it continues on.

We've seen this before when comparing booleans:

# left value True, returns right value
True and False

But, the same logic holds when comparing strings, for example. Here we see a non-empty string (`'a'`) on the left-hand side. This evaluates as true. So, Python returns the right-hand side accordingly:

'a' and 'b'

Taking this a step further, we can combine logic and comparison operators. So, let's think about the following expression:

# the left value in parentheses is True
'a' == ('b' and 'a')

If you're new to programming you may see the line of code above and think it's asking if the string 'a' is equal to both 'b' and 'a'. You may *expect* this to return `False`; however, if you're following the rules we've been discussion, you'll know that this expression evaluates as `True`. Let's discuss why.

Well, first things first, we know that parentheses are evaluated first, so Python first evaluates the following:

'b' and 'a'

Thus, the expression above is really asking if the string 'a' is equal to the string 'a', which of course is `True`:

'a' == 'a'

Following that logic, we then know that the following evaluates as `False` because this line of code is asking whether the string `a` is equal to the string `b`, which is `False`.

# evaluates if 'a' is equal to 'b'
'a' == ('a' and 'b')

**Rule #3**: For the `or` operator if left value is `True`, then it is returned, otherwise if left value is `False`, then right value is returned.

Again, this makes sense when we think back to short-circuit evaluation. If the left-hand side is `True` and an `or` is encountered, there is no need for Python to evaluate the right-hand side, as at least one side is true. Accordingly, Python returns the left-hand value.

# left-hand is True and returned
'a' or 'b'

However, if the left hand evaluates as `False`, as is the case with an empty string, when the `or` is encountered, Python continues on and returns the right-hand side.

# empty string evaluates as False
'' or 'b'

Now, when return back to where this thinking started, we understand why the following evaluates as `True`.

'a' == ('a' or 'b')

If we wanted to determine whether 'a' was equal to both 'a' and 'b' (a clearly False statement), we would do the following:

'a' == 'a' and 'a' == 'b'

In the above example, we see that Python would evaluate the left-hand side of the expression (`'a' == 'a'`) as `True`, continuing on to the right-hand side of the `and`, evaluating the expression (`'a' == 'b'`) as False, and returning that.

## Identity Operators

 Identity operators are used to check if two variables are located on the same part of the memory. This is what it means to **compare identity**. If two variables are stored in the same part of memory, the are idenetical.

<div class="alert alert-success">
Python uses <code>is</code> and <code>is not</code> to compare <b>identity</b>. These operators return booleans.
</div>

Python uses the following **identity operators**:

- `is` : True if both refer to the same object in memory
- `is not` : True if they do not refer to the same object

Let's see what that means with an example. Below we create three variables: `a`, `b`, and `c`. They all store the same *value* (927), but are they identical?

a = 927
b = a
c = 927

Well, `a` and `b` are identical as determined here:

a is b

This is because `b` is an **alias** or a copy of `a`. Python stores this alias in the same part of memory to save space. (We'll discuss aliases more later.)

However, `c`, while storing the same *value* as `a` and `b` is *not* identical, as its values was defined independent of `a` and `b`

c is a

 It's important to udnerstand that two variables that are *equal* does **not** imply that they are *identical*.

Remember, if you want to test for *equality*, you would use the `==` operator:

# testing for value equality
a == b == c

### Delving Deeper: Identity Operators

With basic understanding of identity operators under our belt, let's dig a little deeper in our understanding of how Python defines variables.

We've noted before that a **new object** is created each time we have a variable that makes reference to it, but there are *few notable exceptions*:

- some simple strings
- Integers between -5 and 256 (inclusive)
- empty immutable containers (e.g. tuples) - we'll get to these later

While these may *seem* random, they exist for memory optimization in Python implementation. 

Shorter and less complex strings are **interned**. This means that they share the same space in memory, to maximize Python efficiency.

The rules behind this are a bit fuzzy and not important for beginner-level understanding, so we'll just go through a few examples here. But, if you want to read more about string interning and how Python handles this, you can read more [here](http://guilload.com/python-string-interning/).

Here, we define two variables. Following logic from above, you may expect these strings to *not* be identical. However, these are 'simple' strings in Python world. As such, they are in fact stored in the same place of memory (interned), and by definition, identical:

# define two variables
simple_string = 'string'
simple_string2 = 'string'

simple_string is simple_string2

To check where a variable is stored in memory, you can use the `id()` function. The variable of interest goes within the parentheses of the function. The two values returned are identical, so we know they're stored in the same place.

print(id(simple_string), id(simple_string2))

Alternatively, longer strings are not interned and are thus stored separately within Python's memory:

longer_string = 'really long string that just keeps going'
longer_string2 = 'really long string that just keeps going'

longer_string is longer_string2

print(id(longer_string), id(longer_string2))

Above, we see that these are *not* identical.

Like simple strings, integers between -5 and 256 *are* interned and thus are stored in the same place in Python's memory.

d = 5
e = 5

print(id(d), id(e))

print(d is e)

This is because Python implementation front loads an array of integers between -5 to 256. This means these objects *already exist*.

In this first example, the integer '5' and simple string 'Hello' are both interned or already available. Accordingly, `j` and `k` are identical and `l` and `m` are identical.

# Python doesn't create a new object here
j = 5
k = 5
l = 'Hello'
m = 'Hello'

true_variable_integer = j is k
true_variable_string = l is m

print(true_variable_integer, true_variable_string)

Conversely, here we have an integer greater than 256 and a complex string, due to the addition of an exclamation part. Here, `n` and `o` and `p` and `q` are *not* identical. Each of these values is held separately in memory.

# Python DOES create a new object here
n = 975 #greater than 256
o = 975
p = 'Hello!' #that exclamation point makes it more complex
q = 'Hello!'

false_variable_integer = n is o
false_variable_string = p is q

print(false_variable_integer, false_variable_string)

## Membership Operators

The final Python operator we'll introduce is the **membership operator**. These are used to check whether a value or variable is found in a sequence. These operators also return booleans.

<div class="alert alert-success">
Python uses <code>in</code> and <code>not in</code> to compare <b>membership</b>. These operators return booleans.
</div>

Here, we'll just be checking for value membership in strings. But, we'll discuss lists, tuples, sets, and dictionaries soon.

Python uses the following membership operators:

- `in` : True if value is found in the sequence
- `not in` : True if value is not found in the sequence

For these examples, we'll refer to the following variable (`my_string`)

my_string = 'I love Python!'

If you wanted to determine whether there was an `l` in `my_string`, you would use the membership operator `in`:

# check if l in my_string
'l' in my_string

As always, capitalization matters, so if you search for a capital L, the membership operator will return `False`:

'L' in my_string

Finally, note that a series of characters can be tested for membership:

'Python' in my_string

## String Concatenation

Now that we know all about strings and mathematics operators, it's important to note that sometimes operators behave differently on different types of variables. 

Above, we saw that for numbers (integers, floats, etc.), the `+` operator will add the two values together and return the sum.

For strings, however, this operator works to concatenate - meaning stick together - the two strings:

<div class="alert alert-success">
Operators sometimes do different things on different types of variables. For example, <code>+</code> on strings does concatenation.
</div>

Here, we see that the `+` operator concatenages the three strings together:

'a' + 'b' + 'c'

## Chaining Operators

It's also possible to combine long phrases of multiple types of operators. The same logic and rules apply, and you are able to combine operators into very long and complex expression. This isn't always the *best* idea as they can be hard to intepret; however, it is programmatically possible.

<div class="alert alert-success">
Operators and variables can also be chained together into arbitrarily complex expressions.
</div>

Here, this expression evaluates as `False`:

# Note that you can use parentheses to chunk sections
(13 % 7 >= 7) and ('Python' + ' ' + '3.7' == 'Python 3.7')

Given all we've learned so far about operators, we know that the left-hand side before the `and` is False, so the left-hand side is returned,

13 % 7 >= 7

regardless of the fact that the right-hand side of the expression is `True`:

'Python' + ' ' + '3.7' == 'Python 3.7'

## Exercies

Q1. **What would be the value stored in `my_value` after executing the following?**

```python
my_value = (3 + 2) + 2 / (16/2)
```

A) 0.218  
B) 0.875  
C) 5.25  
D) 40  
E) Produces an error  

Q2. **What would be the value stored in `remainder` after executing the following?**

```python
remainder = 16 % 5
```

A) 9  
B) 1  
C) 3  
D) 3.2  
E) Produces an error

Q3. **What would be the value stored in `modulo_time` after executing the following?**

```python
modulo_time = 4 * 2 % 5
```

A) 0  
B) 1  
C) 3  
D) 3.2  
E) Produces an error  

Q4. **What value is stored in `math_out` from the code below?**

```python
math_out = 32 / (1 + 3) ** 2 
```

Q5. **How would each of the following boolean expressions evaluate?**

```python
True and False
True and not True or False
True and not False
```

Q6. **Assume you're writing a videogame that will only slay the dragon if the magic lightsabre sword is charged to 90 or higher and has 100 or more energy units in its protective shield. Start with the code provided here. Replace `---` with values that will evaluate to `True` when the cell is run (and slay the dragon!).**

```python
sword_charge = ---
shield_energy = ---

(sword_charge ---) and (shield_energy ---)
```

Q7. **How would each of the following expressions evaluate?**

```python
'' and 'a'
'a' == ('' and 'a')
'a' == 'a' and 'a' == 'b' 
'a' == ('' and 'a')
```

Q8. **Using the variables provided, replace `---` with expression using identity operators such that `true_variable` will store `True` and `false_variable` will store `False`:

```python
a = 5
b = 5
c = b
d = 'Hello!'
e = 'Hello!'
f = 567
g = 567

true_variable = ---
false_variable = ---

print(true_variable, false_variable)
```

Q9. **What would be the value stored in `my_value` after executing the following?**

```python
my_value = (3+2)+2/(16/2)
```

A) 0.218    
B) 5.25  
C) 20  
D) 40  
E) Produces an error  


Q10. **How would each of the following expressions evaluate?**

```python
17 % 7
2**2 >= 4 and 13%3 > 1
```