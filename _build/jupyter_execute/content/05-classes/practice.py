# Practice: Classes

In this set of practice problems, it's all about classes, really putting together everything discussed up to this point, including how to create our own classes of objects, with their own associated attributes and methods.

As for all practice sections, each question will include a handful of `assert` statements. After you write and execute the code to each question, each `assert` should "pass silently" (meaning: should give no output upon execution) indicating that you are on the right track. After you've written your code and run the `assert`s, you can always check your answers, as the answers to these questions are included in the "Answers" chapter of this book.

## Objects

**Objects Q1**. `isalnum()` is a string method that determines if all the characters in a string are alphanumeric (meaning letters or numbers: A-Z, a-z, 0-9).

Use the `isalnum()` method on two strings (of your choosing) below to create two variables:
- `true_var` | should store the value `True`
- `false_var` | should store the value `False`

Checks you can use to see if you're on the right track:

assert true_var
assert not false_var

**Objects Q2**. Here, `site_days` and `days_of_week` have been provided for you. 
- `site_days`: is a (totally made up) list of days on which people received their vaccinations
- `days_of_week`: a tuple containing the days of the week

Note: `count()` is a list method that counts the number of appearances of a specified element in a list.

Using the `count()` method, code constructs discussed in class, and referencing the two variables provided, generate a dictionary:
 - `days_summary`  | whose keys are each of the days of the week in `days_of_week` and whose corresponding values are the number of times each day shows up in `site_days`.
 
Variables provided:
```python
site_days = ['M', 'M', 'M', 'M']
days_of_week = ('M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su')
```

assert list(days_summary.keys()) == ['M', 'Tu', 'W', 'Th',
                                     'F', 'Sa', 'Su']
assert list(days_summary.values()) == [4, 0, 0, 0, 0, 0, 0]

**Objects Q3**. Here, import the `random` module so that you can use the `choice` function from the module. (Note: the `choice` function from the `random` module returns a single value from a collection at random.)

Use the `choice` function from the `random` module to randomly choose a value from `range(0,10)`.

Store the output from this operation in the variable `rand_int`.

Checks you can use to see if you're on the right track:

assert isinstance(rand_int, int)
assert rand_int in range(0,10)

## Classes

**Classes Q1**. Define a class `ClassRoster()` that meets the following specifications:

- has two instance attributes:
    - `students`; initialized as an empty list
    - `course`; which the user specifies when creating a `ClassRoster()` object
- a single method `add_student()`, which will have `pid` and `name` as arguments, and will add these two inputs as a dictionary with `pid` as the key and the student's `name` as the value to the `students` list each time the method is called

Checks you can use to see if you're on the right track:

assert my_course.course == 'COGS 18'
assert my_course.students == []

my_course.add_student(pid='A12345', name='Shannon')
my_course.add_student(pid='A56789', name='Josh')

assert my_course.students == [{'A12345':'Shannon'}, {'A56789': 'Josh'}]

**Classes Q2**. Define a class `ToDo()` to keep track of your to do list.

This should have a single instance attribute: `to_do`, which is initialized as an empty list.

It will then have two methods: `add_item` and `remove_item`.

`add_item()`:
- will have two parameters `item`, and `top` (`top` takes the default value `True`)
- if `top` is `True`:
    the string in `item` will be added to the top of `to_do`:
- if `top` is not true:
    the string it `item` will be added to the end of `to_do`

`remove_item()`:
- will have a single parameter `item`
- will remove the item specified from `to_do`

Note: there is a list method `insert()`, which operates in place to add a value to a list at the index specified with the general syntax `my_list.insert(index, item_to_add)`.

Checks you can use to see if you're on the right track:

my_todo_list = ToDo()
assert my_todo_list.to_do == []

my_todo_list.add_item('A')
my_todo_list.add_item('B')
assert my_todo_list.to_do == ['B','A']

my_todo_list.add_item('C', top=False)
assert my_todo_list.to_do == ['B','A', 'C']

my_todo_list.remove_item('A')
assert my_todo_list.to_do == ['B', 'C']

**Classes Q3**. For this question, let's create a class to celebrate the Lunar New Year!

Here, define a class `NewYear()`.

This class should have:

