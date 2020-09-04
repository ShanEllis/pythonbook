# Loops

We previously discussed conditionals as a way to control the flow of your code. Here, we introduce the concept of loops. We'll discuss `while` loops and `for` loops and introduce how to incorporate these into your code.

Specifically, **loops** are a procedure utilized in code to repeat a piece of code more than once.

<div class="alert alert-success">
A <b>loop</b> is a procedure to repeat a piece of code.
</div>

More specifically, loops help you to avoid copy and pasting similar pieces of your code over and over again throughout your code. It's best to avoid copying and pasting code to (1) make your code more readable to yourself and others and (2) to avoid errors when debugging. By avoiding copying and pasting, when you make a change to improve your code, you only have to make that edit in one single location rather than in every place where the code has been copy and pasted.

This means that when it comes to repetitive actions in code, if you find yourself copying + pasting, rethink your strategy. Loops are one way to avoid this. We'll discuss other approaches later on.

## Why loops?

Imagine you wanted to send an email to all the email addresses in your list.

Well, if you only had two emails in your list, you could specify who the email is being sent to using something like what we see here:

email_list = ['friend@yahoo.com', 'them@bing.com']

email = email_list[0]
    # send email

email = email_list[1]
    # send email

But, what if you had 100 emails or 1000 emails? Going through and changing the index to refer to the individual in your list of emails would take a long time and would be prone to error. 

This is when you want to turn to loops!

## `while` Loops

A `while` loop is a procedure to use that will repeat the code within the loop for as long as a condition is met. The loop will terminate (stop running the code) once the condition is no longer met.

<div class="alert alert-success">
A <b>while loop</b> is a procedure to repeat a piece of code while some condition is still met. 
</div>

While loops always have the structure:

```python
while condition:
    # Loop contents
```

`while` is followed by a condition. The condition is then followed by a colon (`:`). The contents within the loop - the code that you want to execute as long as the condition is met are on the subsequent lines and are all indented, visibly indicating that those lines of code are part of the while loop.

