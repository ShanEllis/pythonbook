# Answers: Collections & Loops

Provided here are answers to the practice questions at the end of "Collections & Loops".

## Collections

**Collections Q1**.

# actual approaches could differ
trees_a = trees[5]
trees_b = trees[-3:]
trees_c = trees[2:9:2]
trees_d = trees[::3]

**Collections Q2**.

Part I.

# actual values will differ
practice_list = ['a', 'b', 2.9, True, 
                 {'A':1, 'B':2}, (2, 3)]

Part II.

slice_1 = practice_list[1:4]
slice_2 = practice_list[1::2]
slice_3 = practice_list[-3]

**Collections Q3**.

practice_dict = {'name': 'Shannon',
                 'favorite_game' : 'Coup',
                 'height': 65}

**Collections Q4**.

Part I.

grading = {'A': (90, 100),
           'B': (80, 90),
           'C': (70, 80),
           'D': (60, 70),
           'F': (0, 60)}

Part II.

A_lower = grading['A'][0]
A_upper = grading['A'][1]

**Collections Q5**.

dict_a = cogs18_dict['Ellis']
dict_b = type(cogs18_dict)
dict_c = len(cogs18_dict)

## Loops

**Loops Q1**.

my_name = 'Shannon'
counter = 0

for char in my_name:
    counter += 1

**Loops Q2**.

# there are other approaches that use string methods
sentence = ''

for word in vaccination_list:
    sentence += word

## Topic Synthesis

**Synthesis Q1**.

output = []
val = 0 

while val <= 100: 
    if val % 10 == 0:
        output.append(val)
    
    val += 1

**Synthesis Q2**.

# output will differ based on my_name
my_name = 'Shannon'
counter = 0

for char in my_name:
    char = char.lower()
    if char not in ['a', 'e', 'i', 'o', 'u']:
        counter += 1

**Synthesis Q3**.

Part I.

# output will differ based on my_name
my_name = 'Shannon'
name_consonants = {}

vowels = ['a', 'e', 'i', 'o', 'u']
            
for char in my_name:
    char = char.lower()
    if char not in vowels:
        if char not in name_consonants:
            name_consonants[char] = 1
        else:
            name_consonants[char] += 1  

Part II.

# output will differ based on who is taking the exam
consonant_count = 0

for key in name_consonants:
    consonant_count += name_consonants[key]

**Synthesis Q4**.

to_contact = []

for person in staff:
    if '_IA' in person:
        to_contact.append(person)

**Synthesis Q5**.

# there are multiple possible solutions/approaches
cogs18_students = 0

for key in ellis_courses:
    if 'cogs18' in key:
        cogs18_students = cogs18_students + ellis_courses[key]

cogs18_students

**Synthesis Q6**.

Part I.

# there are multiple possible solutions/approaches
steps = []
to_do = []
grocery = []

for value in to_do_list:
    if isinstance(value, int):
        steps.append(value)
    else:
        if 'cogs' in value:
            to_do.append(value)
        else: 
            grocery.append(value)

Part II.

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday', 'Sunday']
steps_dict = {}

for i in range(0,7):
    key = days_of_week[i]
    val = steps[i]
    steps_dict[key] = val