# Practice: The Basics

With variables, conditionals and operators under your belt, this chapter is meant to give you additional practice. Note that each question will include a handful of `assert` statements. After you write and execute the code to each question, each `assert` should "pass silently" (meaning: should give no output upon execution) indicating that you are on the right track. After you've written your code and run the `assert`s, you can always check your answers, as the answers to these questions are included in the "Answers" chapter of this book.

## Variables

**Variables Q1**. Write five lines of code that define five different variables named `var_float`, `var_str`, and `var_bool`, `var_tuple`, and `var_dict`, storing a float, a string, and a boolean, a tuple, and a dictionary, respectively. (You get to choose the specific float, string, boolean, tuple, or dictionary each variable stores.)

Checks you can use to see if you're on the right track:

assert isinstance(var_float, float)
assert isinstance(var_str, str)
assert isinstance(var_bool, bool)
assert isinstance(var_tuple, tuple)
assert isinstance(var_dict, dict)

**Variables Q2**. Consider each of the following scenarios and determine what type of collection (list, tuple, dictionary) would be best to use. For each scenario, store 'list', 'tuple' or 'dictionary' in the variable specified, depending upon which is best for the given scnenario. (Note: Capitalization and spelling matter.)

For example, for `scenario_A`, if you thought the correct answer were 'list' your answer in the answer cell would be:

```python
scenario_A = 'list'
```

Scenarios:

- `scenario_A` | You want to store all of the names of the films that won an Academy Award last year.
- `scenario_B` | You want to keep a record of all the email addresses (and only the email addresses) of all of Directors working in Hollywood, so that you can email them your brilliant ideas whenever you have them. 
- `scenario_C` | You want to store the names *and* email addresses of all of the Directors working in Hollywood, so that you can email them your brilliant ideas whenever you have them *and* address the email to the right name. 
- `scenario_D` | You want to keep a record of all of the films that have ever won an Academy award and the year in which that award was won.

Checks you can use to see if you're on the right track:

assert scenario_A in ['tuple', 'list', 'dictionary']
assert scenario_B in ['tuple', 'list', 'dictionary']
assert scenario_C in ['tuple', 'list', 'dictionary']
assert scenario_D in ['tuple', 'list', 'dictionary']

## Operators

**Operators Q1** Use the variables provided below (`var_low`, `var_mid` and `var_high`) to generate the variables: `var_even` and `var_odd` according to the following specifications:

- `var_even` | use the 3 variables provided once each and *at least two* of the math operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`) to store the value 12 
- `var_odd` | use the 3 variables provided once each and *at least two* of the math operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`) to store the value 13

Variables provided:

```python
var_low = 2
var_mid = 20
var_high = 30
```

Checks you can use to see if you're on the right track:

assert int(var_even % 2) == 0
assert var_even == 12
assert var_odd % 2 != 0
assert var_odd == 13

**Operators Q2**. First, define two variables below: `my_age` and `pres_age`. Store your age (as an integer) in `my_age` and store the current US President's age (as an integer) in `pres_age`.

Then, use (refer to) `my_age` and `pres_age` to define define two variables: `true_compar` and `false_compar`.

These variables must satisfy the following requirements:

1. Each variable must be defined using one comparison operator (`<`,`>`,`<=`,`>=`,`!=`,`==`).
2. Each variable must use and refer to `my_age` and `pres_age` (and no other values or variables)
4. `true_compar` should evaluate as the boolean `True`; `false_compar` should evaluate as the boolean `False`

Checks you can use to see if you're on the right track:

assert isinstance(my_age, int)
assert my_age < 150
assert pres_age <150
assert true_compar
assert not false_compar

**Operators Q3**. Two variables (`spring_holidays` and `current_holidays`) have been created for you below. Using **only these two variables and membership operators**, define the following two variables below (`yes_member` and `no_member`), such that they meet the following specifications:

- `yes_member` | stores the boolean `True`
- `no_member` | stores the boolean `False`

Variables provided:

```python
spring_holidays = ['César Chávez', 'Passover', 'Easter', 
                   'Ramadan', 'Shavout', 'Memorial Day']
current_holiday = 'Ramadan'
````

Checks you can use to see if you're on the right track:

assert yes_member
assert not no_member

**Operators Q4**. Create three variables: `var_even`, `var_odd`, and `var_operator`.

Across these three variables:
- all seven math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) must be used _at least once_ 
- `var_even` must store an even number
- `var_odd` must store an odd number
- `var_operator` can include other variables/numbers but must use (refer to) the variables `var_even` *and* `var_odd` during assignment and must store (have the value) 6 (or 6.0)

Checks you can use to see if you're on the right track:

assert var_odd % 2 != 0
assert int(var_even % 2) == 0
assert isinstance(var_operator, float) or isinstance(var_operator, int)
assert var_operator == 6

**Operators Q5**. Your answer will define two variables: `true_var` and `false_var`.

These variables must satisfy the following requirements:

1. Each variable must be defined using *at least one* comparison operator (`<`,`>`,`<=`,`>=`,`!=`,`==`).
2. Each variable must use and refer to at least one variables defined below (`var_low`, `var_mid`, `var_high`)
3. Additional values and/or operators may also be used, but `true_var` must use the `or` operator; `false_var` must use the `and` operator.
4. `true_var` should evaluate as the boolean `True`; `false_var` should evaluate as the boolean `False`

Variables provided:

```python
var_low = 35 % 11
var_mid = 5 ** 2
var_high = (14 + 2) * 6
```

Checks you can use to see if you're on the right track:

assert true_var
assert not false_var

**Operators Q6** Create three variables: `comp_a`, `comp_b`, and `comp_c`.

These variables must satisfy the following requirements:

1. Each variable must store (aka return) the Boolean `True`
2. Additional operators may also be used, but `comp_a` must use the `and` operator; `comp_b` must use the `or` operator, and `comp_c` must use the `not` operator. 
3. Each variable must be created using *at least two* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`).
4. All six comparison operators must show up in the cell below *at least once*.

Checks you can use to see if you're on the right track:

assert comp_a
assert comp_b
assert comp_c

**Operators Q7**. Using the following string and list provided below, create two variables `memb_a` and `memb_b` that satisfy the following conditions:

1. `memb_a` must use the `in` operator to check membership in `my_string`. It should store (return) `True`.
2. `memb_b` must use the `not in` operator to check membership in `my_list`. It should store (return) `False`. 
3. `memb_a` must refer to the `my_string` variable defined for you below. `memb_b` must refer to the `my_list` variable defined for you below.

Variables provided:

```python
my_string = 'I love Python!'
my_list = ['Chapters', 'Exercises', 'Practice']
```

Checks you can use to see if you're on the right track:

assert memb_a
assert not memb_b

## Conditionals

**Conditionals Q1**. Store your first name as a string in the variable `my_name`.

Write a conditional that will determine if there are more letters in your name (`my_name`) relative to the number of letters in the `comparison_name` (provided below, and storing the string 'Shannon').

If your name is:
- shorter than the `comparison_name`, store the string 'shorter' in the variable `output`
- longer than the `comparison_name`, store the string 'longer' in the variable `output`
- the same length as `comparison_name`, store the string 'same length' in the variable `output`

Note: Do not hard-code. This means your code should work (store the correct string in `output`) regardless of the specific strings stored in `comparison_name` or `my_name`.

Variable provided:

```python
comparison_name = 'Shannon'
```

Checks you can use to see if you're on the right track:

assert my_name
assert output
assert output in ['shorter', 'longer', 'same length']

## Topics Synthesis

**Synthesis Q1**. Create two variables: `var_cat` and `var_sum`. 

- `var_cat` should store a string created (assigned) by concatenating two strings together 
- `var_sum` should store a numeric variable (float or int) created (assigned) by adding two numeric values together

The specific values you use to generate `var_cat` and `var_sum` are up to you, as long as they fulfull the criteria specified.

Checks you can use to see if you're on the right track:

assert isinstance(var_cat, str)
assert isinstance(var_sum, float) or isinstance(var_sum, int)

**Synthesis Q2**. Create three variables: `var_int`, `var_float`, and `var_combined`. 

- `var_int` should store an integer
- `var_float` should store a float
- `var_combined` should use a math operator to add `var_int` and `var_float` together

The specific values you use to generate `var_int` and `var_float` are up to you, as long as they fulfull the criteria specified.

Checks you can use to see if you're on the right track:

assert isinstance(var_int, int)
assert isinstance(var_float, float)
assert var_combined == var_int + var_float

**Synthesis Q3**. create three variables: `var_a`, `var_b`, and `var_c`.

These variables must satisfy the following requirements:

1. `var_a` must store a float (you get to choose the specific float)
2. `var_b` must use *at least two* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`) and store (return) the value `True`. 
3. `var_c` must use *at least two* of the math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) and store the value 36

Checks you can use to see if you're on the right track:

assert isinstance(var_a, float)
assert var_b 
assert var_c == 36

**Synthesis Q4**. create three variables: `var_a`, `var_b`, and `var_c`. 

- `var_a` should store four characters in an immutable variable type that is only able to store one piece of information
- `var_b` should be a single value that, when added to itself returns a whole number
- `var_c` should be an immutable variable storing three different values

The specific values you use to generate the variables are up to you, as long as they fulfull the criteria specified.

Checks you can use to see if you're on the right track:

assert isinstance(var_a, str)
assert len(var_a) == 4
assert var_b % 1 == 0 
assert isinstance(var_c, tuple)
assert len(var_c) == 3