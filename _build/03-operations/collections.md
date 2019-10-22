---
interact_link: content/03-operations/collections.ipynb
kernel_name: python3
title: 'Collections'
prev_page:
  url: /03-operations/collections_loops
  title: 'Collections & Loops'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Collections

To this point we have discussed a number of different types of variables (strings, integers, floats, booleans, NoneType); however, each of these variables can only store one piece of information - a single string, a single integer, etc. If you want to store a **collection** of pieices of information - say, the heights of everyone in your family - you'll need a different type of variable.

In this chapter, we'll introduce three such variable types: **lists**, **tuples**, and **dictionaries**.

## Lists

One of the most common ways to store multiple pieces of information is in a **list**. Lists store items in an ordered fashion. This means that there is a zeroth, first, second, third, and so on item in your list. Additionally, lists can store information of mixed type - so if you want to store strings with integers or floats with booleans, you can do so using a list.

Syntactically, lists are generated using square brackets around the items in your list, with each item separated by a comma.

<div class="alert alert-success">
A list is a mutable collection of ordered items, that can be of mixed type. Lists are created using square brackets.
</div>

### Defining a list

To define a list, we will assign the information back to a variable (`my_list`) using the assignment operator (`=`), as we do for all variables. To the right of the assignment operator, the list is created using square brackets around the list items. Each item in the list is separated by a comma.

In this first list, we have three items - an integer (`1`), a string (`a`), and a boolean (`True`).



{:.input_area}
```python
# Define a list
my_list = [1, 'a', True]
```


As we've seen previously, to inspect the items in a list, `print()` statements can be helpful. This reminds you what information is stored in a variable.



{:.input_area}
```python
# Print out the contents of a list
print(my_list)
```


{:.output .output_stream}
```
[1, 'a', True]

```

Similarly, `type()`, when provided with a list as its input, will return `list`.



{:.input_area}
```python
# Check the type of a list
type(my_list)
```





{:.output .output_data_text}
```
list
```



To add to these common functions, we'll introduce `len()` which returns the number of items (elements) in the list specified within the parentheses:



{:.input_area}
```python
# Get the length of the list, and print it out
len(my_list)
```





{:.output .output_data_text}
```
3
```



### Indexing

As we store more items (piecies of information) in a variable, we need a way to get specific pieces of information back out of that list. To obtain a specific item or specific set of items from a list, we will use the process of **indexing**.

<div class="alert alert-success">
Indexing refers to selecting an item from within a collection. Indexing is done with square brackets.
</div>

For example, what if we had a class with 5 students in it. We could store their first names in a list called `students`:



{:.input_area}
```python
# Define a list 
students = ['Julian', 'Amal', 'Richard', 'Juan', 'Xuan']
```


If we wanted to know who the first student in our list was, we could **index** that value from the list. 

To do so, we would use square brackets after the variable name and specify the position from the list that we want to index. If we want the first item in the list, we'll use the number '0'. This is because Python is zero-based. This means that counting starts with 0. The second item in the list could be accessed with the number '1'.

Thus, to return the first student in the list ('Julian'), we would index `students[0]`:



{:.input_area}
```python
# Indexing: Count forward, starting at 0, with positive numbers
print(students[0])
```


{:.output .output_stream}
```
Julian

```

Similarly, if we wanted the second student in the list, we would index with `students[1]`:



{:.input_area}
```python
# Indexing second student in list
print(students[1])
```


{:.output .output_stream}
```
Amal

```

#### Negative Indexing

**Negative indexing** is also possible - you *can* count backward from the end of the list. In this case '-1' refers to the last item in the list and indexing counts from there. So, the second to last item in the list would be '-2'.

Thus, to return the last student in the list, we would use `students[-1]`:



{:.input_area}
```python
# Indexing: Count backward, starting at -1, with negative numbers
print(students[-1])
```


{:.output .output_stream}
```
Xuan

```

#### Slicing

It is also possible to obtain a portion or subset of the list, referred to as a **slice**. 

