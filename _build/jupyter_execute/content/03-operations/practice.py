# Practice: Collections & Loops

This section is meant to give you additional practice, with a particular focus on collections and loops. However, we do assume that you have the previous section's material understood as well, so we can't forget about conditionals or variable types learned previously. 

As in the last practice section, each question will include a handful of `assert` statements. After you write and execute the code to each question, each `assert` should "pass silently" (meaning: should give no output upon execution) indicating that you are on the right track. After you've written your code and run the `assert`s, you can always check your answers, as the answers to these questions are included in the "Answers" chapter of this book.

## Collections

**Collections Q1**. The list `trees` has been provided below for you.

***Use the `trees` variable and indexing*** to generate each of the four variables at left below, so that each stores the output at right below. For example, `trees_a` should refer to `trees` in its answer and use indexing to store the string 'Pine'.

- `trees_a` | `'Pine'`
- `trees_b` | `['Liquid Amber', 'Pepper', 'Podocarpus']`
- `trees_c` | `['Eucalyptus', 'Ficus', 'Tipuana', 'Pepper']`
- `trees_d` | `['Palms', 'Carrotwood', 'Tipuana', 'Podocarpus']`

Variable provided:

```python
trees = ['Palms', 'Jacaranda', 'Eucalyptus', 'Carrotwood', 
         'Ficus', 'Pine', 'Tipuana', 'Liquid Amber', 
         'Pepper', 'Podocarpus']
```

Checks you can use to see if you're on the right track:

assert trees_a == 'Pine'
assert trees_b == ['Liquid Amber', 'Pepper', 'Podocarpus']
assert trees_c == ['Eucalyptus', 'Ficus', 'Tipuana', 'Pepper']
assert trees_d == ['Palms', 'Carrotwood', 'Tipuana', 'Podocarpus']

**Collections Q2**. 

Part I. Generate a list called `practice_list` that meets the following criteria:

- contains 6 elements/items 
- has 2 strings, 1 float, 1 boolean, 1 dictionary, and 1 tuple as its elements

The specific elements in the list `practice_list` are up to you and can be stored in any order/position within the list, so long as they're in there and of the types specified above.

Checks you can use to see if you're on the right track:

assert isinstance(practice_list, list)
assert len(practice_list) == 6

Part II. Using the list you defined in Part 1 (`practice_list`), ***use indexing*** to return the slice/element of the list specified below, storing it in the variable name provided:

- `slice_1` | stores the second, third, and fourth elements in `practice_list`
- `slice_2` | stores the second, fourth, and sixth elements in `practice_list`
- `slice_3` | uses ***negative indexing*** to return the single element stored in the third position from the end of `practice_list`

Note on wording: the first _element_ in a given list is the same as the 0<sup>th</sup> _index_ of that list.

Checks you can use to see if you're on the right track:

assert len(slice_1) == 3
assert len(slice_2) == 3
assert slice_3

**Collections Q3**. Generate a dictionary called `practice_dict` that meets the following criteria:

- has three keys: 'name', 'favorite_game', and 'height'
- stores _your_ `name` (string), `favorite_game` (string), and `height` (int) in inches as each key's value

Checks you can use to see if you're on the right track:

assert isinstance(practice_dict, dict)
assert len(practice_dict) == 3
assert isinstance(practice_dict['name'], str)
assert isinstance(practice_dict['favorite_game'], str)
assert isinstance(practice_dict['height'], int)

**Collections Q4**. 

Part I. Generate a dictionary called `grading` that meets the following criteria:

- has 5 keys: 'A', 'B', 'C', 'D', 'F'
- stores a tuple containg the lower and upper bound for each letter grade for each key's value.

Use the following ranges for reference:

- A: 90-100
- B: 80-90
- C: 70-80
- D: 60-70
- F: 0-60

Note that the upper bound for one letter will be the same value as the lower bound for the higher grade. This is expected behavior.

Checks you can use to see if you're on the right track:

assert isinstance(grading, dict)
assert len(grading) == 5
assert isinstance(list(grading.keys())[0], str)
assert isinstance(list(grading.values())[0], tuple)
assert list(grading.keys()) == ['A', 'B', 'C', 'D', 'F']
assert list(grading.values()) == [(90, 100), (80, 90), (70, 80), 
                                  (60, 70), (0, 60)]

Part II. Use the `grading` dictionary you just generated **and indexing** to generate two variables: `A_lower` and `A_upper`.

- `A_lower` will store the first (smaller) value in the tuple corresponding to the `'A'` key in `grading`.
- `A_upper` will store the second (larger) value in the tuple corresponding to the `'A'` key in `grading`

