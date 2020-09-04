# Dictionaries 
The third and final new type of variable we'll introduce here is the **dictionary**. Like dictionaries where you look up words and are provided with a definition of that word, Python dictionaries store two pieces of information. These two pieces are referred to as the **key** and its **value**. Dictionaries are a collection of **key-value pairs**.

<div class="alert alert-success">
A <b>dictionary</b> is mutable collection of items, that can be of mixed-type, that are stored as key-value pairs.
</div>

## Defining a dictionary

Specifically, dictionaries are defined using curly brackets `{}`. Within the curly brackets are key-value pairs. Each key-value pair is created using a colon (`:`) between the key and its value. And, separate key-value pairs are stored by separating each key-value pair, using a comma (`,`).

Here we create `my_dictionary` which stores two key-value pairs.

# Create a dictionary
my_dictionary = {'key_1' : 'value_1', 'key_2' : 'value_2'}

All of our now-familiar operations that we use for lists and tuples are also helpful when operating on dictionaries.

For example, we can use `print()` to retrieve the contents of the dictionary:

# Check the contents of the dictionary
print(my_dictionary)

We can use `type()` to return the variable type. Note that dictionaries return 'dict' as their variable type:

# Check the type of the dictionary
type(my_dictionary)

And, we can use `len()` to return the number of key-value pairs stored in a given dictionary:

# Dictionaries also have a length
# length refers to how many pairs there are
len(my_dictionary)

## Indexing: dictionaries

As with lists and tuples, indexing occurs using square brackets `[]`. However, dictionaries are unique in that they are indexed by their keys. When a specific *key* is indexed, the *value* stored in that key is returned.

For example, if we index to specify we want information from 'key_1', note that 'value_1' is returned. This is because we index *by* keys to return the *values* stored in those keys:

# Dictionaries are indexed using their keys
dictionary['key_1']

## Uses: dictionaries 

Dictionaries are particularly helpful when you want to store related pieces of information. For example, if you had a list of names and their respecititve emails, you would want to store these two pieces of information in such a way that you knew which email addresses were related to which individuals. A dictionary is perfect for this! The names of the individuals therefore become the keys and their respective emails the values:

student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : 'ada@analyticengine.com',
    'Alan Turing' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}

student_emails

Dictionaries, like lists, are *mutable*. This means that dictionaries, once created, values *can* be updated.

For example, if you wanted to store information about students' attendance for a particular lab, you could store `True` for all students who attended and `False` for all who failed to attend.

# remember what dictionary we created above
lab_attendance = {
    'A1234' : True,
    'A5678' : False,
    'A9123' : True
}

lab_attendance

If later on you were made aware that the student with the ID 'A5678' did in fact attend lab, you could update the value stored for that key.

This occurs as we've seen with other types of collections. The key is index and the value for that key is then assigned to the indexed value. The distiction here is that the *value* for the specified key is updated, and not the key itself.

# change value of specified key
lab_attendance['A5678'] = True
lab_attendance

With this change, all three keys now store the value `True`.

## Key Deletion

Because dictionaries are mutable, key-value pairs can also be removed from the dictionary using `del`.

In our example above, if student 'A5678' dropped the course, they could be dropped from the dictionary as well. The resulting dictionary now has only two key-value pairs.

print(lab_attendance)
len(lab_attendance)

## remove key-value pair using del
del lab_attendance['A5678']

print(lab_attendance)
len(lab_attendance)

## Operators: dictionaries

The operators we've discussed previously can be used when working with dictionaries.

To determine if a specified *key* is present in a dictionary we can again use the `in` operator:

if 'A1234' in lab_attendance:
  print('Yes, that student is in this class')

## Dictionary Properties

When storing key-value pairs in dictionaries, there are a number of additional rules and properties that are important to understand to effectively use dictionaries:

**Property #1**
- Only one value per key. No duplicate keys allowed. 
    - If duplicate keys specified during assignment, the last assignment wins.

In this example here, there are three key-value pairs specified in the creation of the dictionary; however, only the last key-value pair is stored:

# Last duplicate key assigned wins
{'Student' : 97, 'Student': 88, 'Student' : 91}

**Property #2**
- **keys** must be of an immutable type (string, tuple, integer, float, etc)
- Note: **values** can be of any type

Here, this code produces an error, as the dictionary attempts to use a *mutable* type for the dictionary's key:

# lists are not allowed as key types
# this code will produce an error
{['Student'] : 97}

**Property #3**
- Dictionary keys are case sensitive.

As with everything when it comes to code, capital and lowercase letters are distinct characters. Thus, case sensitivity matters. The key 'Student' and the key 'STUDENTS' are two distinct keys and will be treated as such in dictionary generation.

{'Student' : 97, 'student': 88, 'STUDENT' : 91}

## Exercises

Q1. **Which of the following would create a dictionary of length 3?**

A) `{'Student_1' : 97, 'Student_2'}`  
B) `{'Student_1', 'Student_2', 'Student_3'}`  
C) `['Student_1' : 97, 'Student_2': 88, 'Student_3' : 91]`  
D) `{'Student_1' : 97, 'Student_2': 88, 'Student_3' : 91}`  
E) `('Student_1' : 97, 'Student_2': 88, 'Student_3' : 91)`  

Q2. **Fill in the '---' in the code below to return the value stored in the second key.**

```python
height_dict = {'height_1' : 60, 'height_2': 68, 'height_3' : 65, 'height_4' : 72}
height_dict[---]
```

Q3. **Write the code that would create a dictionary `car` that stores values about your dream car's `make`, `model`, and `year`.**

Q4. **What would the value of `result` be after this code has executed?**

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

Q5. **Why does the following code produce an error?**

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
