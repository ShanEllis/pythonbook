# Lists

One of the most common ways to store multiple pieces of information is in a **list**. Lists store items in an ordered fashion. This means that there is a zeroth, first, second, third, and so on item in your list. Additionally, lists can store information of mixed type - so if you want to store strings with integers or floats with booleans, you can do so using a list.

Syntactically, lists are generated using square brackets around the items in your list, with each item separated by a comma.

<div class="alert alert-success">
A list is a mutable collection of ordered items, that can be of mixed type. Lists are created using square brackets.
</div>

## Defining a list

To define a list, we will assign the information back to a variable (`my_list`) using the assignment operator (`=`), as we do for all variables. To the right of the assignment operator, the list is created using square brackets around the list items. Each item in the list is separated by a comma.

In this first list, we have three items - an integer (`1`), a string (`a`), and a boolean (`True`).

# Define a list
my_list = [1, 'a', True]

As we've seen previously, to inspect the items in a list, `print()` statements can be helpful. This reminds you what information is stored in a variable.

# Print out the contents of a list
print(my_list)

Similarly, `type()`, when provided with a list as its input, will return `list`.

# Check the type of a list
type(my_list)

To add to these common functions, we'll introduce `len()` which returns the number of items (elements) in the list specified within the parentheses:

# Get the length of the list, and print it out
len(my_list)

## Indexing

As we store more items (piecies of information) in a variable, we need a way to get specific pieces of information back out of that list. To obtain a specific item or specific set of items from a list, we will use the process of **indexing**.

<div class="alert alert-success">
Indexing refers to selecting an item from within a collection. Indexing is done with square brackets.
</div>

For example, what if we had a class with 5 students in it. We could store their first names in a list called `students`:

# Define a list 
students = ['Julian', 'Amal', 'Richard', 'Juan', 'Xuan']

If we wanted to know who the first student in our list was, we could **index** that value from the list. 

To do so, we would use square brackets after the variable name and specify the position from the list that we want to index. If we want the first item in the list, we'll use the number '0'. This is because Python is zero-based. This means that counting starts with 0. The second item in the list could be accessed with the number '1'.

Thus, to return the first student in the list ('Julian'), we would index `students[0]`:

# Indexing: Count forward, starting at 0, with positive numbers
print(students[0])

Similarly, if we wanted the second student in the list, we would index with `students[1]`:

# Indexing second student in list
print(students[1])

### Negative Indexing

**Negative indexing** is also possible - you *can* count backward from the end of the list. In this case '-1' refers to the last item in the list and indexing counts from there. So, the second to last item in the list would be '-2'.

Thus, to return the last student in the list, we would use `students[-1]`:

# Indexing: Count backward, starting at -1, with negative numbers
print(students[-1])

### Slicing

It is also possible to obtain a portion or subset of the list, referred to as a **slice**. 

The syntax to obtain a slice of the list requires that you specify at what index (position) you want the slice to return and when the slice should stop using `[start:stop]`. Importantly, the `start` position is included in the output, but the `stop` position specified is *not* returned. Each item *up until* to `stop` position is returned.

To return the third and fourth position in the list, you would then use `students[2:4]` as this would return the item in the '2' position and the '3' position, but would not include the '4' position, as the `stop` is not included in the output.

# Indexing: Grab a group of adjacent items using `start:stop`, called a slice
print(students[2:4])

For slicing, you often want to take a slice of the list starting with a certain position and continuing on until the end of the list. This can be accomplished by not specifying a stop position, using the syntax `[start:]`:

# indexing from third position to end of list
print(students[2:])

Similarly, to index from the beginning of the list until a stop position, you would exclude a start position and use `[:stop]`:

# Indexing from beginning of list
print(students[:4])

Note above that again, the stop position is *not* included in the slice that is output.

Finally, it is also possible to obtain a slice using a specific pattern by specifying the `step` of the slice using `[start:stop:step]`. The default step is '1', returning each item in the slice. However, if the `step` is '2', the slice will include and return every other item in your list. If the `step` is 3, it will return every third item, and so on.

