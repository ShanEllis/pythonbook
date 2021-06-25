# Practice: Functions

In this set of practice problems, it's all about functions - how to execute them, how to write our own functions, and how to debug functions.

As for all practice sectiosn, each question will include a handful of `assert` statements. After you write and execute the code to each question, each `assert` should "pass silently" (meaning: should give no output upon execution) indicating that you are on the right track. After you've written your code and run the `assert`s, you can always check your answers, as the answers to these questions are included in the "Answers" chapter of this book.

## Function Execution

**Function Execution 1**. The function `square_default` has been provided for you. After defining the function, execute (use) this function to create the following variables under the specified conditions:

1. `square_default` | execute the `square_all` function using the default parameter such that the output will carry out the function on a list of input values containing the integers 2, 3, and 4. 
2. `power_three` | Use the same input values as above, but this time, use the `square_all` function provided to raise all input values to the power 3
3. `out_4` | Execute the `square_all` function such that `out_4` will store a list with 4 values, each of which is the integer 4.

Function provided:
```python
def square_all(collection, power=2):
    
    square_list = []
    for val in collection:
        square_list.append(val**power)
    
    return square_list
```

Checks you can use to see if you're on the right track:

assert  square_default == [4,9,16]
assert power_three  == [8, 27, 64]
assert out_4  == [4,4,4,4]

**Function Execution Q2**. The function `convert_temp` has been provided for you. After understanding the code in the function, define the function. Then, execute (use) this function to create the following variables under the specified conditions:

1. `tempA` | execute the `convert_temp` function to convert the temperature 95 degrees Fahrenheit into degrees Celsius
2. `tempB` | execute `convert_temp` to convert the temperature 17 degrees Celsius into degrees Fahrenheit

Provided function:
```python
def convert_temp(temp, input_unit='F'):
    
    if input_unit == 'F':
        out_temp = (temp - 32) * 5/9
    elif input_unit == 'C':
        out_temp = (temp * 9/5) + 32
    else:
        print("Please specify either 'F' or 'C' for input_unit")
        
    return out_temp
```

Checks you can use to see if you're on the right track:

assert tempA == 35.0
assert tempB == 62.6

**Function Execution Q3** The function `court_jester_jokes` that has been provided for you. After understanding the code in the function, run the cell below (to define this function). Then, execute (use) this function to create the following variables under the specified conditions:

1. `joke_random` | execute the `court_jester_jokes` function to return a joke at random
2. `joke_nonrandom` | execute `court_jester_jokes` to return the second joke in `joke_list`

Function provided:
```python
import random

def court_jester_jokes(random_joke=True):
    joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
                 'How does the court jester address the King of Ducks? Mal’Lard',
                 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
                 'What do you call a joke made by using sign language? A jester']
    
    if random_joke:
        out_joke = random.choice(joke_list)
    else:
        out_joke = joke_list[1]

    return out_joke
```

jokes = ['A clown held the door open for me yesterday. I thought it was a nice jester',
         'How does the court jester address the King of Ducks? Mal’Lard',
         'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
         'What do you call a joke made by using sign language? A jester']
assert joke_random in jokes
assert joke_nonrandom == 'How does the court jester address the King of Ducks? Mal’Lard'

## User-Designed Functions (UDFs)

**UDFs Q1** Write a function `provide_info` that takes three parameters: `name`, `year`, and `school`. Set the default value for `school` to be 'UCSD'.

This function should `return` the string "Hi! I'm `name`. I am a `year` at `school`." (where the variable names are replaced by the values input to the function upon execution).

For example, one possible execution of this function could return "Hi! I'm Shannon. I am a sophomore at UCSD."

Note: Be sure punctuation and spacing match that specified in the instructions.

Checks you can use to see if you're on the right track:

assert provide_info(name='Taylor', year='junior', school='UCLA') == "Hi! I'm Taylor. I am a junior at UCLA." 
assert provide_info(name='Shannon', year='junior') == "Hi! I'm Shannon. I am a junior at UCSD."