The syntax to obtain a slice of the list requires that you specify at what index (position) you want the slice to return and when the slice should stop using `[start:stop]`. Importantly, the `start` position is included in the output, but the `stop` position specified is *not* returned. Each item *up until* to `stop` position is returned.

To return the third and fourth position in the list, you would then use `students[2:4]` as this would return the item in the '2' position and the '3' position, but would not include the '4' position, as the `stop` is not included in the output.



{:.input_area}
```python
# Indexing: Grab a group of adjacent items using `start:stop`, called a slice
print(students[2:4])
```


{:.output .output_stream}
```
['Richard', 'Juan']

```

For slicing, you often want to take a slice of the list starting with a certain position and continuing on until the end of the list. This can be accomplished by not specifying a stop position, using the syntax `[start:]`:



{:.input_area}
```python
# indexing from third position to end of list
print(students[2:])
```


{:.output .output_stream}
```
['Richard', 'Juan', 'Xuan']

```

Similarly, to index from the beginning of the list until a stop position, you would exclude a start position and use `[:stop]`:



{:.input_area}
```python
# Indexing from beginning of list
print(students[:4])
```


{:.output .output_stream}
```
['Julian', 'Amal', 'Richard', 'Juan']

```

Note above that again, the stop position is *not* included in the slice that is output.

Finally, it is also possible to obtain a slice using a specific pattern by specifying the `step` of the slice using `[start:stop:step]`. The default step is '1', returning each item in the slice. However, if the `step` is '2', the slice will include and return every other item in your list. If the `step` is 3, it will return every third item, and so on.