Here, we `start` at 0 (the beginning of the list), `stop` at (and don't include) the 4th index and `step` to include every second student in the list:

# slicing by skipping a value [start:stop:step]
print(students[0:4:2])

### Summary: Indexing

- Python is zero-based (The first index is '0')
- Negative indices index backwards through a collection
- A sequence of indices (called a slice) can be accessed using `start:stop`
    - In this contstruction, `start` is included then every element until `stop`, not including `stop` itself
    - To skip values in a sequence use `start:stop:step`

## Operators with lists

We previously introduced the **membership** operator, `in`. These operators work to identify whether a specific item exists in the specified list, returning the boolean `True` if it is a member of the list and `False` if it is not.

<div class="alert alert-success">
The <code>in</code> operator asks whether an element is present inside a collection, and returns a boolean answer. 
</div>

# Define a new list to work with
list_again = [True, 13, None, 'apples']

For example, 'Julian' is a student in our list of students, so the following returns `True`:

# returns True if element in list
'Julian' in students

When asked about a name that is *not* in our list of students, the `in` membership operator will return `False`.

# Check if a particular element is present in the list of students
'Shannon' in students

Of importance, it is searching for the entire element, so if we searched for 'Jul', which is part of the name Julian but not the whole name, the membership operator would accurately specify that 'Jul' is *not* and element in the list.

# Jul is not an element in list
'Jul' in students

As specified in an earlier chapter, the `not` operator can be combined with membership operators to evaluate the expression. For example, Shannon is `not in` the `students` list, so the following will return `True`, as this expression evaluates as `True`:

# The `in` operator can be combined with the `not` operator
'Shannon' not in students

## Mutating

Beyond slicing to obtain a portion of the list, it's important to know that lists are *mutable*. This means that the elements of the list can be changed after the list is created. Updating or changing the contents of a list is referred to **mutating** the contents of the list.

<div class="alert alert-success">
Lists are mutable, meaning after definition, you can update and change things about the list.
</div>

Here we create a list `udpates` which stores three integer values:

# Define a list
updates = [29, 2, 3]

# Check the contents of the list
print(updates)

We can then mutate (change) an element of the list by assigning a new value to a specific indexed position in the list. 

Here, we assign the value '1' to the zeroth position in the list `updates`:

# Redefine a particular element of the list
updates[0] = 1

# Check the contents of the list
print(updates)

## Exercises

Q1. **Which of the following specifies a list of 4 items?**

A) `item_A = [0, 'string', 18]`  
B) `item_B = (0, 'string', 18, 'name')`  
C) `item_C = [0, 'string', 18, 'name']`  
D) `item_D = (0, 'string', 18)`  
E) `item_E = [1234]`  

Q2. **What will be the output of the following piece of code:**

```python
q2_lst = ['a', 'b', 'c','d']
q2_lst[-3:-1]
```

A) ['a', 'b', 'c']  
B) ['c', 'b', 'a']  
C) ['c', 'b']  
D) ['b', 'c', 'd']  
E) ['b', 'c']  

Q3. **Given the following list, what would be the appropriate line of code to return `['butter', '&', 'jelly']`?**

```python
q3_lst = ['peanut', 'butter', '&','jelly']
```

A) `q3_lst[2:4]`  
B) `q3_lst[1:3]`  
C) `q3_lst[:-2]`  
D) `q3_lst[-3:]`  
E) `q3_lst[1:4:2]`  

Q4. **Given the following list `practice_lst = [1, True, 'alpha', 13, 'cogs18']`, what would be returned from each of the following lines of code if executed?**


```python
13 in practice_lst
False in practice_lst
'True' in practice_lst
'cogs' in practice_lst
'cogs18' in practice_lst
```

Q5. **After executing the following lines of code, what will be the value of output?**

```python
ex2_lst = [0, False, 'ten', None]

bool_1 = False in ex2_lst
bool_2 = 10 not in ex2_lst

output = bool_1 and bool_2
```

Q6. **What would the following two lines of code accomplish?**

```python
lst_update = [1, 2, 3, 0, 5]
lst_update[3] = 4 
```

A) replace 0 with 4 in `lst_update`    
B) replace 4 with 0 in `lst_update`  
C) no change to `lst_update`  
D) produces an error  

Q7. **What will be the value of `counter` after this code is run?**

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