**UDFs Q2**. Write a function `count_int` that will take a tuple or list as the input and count the number (count) of integer values in that tuple/list, returning this value from the function. 

For example, if 3 of the values in the input list were integers, the function would return 3.

Note: You can assume the input to this function will be a tuple or list and do *not* need to write code to check whether or not this is true.

Checks you can use to see if you're on the right track:

assert count_int(['string']) == 0
assert count_int((1,2,3,4,5,'string',4.4)) == 5

**UDFs Q3**. Define a function `modify_string` with a single parameter `input_string`. If any of the characters in the `input_string` to the function are keys in the dictionary `new_language` below, use that key's value in that letter's place. If the letter is not in `new_language`, the resulting string should store the same character.

For example, if `my_name` stored 'Shannon', the output from this function would store 'Shӓnnðn' (the a and the o have the modified character from `new_language`)


Variable provided:

```python
new_language = {'a': 'ӓ',
                'e' : 'ɚ',
                'i' : '¡',
                'o' : 'ð', 
                'u' : 'û',
                'A' : 'Ӓ', 
                'E' : 'ɛ', 
                'O' : 'Ó', 
                'U' : 'Ü'}
```

Checks you can use to see if you're on the right track:

assert modify_string('AaEe') == 'Ӓӓɛɚ'
assert modify_string('BbCc') == 'BbCc'
assert modify_string('Taylor') == 'Tӓylðr'
assert modify_string('AaBbCcEe') == 'ӒӓBbCcɛɚ'

**UDFs Q4** Write a function `calculate_points` that has a single input parameter: `hand`. `hand` can be assumed to be a list of string values, where each string corresponds to a value in a deck of cards (2-10, J, Q, K, or A)

This function should calculate the total number of "pointer" cars in your hand, where ***a "pointer" is either a 10, J, Q, K, or A***. Each "pointer" is worth one point. All other cards are worth zero points. The function should `return` the total number of points in the `hand` as an integer.

For example, if your `hand` input was: 

```python
['J', '10', '2', '5', 'K']
```