Here, we `start` at 0 (the beginning of the list), `stop` at (and don't include) the 4th index and `step` to include every second student in the list:



{:.input_area}
```python
# slicing by skipping a value [start:stop:step]
print(students[0:4:2])
```


{:.output .output_stream}
```
['Julian', 'Richard']

```

#### Summary: Indexing

- Python is zero-based (The first index is '0')
- Negative indices index backwards through a collection
- A sequence of indices (called a slice) can be accessed using `start:stop`
    - In this contstruction, `start` is included then every element until `stop`, not including `stop` itself
    - To skip values in a sequence use `start:stop:step`

### Operators with lists

We previously introduced the **membership** operator, `in`. These operators work to identify whether a specific item exists in the specified list, returning the boolean `True` if it is a member of the list and `False` if it is not.

<div class="alert alert-success">
The <code>in</code> operator asks whether an element is present inside a collection, and returns a boolean answer. 
</div>



{:.input_area}
```python
# Define a new list to work with
list_again = [True, 13, None, 'apples']
```


For example, 'Julian' is a student in our list of students, so the following returns `True`:



{:.input_area}
```python
# returns True if element in list
'Julian' in students
```





{:.output .output_data_text}
```
True
```



When asked about a name that is *not* in our list of students, the `in` membership operator will return `False`.



{:.input_area}
```python
# Check if a particular element is present in the list of students
'Shannon' in students
```





{:.output .output_data_text}
```
False
```



Of importance, it is searching for the entire element, so if we searched for 'Jul', which is part of the name Julian but not the whole name, the membership operator would accurately specify that 'Jul' is *not* and element in the list.



{:.input_area}
```python
# Jul is not an element in list
'Jul' in students
```





{:.output .output_data_text}
```
False
```



As specified in an earlier chapter, the `not` operator can be combined with membership operators to evaluate the expression. For example, Shannon is `not in` the `students` list, so the following will return `True`, as this expression evaluates as `True`:



{:.input_area}
```python
# The `in` operator can be combined with the `not` operator
'Shannon' not in students
```





{:.output .output_data_text}
```
True
```



### Mutating

Beyond slicing to obtain a portion of the list, it's important to know that lists are *mutable*. This means that the elements of the list can be changed after the list is created. Updating or changing the contents of a list is referred to **mutating** the contents of the list.

<div class="alert alert-success">
Lists are mutable, meaning after definition, you can update and change things about the list.
</div>

Here we create a list `udpates` which stores three integer values:



{:.input_area}
```python
# Define a list
updates = [29, 2, 3]
```




{:.input_area}
```python
# Check the contents of the list
print(updates)
```


{:.output .output_stream}
```
[29, 2, 3]

```

We can then mutate (change) an element of the list by assigning a new value to a specific indexed position in the list. 

Here, we assign the value '1' to the zeroth position in the list `updates`:



{:.input_area}
```python
# Redefine a particular element of the list
updates[0] = 1
```




{:.input_area}
```python
# Check the contents of the list
print(updates)
```


{:.output .output_stream}
```
[1, 2, 3]

```

## Tuples

Lists are not hte only variable type that can store a collection of multiple elements. Like lists, **tuples** store elements of mixed type in an ordered manner. However, tuples are *immutable*. Once created, their contents can not be mutated or changed. Syntactically, tuples are specified with *parentheses* around the elements of the tuple. Separate elements in the tuple are separated using commas, as we saw previously.

<div class="alert alert-success">
A tuple is an <b>immutable</b> collection of ordered items, that can be of mixed type. Tuples are created using parentheses.
</div>

### Defining a tuple

Here, rather than square brackets which are used to create lists, we use parentheses around the elements of our tuple: `my_tuple`.



{:.input_area}
```python
# Define a tuple
my_tuple = (2, 'b', False)
```


While tuples are immutable and thus do not allow for mutating, the rest of the principles that applied to lists also apply to tuples. 

For example, we can pring the contents of a tuple:



{:.input_area}
```python
# Print out the contents of a tuple
print(my_tuple)
```


{:.output .output_stream}
```
(2, 'b', False)

```

We can determine the `type()`, which, for tuples returns 'tuple':



{:.input_area}
```python
# Check the type of a tuple
type(my_tuple)
```





{:.output .output_data_text}
```
tuple
```



We can index to return specific elements or slices of a tuple:



{:.input_area}
```python
# Index into a tuple
my_tuple[0]
```





{:.output .output_data_text}
```
2
```



And finally, we can return the number of elements in the tuple using `len()`:



{:.input_area}
```python
# Get the length of a tuple
len(my_tuple)
```





{:.output .output_data_text}
```
3
```



### Tuples are Immutable

Tuples defining feature from lists is that they are immutable. If you try to change a value of a particular element of your list, you will receive a `TypeError`, as tuples do not allow for mutating.



{:.input_area}
```python
# Tuples are immutable - meaning after they defined, you can't change them
# This code will produce an error.
tup[2] = 1
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-47-6b0fd3f24bc7> in <module>()
          1 # Tuples are immutable - meaning after they defined, you can't change them
          2 # This code will produce an error.
    ----> 3 tup[2] = 1
    

    TypeError: 'tuple' object does not support item assignment


```

## Aliases

Now that we've discussed lists and tuples, we can discuss the topic of **aliases**.

Python allows you to make a new variable that refers to a variable you've already defined. 

### Aliases: immutable types

For example, here we create the variable `a`, which stores the value '1'.

We then make an *alias* `b` of the variable `a`. When we look at the contents of `b`, we see that it stores the same information as the original variable `a`.



{:.input_area}
```python
# Make a variable, and an alias
a = 1
b = a
print(b)
```


{:.output .output_stream}
```
1

```

But, what happens if we change the value of the original variable (`a`) - what happens to `b`?



{:.input_area}
```python
# Make a variable & an alias
# change value of original variable
a = 1
b = a
a = 2

print(a)
print(b)
```


{:.output .output_stream}
```
2
1

```

In this example, we see that when we change the value stored in `a`, the value stored in the alias `b` remains unchanged.

This is because integers are an **immutable** variable type.

### Aliases: mutable types

On the other hand, what happens if we make an alias of a **mutable** variable type, like a list?

Here we create `first_list` and then make an alias called `alias_list`.

We see that the contents of `alias_list` are the same as the contents assigned to `first_list`:



{:.input_area}
```python
first_list = [1, 2, 3, 4]
alias_list = first_list
alias_list
```





{:.output .output_data_text}
```
[1, 2, 3, 4]
```



Now, if we change the second value of the original list `first_list` and take a look at that variable's contents, we see that, the second value has been mutated.



{:.input_area}
```python
#change second value of first_list
first_list[1] = 29
first_list
```





{:.output .output_data_text}
```
[1, 29, 3, 4]
```



But, what about the alias list `alias_list`?

Here, the alias has been updated as well. Unlike for immutable variable types, when you make a change to (mutate) a *mutable* variable type, the alias changes as well. 



{:.input_area}
```python
# check alias_list
alias_list
```





{:.output .output_data_text}
```
[1, 29, 3, 4]
```



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



{:.input_area}
```python
# Define a string
my_string = 'TheFamousFive'
```


Strings can be indexed. The zeroth inex refers to the first character in the string.

So here, `my_string[2]` returns  the third position in the string `my_string` defined above:



{:.input_area}
```python
# Index into a string
my_string[2]
```





{:.output .output_data_text}
```
'e'
```



We can use membership operators to determine if a string of characters is found within the collection:



{:.input_area}
```python
# Ask if an item is in a string
'Fam' in my_string
```





{:.output .output_data_text}
```
True
```



We can determine the number of characters in the string using `len()`.



{:.input_area}
```python
# Check the length of a string
len(my_string)
```





{:.output .output_data_text}
```
13
```



*But*, like tuples, because strings are also *immutable*, we can not mutate a slice of the string.



{:.input_area}
```python
# Index into a string
# This code will produce an error
my_str[1:3] = 'HE'
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-21-9139cc40aa38> in <module>()
          1 # Index into a string
          2 # This code will produce an error
    ----> 3 my_str[1:3] = 'HE'
    

    NameError: name 'my_str' is not defined


```

## Dictionaries

The third and final new type of variable we'll introduce here is the **dictionary**. Like dictionaries where you look up words and are provided with a definition of that word, Python dictionaries store two pieces of information. These two pieces are referred to as the **key** and its **value**. Dictionaries are a collection of **key-value pairs**.

<div class="alert alert-success">
A <b>dictionary</b> is mutable collection of items, that can be of mixed-type, that are stored as key-value pairs.
</div>

### Defining a dictionary

Specifically, dictionaries are defined using curly brackets `{}`. Within the curly brackets are key-value pairs. Each key-value pair is created using a colon (`:`) between the key and its value. And, separate key-value pairs are stored by separating each key-value pair, using a comma (`,`).

Here we create `my_dictionary` which stores two key-value pairs.



{:.input_area}
```python
# Create a dictionary
my_dictionary = {'key_1' : 'value_1', 'key_2' : 'value_2'}
```


All of our now-familiar operations that we use for lists and tuples are also helpful when operating on dictionaries.

For example, we can use `print()` to retrieve the contents of the dictionary:



{:.input_area}
```python
# Check the contents of the dictionary
print(my_dictionary)
```


{:.output .output_stream}
```
{'key_1': 'value_1', 'key_2': 'value_2'}

```

We can use `type()` to return the variable type. Note that dictionaries return 'dict' as their variable type:



{:.input_area}
```python
# Check the type of the dictionary
type(my_dictionary)
```





{:.output .output_data_text}
```
dict
```



And, we can use `len()` to return the number of key-value pairs stored in a given dictionary:



{:.input_area}
```python
# Dictionaries also have a length
# length refers to how many pairs there are
len(my_dictionary)
```





{:.output .output_data_text}
```
2
```



### Indexing: dictionaries

As with lists and tuples, indexing occurs using square brackets `[]`. However, dictionaries are unique in that they are indexed by their keys. When a specific *key* is indexed, the *value* stored in that key is returned.

For example, if we index to specify we want information from 'key_1', note that 'value_1' is returned. This is because we index *by* keys to return the *values* stored in those keys:



{:.input_area}
```python
# Dictionaries are indexed using their keys
dictionary['key_1']
```





{:.output .output_data_text}
```
'value_1'
```



### Uses: dictionaries

Dictionaries are particularly helpful when you want to store related pieces of information. For example, if you had a list of names and their respecititve emails, you would want to store these two pieces of information in such a way that you knew which email addresses were related to which individuals. A dictionary is perfect for this! The names of the individuals therefore become the keys and their respective emails the values:



{:.input_area}
```python
student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : 'ada@analyticengine.com',
    'Alan Turing' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}

student_emails
```





{:.output .output_data_text}
```
{'Ada Lovelace': 'ada@analyticengine.com',
 'Alan Turing': 'aturing@thebomb.gov',
 'Betty Jennings': 'bjennings@eniac.org',
 'Grace Hopper': 'ghopper@navy.usa'}
```



Dictionaries, like lists, are *mutable*. This means that dictionaries, once created, values *can* be updated.

For example, if you wanted to store information about students' attendance for a particular lab, you could store `True` for all students who attended and `False` for all who failed to attend.



{:.input_area}
```python
# remember what dictionary we created above
lab_attendance = {
    'A1234' : True,
    'A5678' : False,
    'A9123' : True
}

lab_attendance
```





{:.output .output_data_text}
```
{'A1234': True, 'A5678': False, 'A9123': True}
```



If later on you were made aware that the student with the ID 'A5678' did in fact attend lab, you could update the value stored for that key.

This occurs as we've seen with other types of collections. The key is index and the value for that key is then assigned to the indexed value. The distiction here is that the *value* for the specified key is updated, and not the key itself.



{:.input_area}
```python
# change value of specified key
lab_attendance['A5678'] = True
lab_attendance
```





{:.output .output_data_text}
```
{'A1234': True, 'A5678': True, 'A9123': True}
```



With this change, all three keys now store the value `True`.

### Key Deletion

Because dictionaries are mutable, key-value pairs can also be removed from the dictionary using `del`.

In our example above, if student 'A5678' dropped the course, they could be dropped from the dictionary as well. The resulting dictionary now has only two key-value pairs.



{:.input_area}
```python
print(lab_attendance)
len(lab_attendance)
```




{:.input_area}
```python
## remove key-value pair using del
del lab_attendance['A5678']

print(lab_attendance)
len(lab_attendance)
```


{:.output .output_stream}
```
{'A1234': True, 'A9123': True}

```




{:.output .output_data_text}
```
2
```



### Operators: dictionaries

The operators we've discussed previously can be used when working with dictionaries.

To determine if a specified *key* is present in a dictionary we can again use the `in` operator:



{:.input_area}
```python
if 'A1234' in lab_attendance:
  print('Yes, that student is in this class')
```


{:.output .output_stream}
```
Yes, that student is in this class

```

### Dictionary Properties

When storing key-value pairs in dictionaries, there are a number of additional rules and properties that are important to understand to effectively use dictionaries:

**Property #1**
- Only one value per key. No duplicate keys allowed. 
    - If duplicate keys specified during assignment, the last assignment wins.

In this example here, there are three key-value pairs specified in the creation of the dictionary; however, only the last key-value pair is stored:



{:.input_area}
```python
# Last duplicate key assigned wins
{'Student' : 97, 'Student': 88, 'Student' : 91}
```





{:.output .output_data_text}
```
{'Student': 91}
```



**Property #2**
- **keys** must be of an immutable type (string, tuple, integer, float, etc)
- Note: **values** can be of any type

Here, this code produces an error, as the dictionary attempts to use a *mutable* type for the dictionary's key:



{:.input_area}
```python
# lists are not allowed as key types
# this code will produce an error
{['Student'] : 97}
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-26-27b11708f095> in <module>()
          1 # lists are not allowed as key types
          2 # this code will produce an error
    ----> 3 {['Student'] : 97}
    

    TypeError: unhashable type: 'list'


```

**Property #3**
- Dictionary keys are case sensitive.

As with everything when it comes to code, capital and lowercase letters are distinct characters. Thus, case sensitivity matters. The key 'Student' and the key 'STUDENTS' are two distinct keys and will be treated as such in dictionary generation.



{:.input_area}
```python
{'Student' : 97, 'student': 88, 'STUDENT' : 91}
```





{:.output .output_data_text}
```
{'STUDENT': 91, 'Student': 97, 'student': 88}
```



## Exercises

1. **Which of the following specifies a list of 4 items?**

A) `item_A = [0, 'string', 18]`  
B) `item_B = (0, 'string', 18, 'name')`  
C) `item_C = [0, 'string', 18, 'name']`  
D) `item_D = (0, 'string', 18)`  
E) `item_E = [1234]`  

