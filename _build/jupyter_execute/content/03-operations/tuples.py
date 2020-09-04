# Tuples 

Lists are not the only variable type that can store a collection of multiple elements. Like lists, **tuples** store elements of mixed type in an ordered manner. However, tuples are *immutable*. Once created, their contents can not be mutated or changed. Syntactically, tuples are specified with *parentheses* around the elements of the tuple. Separate elements in the tuple are separated using commas, as we saw previously.

<div class="alert alert-success">
A tuple is an <b>immutable</b> collection of ordered items, that can be of mixed type. Tuples are created using parentheses.
</div>

## Defining a tuple

Here, rather than square brackets which are used to create lists, we use parentheses around the elements of our tuple: `my_tuple`.

# Define a tuple
my_tuple = (2, 'b', False)

While tuples are immutable and thus do not allow for mutating, the rest of the principles that applied to lists also apply to tuples. 

For example, we can pring the contents of a tuple:

# Print out the contents of a tuple
print(my_tuple)

We can determine the `type()`, which, for tuples returns 'tuple':

# Check the type of a tuple
type(my_tuple)

We can index to return specific elements or slices of a tuple:

# Index into a tuple
my_tuple[0]

And finally, we can return the number of elements in the tuple using `len()`:

# Get the length of a tuple
len(my_tuple)

## Tuples are Immutable

Tuples defining feature from lists is that they are immutable. If you try to change a value of a particular element of your list, you will receive a `TypeError`, as tuples do not allow for mutating.

# Tuples are immutable - meaning after they defined, you can't change them
# This code will produce an error.
tup[2] = 1

## Aliases

Now that we've discussed lists and tuples, we can discuss the topic of **aliases**.

Python allows you to make a new variable that refers to a variable you've already defined. 

### Aliases: immutable types

For example, here we create the variable `a`, which stores the value '1'.

We then make an *alias* `b` of the variable `a`. When we look at the contents of `b`, we see that it stores the same information as the original variable `a`.

# Make a variable, and an alias
a = 1
b = a
print(b)

But, what happens if we change the value of the original variable (`a`) - what happens to `b`?

# Make a variable & an alias
# change value of original variable
a = 1
b = a
a = 2

print(a)
print(b)

In this example, we see that when we change the value stored in `a`, the value stored in the alias `b` remains unchanged.

This is because integers are an **immutable** variable type.

### Aliases: mutable types

On the other hand, what happens if we make an alias of a **mutable** variable type, like a list?

Here we create `first_list` and then make an alias called `alias_list`.

We see that the contents of `alias_list` are the same as the contents assigned to `first_list`:

first_list = [1, 2, 3, 4]
alias_list = first_list
alias_list

Now, if we change the second value of the original list `first_list` and take a look at that variable's contents, we see that, the second value has been mutated.

#change second value of first_list
first_list[1] = 29
first_list

But, what about the alias list `alias_list`?

Here, the alias has been updated as well. Unlike for immutable variable types, when you make a change to (mutate) a *mutable* variable type, the alias changes as well. 

# check alias_list
alias_list

### Why allow aliasing? 

Aliasing can get confusing and be difficult to track, so why does Python allow it?

Well, it's more efficient to point to an alias than to make an entirely new copy of a a very large variable storing a lot of data. 

Python allows for the confusion, in favor of being more efficient.

## Strings as Collections

While we're talking about lists and tuples here as collections that store multiple elements in an ordered fashion, it's important to keep in mind that strings are also collections. Strings just happen to store multiple characters in a string, rather than multiple elements. As discussed before, strings are *immutable*.

<div class="alert alert-success">
Strings act similarly to ordered collections of homogenous elements - specifically characters. But, they are <b>immutable</b>.
</div>

As they are collections, the operations we've used for lists and tuples also apply to lists:

# Define a string
my_string = 'TheFamousFive'

Strings can be indexed. The zeroth inex refers to the first character in the string.

So here, `my_string[2]` returns  the third position in the string `my_string` defined above:

# Index into a string
my_string[2]

We can use membership operators to determine if a string of characters is found within the collection:

# Ask if an item is in a string
'Fam' in my_string

We can determine the number of characters in the string using `len()`.

# Check the length of a string
len(my_string)

*But*, like tuples, because strings are also *immutable*, we can not mutate a slice of the string.

# Index into a string
# This code will produce an error
my_str[1:3] = 'HE'

## Exercises

Q1. **Which of the following specifies a tuple of 4 items?**

A) `item_A = [0, 'string', 18]`  
B) `item_B = (0, 'string', 18, 'name')`  
C) `item_C = [0, 'string', 18, 'name']`  
D) `item_D = (0, 'string', 18)`  
E) `item_E = [1234]`  

Q2. **What will print out after executing the following code?**

```python
lst = ['a', 'b', 'c']
tup = ('b', 'c', 'd')

if lst[-1] == tup[-1]:
    print('EndMatch')
elif tup[1] in lst:
    print('Overlap')
elif len(lst) == tup:
    print('Length')
else:
    print('None')
```

A) EndMatch   
B) Overlap   
C) Length   
D) Overlap & Match   
E) None