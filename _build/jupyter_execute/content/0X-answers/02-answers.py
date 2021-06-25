# Answers: The Basics

Provided here are answers to the practice questions at the end of "The Basics".

## Variables

**Variables Q1**.

# actual values stored will differ
var_float = 9.29
var_str = 'cogs18'
var_bool = False
var_tuple = (1,2,3)
var_dict = {'a':1}

**Variables Q2**.

scenario_A = 'tuple'
scenario_B = 'list'
scenario_C = 'dictionary'
scenario_D = 'dictionary'

## Operators

**Operators Q1**.

var_even = (var_high + var_low) % var_mid
var_odd = (var_mid ** var_low) // var_high

**Operators Q2**.

# specific values will differ
my_age = 31 
pres_age = 78

true_compar = my_age < pres_age
false_compar = pres_age == my_age

**Operators Q3**.

yes_member = current_holiday in spring_holidays
no_member = current_holiday not in spring_holidays

**Operators Q4**.

# actual operations will differ
var_odd = (9 + 2 - 1) % 3
var_even = 25 / 5 * 2 // 1
var_operator = var_odd ** var_even + 5

**Operators Q5**.

# actual operations will differ
true_var = (var_low < var_mid) or (var_high >= var_mid)
false_var = (var_mid != var_low) and (var_high < var_mid)


**Operators Q6**.

# actual variable creation will differ
comp_a = 7 > 6 and 6 < 7
comp_b = 3 <= 3 or 4 <= 3
comp_c = 3 == 3 and not 3 != 3

**Operators Q7**.

# actual operations will differ
memb_a = 'love' in my_string
memb_b = 'Exercises' not in my_list

## Conditionals

**Conditionals Q1**.

comparison_name = 'Shannon'

### BEGIN SOLUTION
# my_name will differ based on person writing code
my_name = 'Shannon'

if len(my_name) < len(comparison_name):
    output = 'shorter'
elif len(my_name) > len(comparison_name):
    output = 'longer'
elif len(my_name) == len(comparison_name):
    output = 'same length'
else:
    print('something has gone awry')

## Topics Synthesis

**Synthesis Q1**.

# actual values stored will differ
var_cat = 'cogs' + '18'
var_sum = 9 + 29

**Synthesis Q2**.

# actual values stored will differ
var_int = 10
var_float = 1.0 
var_combined = var_int + var_float

**Synthesis Q3**.

# actual variable creation will differ
var_a = 7.3
var_b = 6 == 6 and 3 <= 4
var_c = (6 + 3) * 4

**Synthesis Q4**.

# actual values stored will differ
var_a = 'abcd'
var_b = 6.0
var_c = (1,2,3)