- **one class attribute**: `zodiac_signs` that stores the dictionary `zodiac_signs` specified below. This dictionary contains the zodiac sign as the key and the birth years that correspond to that sign.
- **one instance attribute**:  `year` that takes the birth `year` as input from the user upon creation of a `NewYear` type object.

This class will also have a method `return_sign()`. This method should `return` (*not* just `print`) a string, similar to:

```
'You were born in the year of the Dragon!' 
```

...where 'Dragon' corresponds to the key from the `zodiac_signs` corresponding to the value stored in the `year` attribute. (Be sure captitalization and punctuation match the string specified here. The only thing that should change is the last word in the string.)

For example `NewYear(year=2021).return_sign()` should return 'You were born in the year of the Ox!', since 2021 is a value in the `zodiac_signs` dictionary for the key 'Ox'. 

Variable provided:
```python
zodiac_signs = {
    'Ox' : [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
    'Tiger' : [1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022], 
    'Rabbit' : [1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023], 
    'Dragon' : [1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024], 
    'Snake' : [1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025], 
    'Horse' : [1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026], 
    'Goat/Sheep' : [1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027], 
    'Monkey' : [1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028], 
    'Rooster' : [1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029], 
    'Dog' : [1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030], 
    'Pig' : [1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031], 
    'Rat' : [1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
} 
```

Checks you can use to see if you're on the right track:

dragon = NewYear(1988)
assert isinstance(dragon, NewYear)
assert dragon.year ==  1988
assert dragon.return_sign() == 'You were born in the year of the Dragon!'
assert isinstance(dragon.zodiac_signs, dict)
assert 'Ox' in dragon.zodiac_signs.keys()

**Classes Q4**. 

Part I.

For this question, imagine you want to create a video game with a handful of characters. You want this game to have a royal kingdom theme.

Here, define a class `Kingdom()`.

This class should have two instance attributes: `name` and `title`, which will be strings specifying the name and title of the character (in that order).

This class will also have a method `introduce()`. This method should `return` (*not* just `print`) a string, similar to:

```
'Hello, my name is Ferdinand, and I am a King.' 
```

...where 'Ferdinand' corresponds to whatever is stored in `Kingdom()` object's `name` attribute is and 'King' corresponds to whatever is stored in the `Kingdom()` object's `title` attribute.

Checks you can use to see if you're on the right track:

queen = Kingdom('Elizabeth', 'Queen')
assert isinstance(queen, Kingdom)
assert queen.name == 'Elizabeth'
assert queen.title == 'Queen'

assert callable(queen.introduce)
assert isinstance(queen.introduce(), str)

Part II.

Generate a class called `CourtJester()`.

This object should inherit all attributes and methods from `Kingdom()`.

Additionally, the `CourtJester()` object should have:
- a class attribute `headwear`, storing the value `'fool's cap'`
- a method `tell_a_joke()` that should `return` a joke at random from the list provided below

(Note: You'll likely want to import from the `random` module here. Use of a function from that module will likely be helpful in `tell_a_joke()`.)

Variable provided:
```python
joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
 'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']
```

Checks you can use to see if you're on the right track:

jester = CourtJester('Barney', 'Jester')
assert jester.headwear == "fool's cap"
assert jester.name == 'Barney'
assert jester.title == 'Jester'

joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']
assert jester.tell_a_joke() in joke_list

**Classes Q5**. Generate a class called `StudentInfo`.

This class should have four *instance attributes*: `name`, `year`, `school`, and `proj_grade`. 

This class must also have a single method: `follow_up`. This method should determine if `proj_grade` is 65 or below. If `proj_grade` is 65 or below, the method should return the name of the student as the key and their proj_grade as the value in a dictionary. (If the student has a grade above 65, this method should return an empty dictionary.)

Checks you can use to see if you're on the right track:

student1 = StudentInfo(name='Shannon', year='sophomore', school='UCSD', proj_grade=63)
student2 = StudentInfo(name='Josh', year='senior', school='UCSD', proj_grade=88)

# test attributes
assert student1.name == 'Shannon'
assert student1.school == 'UCSD'
assert student2.year == 'senior'
assert student2.proj_grade == 88

assert student1.follow_up() == {'Shannon': 63}
assert student2.follow_up() == {}