executing the `calculate_points()` function with the above list as the input to the `hand` parameter, the function would `return` the integer 3 (one point each for the `'J'`, `'10'`, and `'K'`.

If there are no pointers in the input `hand`, the function should return 0.

Checks you can use to see if you're on the right track:

assert calculate_points(['2', '7', '9']) == 0
assert calculate_points(['K']) == 1
assert calculate_points(['J', '10', '2', '5', 'K']) == 3

**UDFs Q5**. Recently, the company you work at ('cogs co.') realized that too many employees have problematic usernames. You're going to write a function (`change_username()`) that takes a single parameter `username` as input. 

This function will check if the `username` meets the following specifications:
- contains more than four characters
- includes only letters (A-Z; a-z) and/or numbers (0-9); in other words: is alphanumeric
- does NOT include the string 'cogs'

If the `username` meets the above specifications, the function will `return` `False` (indicating the username does *not* have to be changed. If any one of the above specifications is not met, the function will `return` `True` (indicating that the `username` does *not* meet at least one of the above specifications).

For example, `change_username(username='cogs')` would `return` `True` because it does not contain more than four letters *and* because it includes the string `'cogs'` in its name, while `change_username(username='Shannon')` would return `False`, as this meets all three specifications above. 

Checks you can use to see if you're on the right track:

assert change_username('aaaaa') == False
assert change_username('aaaa') == True
assert change_username('AAAAA') == False
assert change_username('12345') == False
assert change_username('cogs123') == Trueb

**UDFs Q6**. Write a function that, given a salary as input, will `return` how much of that person's salary is going toward taxes.

To accomplish this, write a function `to_taxes()` that takes two parameters as input: `salary` and `tax_brackets`. The default value for the `tax_brackets` parameter should be the `default_brackets` dictionary provided below. Then, use code constructs discussed in class to accomplish the above goal.

Note that the dictionary `default_brackets` provided will have to be used to accomplish this goal. The keys in `default_brackets` are the proportion of an individual's salary that will go toward taxes if their salary is within the range in a given key's value (tuple). For example, an individual who makes \$10,000 would contribute 12\% of their salary in taxes, given the information in `tax_brackets` (specifically becasue 10000 falls between 9876 and 40125).

Accordingly, `to_taxes(salary=10000)` should `return` 1200.0 (which corresponds to 12\% of the input $10,000 salary).

Variable provided:

```python
default_brackets = {0.10 : (0, 9875),
                    0.12 : (9876, 40125),
                    0.22 : (40126, 85525),
                    0.24 : (85526, 163300),
                    0.32 : (163301, 207350),
                    0.35 : (207351, 518400)
                   }
```

Checks you can use to see if you're on the right track:

assert to_taxes(10000) == 1200.0
assert to_taxes(207355) == 72574.25
assert to_taxes(40126) == 8827.72
assert to_taxes(85525) == 18815.5
assert to_taxes(100, tax_brackets={0.5: (0,1000)}) == 50.0

## Debugging

**Debugging Q1** The function `count_consonants` is provided, but it is not operating as anticipated.

`count_consonants` is _supposed_ to take a string as input and count the number of each consonant in the `input_string` (input parameter), storing the output in a dictionary where the key is the consonant and the value is the number of times it appears in the input. 

Note that we want capitalization to be considered such that the capital and lower case letters are counted together, and the lower case letter is used as the key (i.e. 'A' and 'a' would both be counted under the key 'a')

Specifically, if the `input_string` were "Mohammed", the function ould return: `{'m': 3, 'h': 1, 'd': 1}`

Debug, edit, and test the function provided so that it accomplishes the intended goal.

Function provided:

```python
def count_consonants():
    out = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in input_string:
        
        if char not in vowels:
            if char not in out:
                out[char] = 1
```

Checks you can use to see if you're on the right track:

assert count_consonants('Taylor') == {'t': 1, 'y': 1, 'l': 1, 'r': 1}
assert count_consonants('AaBbCc') == {'b': 2, 'c': 2}

**Debugging Q2** The provided `new_encrypt` function is not operating as anticipated.

`new_encrypt` is _supposed_ to take a string as input and return the reverse alphabetical string as output, meaning, given a character, return the capitalized character in the reverse position within the alphabet. 

For example, if the input character is 'B' or 'b', the function would store 'Y' in the output string. If the character is 'A' or 'a', the function would store 'Z'. (and vice versa: the input 'Z' or 'z' would store 'A').

Specifically, if the `input_string` were "ABc", the function would `return`: 'ZYX'

Debug, edit, and test the function provided below so that it accomplishes the intended goal.

Provided function:

```python
def new_encrypt():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    for char in input_string:
        if char in alpha:
            position = alpha.find(char)
            output_string += reverse_alpha[position]
        else:
            output_string = None
            break
```

Checks you can use to see if you're on the right track:

assert new_encrypt('mohammed') == 'NLSZNNVW'
assert new_encrypt(input_string='ABC') == 'ZYX'

**Debugging Q3** The not-totally-functioning `growth_rate()` function is provided for you. The *goal* of this function, is given two population inputs: `last_year`, `this_year`, the function should return the population growth rate for that country.

For example, in 2020, China's population was `1439323776`. This year, its population is `1444216107`.

Population growth rate is calculated by taking the difference between this year's population minus last year's population, dividng that difference by last year's population, and multiplying the entire quantity by 100.

Given China's numbers above and this calculation, we know that this function should return `0.34`...but it's not at this point.

Consider the function currently and then debug (you can edit the code provided directly or copy and paste below so you still have the original if needed) to accomplish the task specified above. 

Note: Do not change the name of the function (`growth_rate`), and the parameter names provided in the instructions (`last_year`, `this_year`) must be used.

Function provided:
```python
def growth_rate(self, this_year, last_year):
    self.this_year - self.last_year/self.last_year * 100
```

assert 0 < growth_rate(last_year=331002651,
                       this_year=332915073) > 1