2. **What will be the output of the following piece of code:**

```python
q2_lst = ['a', 'b', 'c','d']
q2_lst[-3:-1]
```

A) ['a', 'b', 'c']  
B) ['c', 'b', 'a']  
C) ['c', 'b']  
D) ['b', 'c', 'd']  
E) ['b', 'c']  

3. **Given the following list, what would be the appropriate line of code to return `['butter', '&', 'jelly']`?**

```python
q3_lst = ['peanut', 'butter', '&','jelly']
```

A) `q3_lst[2:4]`  
B) `q3_lst[1:3]`  
C) `q3_lst[:-2]`  
D) `q3_lst[-3:]`  
E) `q3_lst[1:4:2]`  

4. **Given the following list `practice_lst = [1, True, 'alpha', 13, 'cogs18']`, what would be returned from each of the following lines of code if executed?**


```python
13 in practice_lst
False in practice_lst
'True' in practice_lst
'cogs' in practice_lst
'cogs18' in practice_lst
```

5. **After executing the following lines of code, what will be the value of output?**

```python
ex2_lst = [0, False, 'ten', None]

bool_1 = False in ex2_lst
bool_2 = 10 not in ex2_lst

output = bool_1 and bool_2
```

6. **What would the following two lines of code accomplish?**

```python
lst_update = [1, 2, 3, 0, 5]
lst_update[3] = 4 
```