Note: Do not hard-code. For example, `A_lower = 90` is *not* the correct answer. Your code should reference `grading` and use indexing to store the value 90 in `A_lower`.

Checks you can use to see if you're on the right track:

assert A_lower == 90
assert A_upper == 100

**Collections Q5**. Create three variables ***using the dictionary `cogs18_dict` provided*** below and functions discussed in class that will store the variable specified:

1. `dict_a`: stores 'Prof'
2. `dict_b`: stores 'dict' (or, when printed: `<class 'dict'>`)
3. `dict_c`: stores `5`

Variable provided:

```python
cogs18_dict = {'Annie' : 'TA',  'Ashlesha' : 'TA', 'Paul' : 'TA', 
               'Mudit': 'TA', 'Ellis' : 'Prof'}

```

Note: each variable's line of code must have `cogs18_dict` as part of your code.

Checks you can use to see if you're on the right track:

assert dict_a == 'Prof'
assert dict_b == dict
assert dict_c == 5

## Loops

**Loops Q1**. Store your first name as a string in the variable `my_name` and initialize a `counter` (use that variable name) 

Then, write a `for` loop that loops through the letters of your first name, increasing the counter by one for each letter in your name. The value stored in the counter at the end of your loop’s execution should be the number of letters in your first name.

Checks you can use to see if you're on the right track:

assert isinstance(counter, int)
assert isinstance(my_name, str)
assert len(my_name) == counter

**Loops Q2**. Somehow you've got a list of words, but you want them all combined into the single string `"I'm so excited that students are now eligible for the vaccine!"`. Write code that uses `vaccination_list` to accomplish this task.

Variable provided:

```python
vaccination_list = ["I'm ", "so ", "excited ", "that ", "students ", "are ", 
                    "now ", "eligible ", "for ", "the ", "vaccine!"]
```

Checks you can use to see if you're on the right track:

assert sentence == "I'm so excited that students are now eligible for the vaccine!"

## Topic Synthesis

**Synthesis Q1**. Write code that:

1. Creates (initializes) a counter `val` that starts at 0
2. Creates (initializes) an empty list `output`
3. Creates a loop that will run as long as the value of `val` is less than or equal to 100
    - Within the loop:
        - first: if the value of `val` is divisible by 10, `append` the value of `val` to the list `output`
        - then: increase the value of `val` by 1 each time through the loop
        
Checks you can use to see if you're on the right track:

assert val == 101
assert isinstance(output, list)
assert output == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] or output == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

**Synthesis Q2**. Store your first name as a string in the variable `my_name` and initialize a `counter` (use that variable name).

Then, write a `for` loop that loops through the letters of your first name, increasing the counter by one for each consonant (non-vowel) in your name. 

The value stored in the counter at the end of your loop’s execution should be the number of consonants in your first name. Be sure that 'B' and 'b' are counted as the same letter in your code.

Checks you can use to see if you're on the right track:

assert isinstance(counter, int)
assert isinstance(my_name, str)

**Synthesis Q3**. 

Part I.

Store your first name as a string in the variable `my_name`. Then, write code that will generate a dictionary name_consonants that stores each consonant letter in `my_name`  as a key in the dictionary, and the number of times each consonant shows up in my_name as the letter's value.

Noe that this code should run, regardless of what string is stored in my_name.

For example, name_consonants for 'Shannon' would return:

{'s': 1, 'h': 1, 'n': 3}

Note that if you have no consonants in your name, this code would still run, but would return an empty dictionary.

Checks you can use to see if you're on the right track:

assert isinstance(my_name, str)
assert isinstance(name_consonants, dict)

Part II.

Write code that will loop through the `name_consonants` dictionary created in the first part of this question and store the sum of the values in the dictionary into `consonant_count`. (For the name 'Shannon', `consonant_count` would store 5).

Checks you can use to see if you're on the right track:

assert consonant_count is not None

**Synthesis Q4**. Background: Imagine that you're taking a course with an instructional staff including TAs (graduate students) and IAs (undergraduates who previously took the course). This means that the IAs have previously completed the course final project, and you want to talk to someone who has previously completed the project to get some questions answered. As you have this thought, you suddenly remember you created a list of all the staff members in the course earlier in the quarter when you were practicing with lists. Perfect! You can use this to help you figure out who you should talk to, since you know that all of the IAs previously took this course and completed the project. They will be able to discuss their experience with you!

Variables provided:

```python
staff = ['Anu_IA', 'Bob_IA', 'Boning_IA', 'Bora_IA', 'David_TA', 'Emma_IA', 
         'Ellis_Prof', 'Frank_IA', 'Mani_IA', 'Harrison_IA', 'Shivani_TA']
```

