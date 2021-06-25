# Answers: Functions

Provided here are answers to the practice questions at the end of "Functions".

## Function Execution

**Function Execution Q1**

square_default = square_all([2,3,4])
power_three = square_all([2,3,4], 3)
out_4 = square_all([2,2,2,2]) # this execution could differ

**Function Execution Q2**.

tempA = convert_temp(95)
tempB = convert_temp(17, 'C')

**Function Execution Q3**

joke_random = court_jester_jokes()
joke_nonrandom = court_jester_joke

## User-Designed Functions

**UDFs Q1**

# there are multiple approaches to string concatenation
def provide_info(name, year, school='UCSD'):
    output = "Hi. I'm " + name + '. I am a ' + year + ' at ' + school + '.'
    return output

**UDFs Q2**.

def count_int(col):
    count = 0
    
    for val in col:
        if type(val) == int:
            count += 1
    
    return count

**UDFs Q3**.

def modify_string(input_string):
    
    new_language = {'a': 'ӓ',
                'e' : 'ɚ',
                'i' : '¡',
                'o' : 'ð', 
                'u' : 'û',
                'A' : 'Ӓ', 
                'E' : 'ɛ', 
                'O' : 'Ó', 
                'U' : 'Ü'}
    
    modified_name = ''
    for letter in input_string:
        if letter in new_language:
            modified_name = modified_name + new_language[letter]
        else:
            modified_name = modified_name + letter

    return modified_name

**UDFs Q4**.

def calculate_points(hand):
    pointers = ['10', 'J', 'Q', 'K', 'A']
    counter = 0
    
    for card in hand:
        if card in pointers:
            counter += 1
        
    return counter

**UDFs Q5**

# there are multiple approaches that work
def change_username(username):
    if len(username) > 4 and username.isalnum() and 'cogs' not in username:
        return False
    else:
        return True

**UDFs Q6**

default_brackets = {0.10 : (0, 9875),
                    0.12 : (9876, 40125),
                    0.22 : (40126, 85525),
                    0.24 : (85526, 163300),
                    0.32 : (163301, 207350),
                    0.35 : (207351, 518400)
                   }

def to_taxes(salary, tax_brackets=default_brackets):
    for key in tax_brackets:
        if tax_brackets[key][0] <= salary <= tax_brackets[key][1]:
            output = key * salary
    
    return output

## Debugging

**Debugging Q1**.

def count_consonants(input_string):
    out = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in input_string:
        char = char.lower()
        
        if char not in vowels:
            if char not in out:
                out[char] = 1
            else:
                out[char] += 1
    return out

**Debugging Q2**. 

def new_encrypt(input_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    output_string = ''

    for char in input_string:
        char = char.upper()
        if char in alpha:
            position = alpha.find(char)
            output_string += reverse_alpha[position]
        else:
            output_string = None
            break
        
    return output_string

**Debugging Q3**

def growth_rate(this_year, last_year):
    return ((this_year - last_year)/last_year) * 100