A) replace 0 with 4 in `lst_update`    
B) replace 4 with 0 in `lst_update`  
C) no change to `lst_update`  
D) produces an error  

7. **Which of the following specifies a tuple of 4 items?**

A) `item_A = [0, 'string', 18]`  
B) `item_B = (0, 'string', 18, 'name')`  
C) `item_C = [0, 'string', 18, 'name']`  
D) `item_D = (0, 'string', 18)`  
E) `item_E = [1234]`  

8. **What will print out after executing the following code?**

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

9. **What will be the value of `counter` after this code is run?**

```python
things_that_are_good = ['python', 'data', 'science', 'tacos']

counter = 0

if 'python' in things_that_are_good:
    counter = counter + 1

if len(things_that_are_good) == 4:
    counter = counter + 1
    
if things_that_are_good[2] == 'data':
    counter = counter + 1 
    
print(counter)
```

10. **Which of the following would create a dictionary of length 3?**

A) `{'Student_1' : 97, 'Student_2'}`  
B) `{'Student_1', 'Student_2', 'Student_3'}`  
C) `['Student_1' : 97, 'Student_2': 88, 'Student_3' : 91]`  
D) `{'Student_1' : 97, 'Student_2': 88, 'Student_3' : 91}`  
E) `('Student_1' : 97, 'Student_2': 88, 'Student_3' : 91)`  

11. **Fill in the '---' in the code below to return the value stored in the second key.**

```python
height_dict = {'height_1' : 60, 'height_2': 68, 'height_3' : 65, 'height_4' : 72}
height_dict[---]
```

12. **Write the code that would create a dictionary `car` that stores values about your dream car's `make`, `model`, and `year`.**

13. **What would the value of `result` be after this code has executed?**

```python
dictionary = {'alpha' : [8, 12], 
              'beta'  : [13, 30], 
              'theta' : [4, 8]}

check = 10

for item in dictionary:
    temp = dictionary[item]
    if temp[0] <= check <= temp[1]:
        result = item
```

14. **Why does the following code produce an error?**

```python
student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : ['ada@analyticengine.com'],
    'Ada Lovelace' : 'aturing@thebomb.gov',
    ['Grace Hopper'] : 'ghopper@navy.usa'
}
```

A) duplicate keys  
B) mutable key specified  
C) keys are case sensitive   
D) mutable value specified   