Note that `condition` can change - this is what determines whether your `while` loop continues to run. While `condition is `True`, the code contents will execute. The code within the loop will repeat until condition is no longer `True`. 

Here, we have an example of a while loop, where `number` initially stores the value '-5'. 

Then we have a `while` loop where the condition looks to see if `number` is less than (`<`) the number 0. This means that as long as `number` is negative, the contents within the `while` loop will execute.

Within the `while` loop, the current value stored in `number` will `print()` *and* the value stored in `number` will increase by 1. 

Thus, the first time through the loop `number` will store -5. The second time through, it will increase by one to store the value -4. This will continue and the loop will continue to run, printing the current value stored in `number` each time through the loop. 

However, once `number` stores the value 0, the condition `number < 0` will no longer be met. At this point, the `while` loop will stop executing, terminating the loop.

number = -5

while number < 0:
    print(number)
    number = number + 1

Note that `while` loops can be combined with the other code constructs you've previously learned - such as conditionals.

Here we see a `while` loop with a nested `if` statement.

keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1
    
    if counter > 2:
        keep_looping = False

print(counter)

In this code, two variables are created: `keep_looping` which stores the boolean `True` and  `counter`, which stores the value '0' to start.

From there, the `while` loop will execute, as `keep_looping` is `True`.

Within the `while` loop, `counter` will increment by 1. The first time through the loop, `counter` will update to store '1'.

Then, the conditional `if` statement is encountered. At this point, `counter` stores the value 1, which is *not* greater than (`>`) 2, so the code within the conditional will *not* execute. 

The `while` loop will then enter its second iteration. `counter` will increase by 1 to store the value '2'. The conditional is still `False`, so the `while` loop will execute once again.

During its third iteration, `counter` will increase to store the value '3'. Now, the conditional statement evaluates as `True`, as the value 3 (stored in `counter`) *is* greater than 2. 

`keep_looping` now stores the value `False`. The `while` condition is no longer `True`, and the loop terminates.

Note that the final line of code here (the `print()` statement) is *not* indented. This indicates that it is *not* part of the `while` loop. This line only executes, printing the last value stored in `counter` (3) once the `while` loop terminates.

## `for` Loops

The second type of loop we'll discuss for controlling the flow of your code is a `for` loop. This procedure repeats code for every element in a collection. 

So if you have a list and want the same code to operate on every element in the list, you'll want to use a `for` loop.

<div class="alert alert-success">
A <b>for loop</b> is a procedure a to repeat code for every element in a sequence.
</div>

For example, here we create a list with three items. If we want to carry out some operation on each element in this list, we'll use a `for` loop.

The operation we'll carry out in this first example is simply to print each element of the list as it loops through the list.

What's most important in the code below is the use of the variable `my_item`. Note that this variable has *not* been previously defined. This variable is used to refer to each element in the list as the loop progresses.

# Define a list of items
list_of_items = ['A', True, 12]

# Loop across each element
for my_item in list_of_items:
     print(my_item)

More specifically, the first time through the `for` loop, `my_item` will refer to the first element in `list_of_items` - the string `'A'`. 

The code within the `for` loop specifies to `print(my_item)`. Thus, the information stored in `my_item` - the string `'A'` is printed.

With the first iteration of the loop, the `for` loop continues on, repeating the code within the `for` loop on the second element in the list - `True`. Now, `my_item` refers to the second element in the list - `True`. So when `print(my_item)` is encountered, the value `True` is printed. 

The third time through the loop, `my_item` refers to the third element in the list - the value '12'. Thus, that is printed when `print(my_item)` is encountered.

After this third iteration, the `for` loop has reached the end of the list. Once the end of the collection the `for` loop is iterating through is reached, the execution of the loop will terminate.

After this loop executes, the value stored in `my_item` will be the last value stored in `my_item` in the loop - the last element of the list.

We can use `print(my_item)` to verify the contents stored in this variable:

# my_item exists outside the loop
print(my_item)

Above, we see that even though `my_item` was created and utilized within the `for` loop, it exists after the loop executes, storing whatever the last value stored during the `for` loops execution was.

### Looping through strings

Note that loops are not used exclusively with strings. You can loop through all of the collections we've discussed previously - strings, tuples, and dictionaries.

When we loop through strings, each character in the string is iterated through until the end of the string is encountered:

# Loop across items in a string
for char in 'python': 
    print(char)

### Looping through dictionaries

Further, when we loop through dictionaries, we iterate across the keys. To see what we mean, let's re-create a dictionary we've seen previously for use in this example:

student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : 'ada@analyticengine.com',
    'Alan Turing' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}

In the example below, `person` refers to the keys in the dictionary. So, the first time through the loop, `person` will refer to the first person in the `student_emails` dictionary - 'Betty Jennings'. The second time through, the second key, and so on and so forth:

# Loop over a dictionary loops across the keys
for person in student_emails:
    print(person)

This can be combined with indexing, if you want to see the values stored in the keys. Here, instead of printing the key, using `person`, we can **index** from the `student_emails` dictionary, which returns the values stored in the keys.

# Loop over a dictionary loops across the keys
#   Inside the loop, you can use the key to access the associated value
for person in student_emails:
    print(student_emails[person])

In each of these scenarios, as we loop through a dictionary, we are using `person` to refer to the keys in the `student_emails` dictionary. Within the `for` loop, we can *refer* to `person` to specify the *key* in the dictionary. 

## `range`

As you begin to write loops, you'll become familiar with the `range` operator, which creates a range of numbers. This operator is frequently used with loops. 

<div class="alert alert-success">
<code>range</code> is an operator to create a range of numbers, that is often used with loops.
</div>

To demonstrate why `range` is helpful, consider looping over a list of integers from 0 to 4, inclusive. To do this using the tools we've discussed so far, you would use the following:

for ind in [0, 1, 2, 3, 4]:
    print(ind)

However, often we want to iterate across lists containing *many* more numbers. Typing each individual number out would become onerous and we'd likely make a typo.

Alternatively, we could use `range()`. `range` uses the same (`start`, `stop`, `step`) concept we used for indexing; however, the values are separated by commas when using range, rather than by colons (as we used for indexing).

The code below accomplishes the same procedure we saw above; however, instead of specifying each number in the list, we can use `range()` and specify the `start` and `stop` values. Recall that the `stop` value (here, 5) is *not* included in the range, just as the `stop` value specified in a slice was not included.

# Loop across a sequence of numbers, using range
for ind in range(0, 5):
    print(ind)

By including a `step` value, `range` further allows us to skip over values in the range, to, for example, only include even values, as we see here:

# Range, like indexing, is defined by 'start', 'stop', 'step'
for ind in range(2, 6, 2):
    print(ind)

## `continue`

Another helpful operator is `continue`. When encountered ina loop, `continue` specifies to jump ahead to the next iteration of a loop, regardless of the code below in the loop.

<div class="alert alert-success">
<code>continue</code> is a special operator to jump ahead to the next iteration of a loop.
</div>

For example, in this loop, when `item == 2`, `continue` is encountered, so the code skips to the top of the for loop, ignoring the `print(item)` statement below. However, for all other values in the range (when `item` is anything *other* than '2', `item` gets printed.

for item in range(0, 4):
    
    if item == 2:
        continue
    
    print(item)

This concept applies across the varies types of collections we've talked about previously. For example, here we are looping through a string, and `continue`-ing on when `char` stores the letter 'p' or 'y'. 

for char in 'love python': 
    
    if char == 'p' or char == 'y':
        continue
        
    print(char)

## `break`

Finally, `break` is a special operator that, when encountered will terminate the loop. Unlike `continue` which carries on immediately to the next iteration of the loop, `break`, when `break` is encountered, the whole loop terminates (stops executing)

<div class="alert alert-success">
<code>break</code> is a special operator to break out of a loop.
</div>

Using the example we saw above with `continue` but replacing `continue` with `break`, we see that once `item == 2` is `True`, `break` is encountered and the loop terminates. `item` never reaches the end of the list (the value 3) and thus that value never gets printed. 

for item in range(0, 4):
    
    if item == 2:
        break
    
    print(item)

The same concept applies for iterating through a string. Once `break` is encountered, the loop terminates immediately:

string = "love python"

for char in string: 
    if char == "p" or char == "y":
        break
        
    print(char)

## Exercises

Q1. **How many values will be output from this `while` loop before "The tea is cool enough." is printed?**

```python
temperature = 115
 