Use code constructs to extract a list of individuals you could talk to, storing this output in a list `to_contact`.

Checks you can use to see if you're on the right track:

assert to_contact == ['Anu_IA',
                     'Bob_IA',
                     'Boning_IA',
                     'Bora_IA',
                     'Emma_IA',
                     'Frank_IA',
                     'Mani_IA',
                     'Harrison_IA']

**Synthesis Q5**. Imagine you want to determine the total number of students Professor Ellis has taught in COGS 18 during her first few years as a Professor.

To do so, use the provided dictionary `ellis_courses`. This dictionary stores course names and quarters as keys and the number of students enrolled as values.

Then, using the information in the `ellis_courses` dictionary, determine what code constructs you would need to sum the values for the students who have taken 'cogs18' with Professor Ellis. Store this value in the variable `cogs18_students`.

```python
ellis_courses = {'cogs9_wi19': 326,
                 'cogs108_sp19': 825,
                 'cogs18_sp19' : 272,
                 'cogs9_fa19' : 292,
                 'cogs18_fa19' : 301,
                 'cogs108_wi20' : 442,
                 'cogs18_sp20' : 307,
                 'cogs108_sp20' : 469,
                 'cogs18_su20' : 88,
                 'cogs18_fa20' : 330,
                 'cogs108_fa20' : 498,
                 'cogs18_wi21' : 99,
                 'cogs108_wi21' : 431, 
                 'cogs18_sp21' : 100,
                 'cogs108_sp21': 311 
                }
```

Checks you can use to see if you're on the right track:

assert isinstance(cogs18_students, int)
assert cogs18_students == 1497

**Synthesis Q6**. Background: Professor Ellis has made a mess of her to do list (`to_do_list`, provided below). She accidentally combined her to do list with her grocery list and the the her daily step count from last week. She needs your help to detangle this mess!

Part I.

Your job is to separate `to_do_list` out into three separate lists:
- `steps` - a list of all the steps from last week (you know which values these are becuase they are integer values)
- `to_do` - a list that contains the to do list items (you know which values these are because they contain 'cogs' in the string)
- `grocery` - a list of all of the grocery list items (you know which values these are because they do NOT contain 'cogs' in the string)

Each of the above lists should contain only the elements from `to_do_list` that match the specified description above. Specifically:
- `steps` should be a list of integers
- `to_do` should be a list of strings 
- `grocery` should be a list of strings

The values in `steps`, `to_do`, and `grocery` should appear in the same relative order as in the original list (`to_do_list`).

Note: This should not be hard-coded. Your answer should use code constructs discussed in class. In other words, your code should produce the correct lists, regardless of the specific values in `to_do_list`.

Variable provided:
```python
to_do_list = ['mushrooms', 'peanut butter', 'release cogs18 exam', 10000, 8500, 
              'release cogs108 lab', 6000, 'tahini', 15000, 'post cogs18 lectures', 
              'post cogs108 lectures', 'release cogs18 practice exam', 12000, 'pineapple', 
              'udon noodles', 18000, 8000, 'romaine lettuce']
```
Checks you can use to see if you're on the right track:

assert grocery == ['mushrooms', 'peanut butter',
                   'tahini', 'pineapple', 'udon noodles',
                   'romaine lettuce']
assert steps == [10000, 8500, 6000, 15000, 12000, 18000, 8000]
assert to_do ==  ['release cogs18 exam', 'release cogs108 lab',
                  'post cogs18 lectures', 'post cogs108 lectures',
                  'release cogs18 practice exam']

Part II. 

Now that you've got the `steps` extracted, Professor Ellis needs a dictionary of which steps she took on which day. 

Using the values in your list `steps`, create a dictionary `steps_dict` that stores each value as a different day's steps, starting with 'Monday'. For example, the first value in the `steps` list will be the value for the key 'Monday', the second for 'Tuesday', so on and so forth. 

Be sure to spell out the day of the week, using a capital letter for the first letter in the day. The list `days_of_week` has been provided, as it may be helpful in answering the question.

Note: This should not be hard-coded. Your answer should use code constructs discussed in class. In other words, your code should produce the correct `steps_dict` if the specific values in `steps` were to change/differ.

Variable provided (may be helpful):

```python
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday', 'Sunday']
```

Checks you can use to see if you're on the right track:

assert all(isinstance(x, str) for x in list(steps_dict.keys()))
assert all(isinstance(x, int) for x in list(steps_dict.values()))
assert set(list(steps_dict.keys())) ==  set(days_of_week)
assert sum(steps_dict.values()) ==  77500