while temperature > 112: 
    print(temperature)
    temperature = temperature - 1

print('The tea is cool enough.')
```

Q2. **What will be the value of `counter` after this loop executes?**


```python
keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1
    
    if counter > 3:
        keep_looping = False

print(counter)
```

Q3. **What will the following loop print out?**

```python
my_lst = range(0, 5)

for item in my_lst[0:-1]:
    print(item + 1)
```

Q4. **How many values will be output from this `for` loop before it *first* prints "The tea is too hot!"?

```python
temperatures = [114, 115, 116, 117, 118]

for temp in temperatures: 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')

```

Q5. **How many values would this loop print and what would be the last value printed?**


```python
for ind in range(1, 10, 3):
    print(ind)
```

A) values printed: 3; last value: 7  
B) values printed: 3; last value: 9  
C) values printed: 4; last value: 9  
D) values printed: 7; last value: 7  
E) values printed: 7; last value: 9  

Q6. **What will be the value of `counter` after this code has executed?**

```python
counter = 0
my_lst = [False, True, False, True]

for item in my_lst:
    if item in my_lst:
        continue
    else:
        counter = counter + 1
```

Q7. **What will the following code print out**?

```python
number = 1

while True:
    if number % 3 == 0:
        break
    print(number)
    
    number = number + 1
```

A) 1  
B) 1 2  
C) 1 2 3  
D) Something else   
E) This code prints forever  

Q8. **For how many `temp` will output be printed from this for loop? (In other words, how many times in this for loop will something be printed out?)**

```python
for temp in range(114, 119): 
    
    if(temp < 116):
        continue
    elif(temp == 116):
        print('The tea is too hot!')
    else:
        break
```

Q9. **Store your name as a string in a variable called `my_name`. Write a loop that will loop through all the letters in `my_name` and count all the vowels in your name.**

Q10. **Write a loop that adds all the *odd* numbers between 1 and 1000 together.**