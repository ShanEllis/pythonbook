# Functions 

So far, we've introduced a number of data types (integers, floats, lists, dictionaries, etc) and code constructs (conditionals and loops). Here, we'll introduce **functions**, which provide your code with seemingly infinite flexibiltiy and reusability once mastered.

We'll discuss how to define a function, using `def`, how to get that function to `return` important information, how to specify input parameters to the function you define, and discuss how functions have a special, separate namespace.

## Functions 

Functions are a way to write a few lines of code to accomplish a goal that can be reused over and over again, carrying out the *same operations* on *different inputs*. 

<div class="alert alert-success">
A function is a re-usable piece of code that performs operations on a specified set of variables, and returns the result.
</div>

You've been *using* functions without us really discussing it. For example, `type()` is a function that takes an input (a variable whose type you want to know). The function always carries out the same operation - it determines the input variable's type, and returns that information to the viewer. *But*, it can take any variable as input. So, the inputs differ, but the procedure (what `type` does behind the scenes) remains the same.

# you've seen functions before
my_var = [3, 4, 5]
type(my_var)

As discussed previously, copy and pasting the same or very similar bits of code over and over again is to be avoided. **Loops** were introduced as one way to avoid this. **Functions** are another! Learning how and when to write functions will make your code easier to read, easier to bug, and easier to use. 

## Modular Programming

Specifically, functions are helpful when programming modularly. **Modular programming** is an approach to programming that focuses on building programs from indendent modules ('pieces'). While these individual pieces can all fit together to accomplish a larger goal, each piece *can* operate independently.

Functions facilitate this approach to programming in the following ways:
- Functions allow us to flexibly re-use pieces of code
- Each function is independent of every other function, and other pieces of code
- Functions are the building blocks of programs, and can be flexibly combined and executed in specified orders
    - This allows us to build up arbitrarily complex, well-organized programs

## User-defined Functions

While you've *used* other functions (`len()`, `type()`, `print()`) previously, we've yet to discuss the fact that you can write your *own* functions to carry out the procedures you want them to carry out. 

To define (create) a **user-defined function**, you'll use `def`.

This will always take hte general form:

```python
def function_name(input_parameters):
    # code with function operation
```

As the creator of the function, you'll specify the `function_name`, determine what variable names to use for your `input_parameters`, and write the code within your function to carry out the desired operations on your `input_parameters`.

For example, the simplest function would be one that took an input and printed that input out. It's not a very *interesting* or *helpful* function, but it demonstrates the idea of how these work.

Here, we define a function called `print_value` that takes `num` as an input parameter.

Within the function definition we see the line of code: `print(num)`. Notice that `num` refers to the input parameter specified within the parentheses after `print_value`. 

# define a function: print_value
# num is a parameter for the function
def print_value(num):
    
    # do some operation
    print(num)

All the code above has done is define (or create) the function. We haven't yet *used* the function. 

To use - or execute - this function, meaning, to get it to actually print out the `num` provided, we first call the function name `print_value()` and then provide a value to the parameter `num` within the parentheses.

In the example below, we provide the value '6' as the input parameter `num`. 

This means that when the code executes, `num` refers to the value '6'. Accordingly, upon execution, the function prints the value stored in `num` - 6:

# excecute a function by calling function by name
# adding input within parentheses
print_value(num = 6)

Note that this function can be equivalently called without specifying `num =`. The function execution below is equivalent to the example above:

# equivalent function call
# without specifying parameter
print_value(6)

##  `return` statements

When this function executes, the code within the function runs using the specified input. The code within this function says to `print()` the variable. 

However, what if we wanted to *store* that output for use later. What if we wanted to store the value '6'?

Well, as the function is *currently* defined, we are unable to do that because currently the function *only* prints the value. It does not store and return it:

If we try to store the output from the function in a new variable `new_var`. As the function is currently defined, nothing is stored and returned from the function. The first line of code `prints()` the input value 6. The second line of code (`print(new_var)`), returns 'None'. 

## why is it printing None?
## lets look at return below
new_var = print_value(6)
print(new_var)

All this function is doing currently is printing the input. It's not actually *storing* any new information. To do that, we need to use `return`.

Here we define a function `return_value`. As with the previous `print_value()` function, it takes `num` as an input parameter. 

However, within the body of the function, we now store the input parameter `num` in the variable `output` and then **`return`** the variable `output`.

# improving that function using return
def return_value(num):
    
    # do some operation
    output = num
    
    # return an answer
    return output

Remember that the code above defines the function. It does *not* execute it. 

To do that, we call the function name `return_value` and provide a value to the input parameter `num`:

# excecute that function
return_value(6)

The output appears similar to what we saw with the `print_value()` function; however, we'll notice the difference with this new function when we try to assign the output to a variable:

# execute function but assign output 
# store that output in variable new_val
new_val = return_value(6)
print(new_val)

Now, the output returned from the function `return_value(6)` can be stored in `new_val`. When we print the contents of this variable, it now stores the output, thanks to the use of `return` within the function!

## Multiple Input Parameters

So far, the functions we've defined have only printed out the input provided to the function. That's not very practical. Typically functions carry out a meaningul operation. To demonstrate this, let's generate a function that takes two values as its input parameters, adds them together, and then returns the sum of the values as its output.

We'll call this function `add_two_numbers`:

# define function
def add_two_numbers(num1, num2):
    
    # Do some operations on the input variables
    answer = num1 + num2
    
    # Return the answer
    return answer

Notice in the function defined above that there are two input parameters specified within the function - `num1` and `num2`. 

Within the body of the function, we store the addition of these two parameters in `answer` and `return` that variable.

With the code above, `add_two_numbers` has been defined. 

To execute that function, we will call the function and provide it with two input values, one for each of its required input parameters:

# execute function
add_two_numbers(-1, 4)

Since this function includes a `return` statement, we can store the output of that function in a variable (here: `output`), allowing us to use the output from the function elsewhere in our code.

# Execute our function again, on some other inputs
output = add_two_numbers(-1, 4)
print(output)

## Multiple Operations

Further, we aren't limited to a single operation within a user-defined function. We can use multiple operations and all of the concepts we've used previously (including, for example, loops and conditionals).

For example, here we define a function called `even_odd`. It takes a single input parameter `value`.

Within the body of the function we use conditionals to determine `if` the input parameter value is even (`value % 2 == 0`). If even, the function stores 'even' in the variable `out`. Otherwise (`else`) it stores 'odd' in the variable `out`.

This variable `out` is `return`-ed.

# determine if a value is even or odd
# and return that value
def even_odd(value): 
    if (value % 2 == 0): 
        out = 'even'
    else: 
        out = 'odd'
    
    return out

Upon execution, the function determines whether the input variable (here, `value = -1`) is even or odd, `return`ing that information:

# Execute our function
even_odd(-1)

## Function Properties

So far, we've discussed a few properties of functions:

- Functions are defined using `def` followed by `:`, which opens a code-block that comprises the function
    - Running code with a `def` block *defines* the function (but does not *execute* it)
- Functions are *executed* using parentheses - `()`
    - This is when the code inside a function is actually run
- Functions use the special operator `return` to exit the function, passing out any specified variables
- When you use a function, you can assign the output to a variable

However, there are additional important properties that we have have encountered, but have not yet explicitly discussed:

- Functions have their own **namespace**
    - They only have access to variables explicitly passed into them
- Inside a function, there is code that performs operations on the available variables

## Function Namespaces

We previously defined the namespace as follows:

<div class="alert alert-success">
The <b>namespace</b> is the 'place' where all your currently defined code is declared - all the things you have stored in active memory. 
</div>

So, as you execute code in a notebook, you generate variables. These variables become available within the namespace.

That is all true; however, importantly, functions have a **separate namespace**. The only variables available within a function are the variables assigned within it and those passed in as input parameters.

For example, with this `even_odd()` function we defined previoulsy, the only variables available within the function are `value` (which is passed in as an input parameter) and `out` (which is defined within the function itself).

def even_odd(value): 
    if (value % 2 == 0): 
        out = 'even'
    else: 
        out = 'odd'
    
    return out

This means that any variables created in a notebook outside of a function as you write code are *not* usable within the defined function. 

This is what allows functions to be indpendent and self-contained pieces of code. This means that if you created a variable called `my_fav_variable` outside of the function, you *cannot* use or refer to that variable within a function because `my_fav_variable` is in a *separate namespace*.

Previously, we noted that within a Jupyter notebook, you can check the variables currently defined using `%whos`:

# Remember, you can check defined variables with `%whos`
%whos

This returns all the variables created and stored in your *global* namespace. These are available for use in operations in your notebook.

However, each function *only* has access to the variables defined within the function or passed in as variables.

To determine what variables a function has access to, we'll create a function called `check_function_namespace()`. This takes an input and uses the  `locals()` function to return information about what variables the function has access to:

def check_function_namespace(function_input):
    # Check what is defined and available inside the function
    print(locals())

When we provide `check_function_namespace()` with the value '1' as its input, it returns that the *only* variable it has access to is the input variable '1'.

# Functions don't `see` everything
check_function_namespace(1)

When we provide `check_function_namespace()` with the value `True` as its input, it returns that the *only* variable it has access to is the input variable `True`. Note that it no longer has access to the value '1', as that was *not* passed in as an input on this execution of hte function.

# Functions don't `see` everything
check_function_namespace(True)

The logic follows that if you pass two inputs into the function, the function will have access to both inputs, but the fact remains that those are the *only* variables to which the function has access. It cannot access the other variables stored outside the function in the global namespace:

# using two different inputs to a function
def check_function_namespace2(function_input, other_name):
    # Check what is defined and available inside the function
    print(locals())

# returning what each input is storing
check_function_namespace2(1, True)

Names defined inside a function only exist within the function.

For example, if we define a global variable `my_var` and store a string in that variable:

my_var = 'I am a variable'

The above line of code creates the variable `my_var`, storing 'I am a variable' in that varaible in the global namespace.

Now, if we run our check_function_namespace, and pass that variable into the function, the function will have access to that variable:

check_function_namespace(my_var)

*But*, if we pass a different variable into that function, `my_var` is no longer available within the function, as it was not passed into the function upon execution.

check_function_namespace('new string')

Regardless of whether or not the variable is available for use within the function, `my_var` still exists in the global namespace:

print(my_var)

Given all of the above discussion about namespaces, it logically follows that a variable of the same name can exist in the global namespace *and* within a function, with each storing different information.

This can be confusing when reading code, so it's best to avoid these situations when writing code and choosing variable names, but it's important to understand that it is logically possible.

To demonstrate this point, let's define a function called `change_var`. This function takes an input variable `my_var`. Within the function it stores 'I am something else' in `my_var` and prints 'Inside function:' and the value stored in `my_var` within the function:

def change_var(my_var):
    my_var = 'I am something else'
    print('Inside function: \t\t', my_var)

Remember, that we've already created `my_var` in the global namespace:

# my_var in the global namespace
my_var

Now, when we execute our `change_var()` function, we see that despite passing `my_var` (which stores 'I am a variable') into the function, within the function, `my_var` gets defined as the string 'I am something else':

# my_var within the function
change_var(my_var)

But, because the namespace within a function is separate, this change only occurs within the function. The value stored in `my_var` in the global namespace (outside the function) remains unchanged:

# my_var in the global namespace remains unchanged
my_var

To summarize, `my_var` outside the function remains unchanged, only storing 'I am somthing else' within the`change_var()` function:

print('Outside, before function: \t', my_var)
change_var(my_var)
print('Outside, after function: \t', my_var)

## Default Values

So far, we've seen that functions can take inputs, but we haven't discussed how to set a default value for an input parameter. It's helpful to set default values for cases when there is a value your input parameter will take most of the time.

<div class="alert alert-success">
Function parameters can also take default values. This makes some parameters optional, as they take a default value if not otherwise specified.
</div>

For example, if you wrote a function called `exponentiate`, you may expect that *most* of the time, people will want to square a value. However, you want to leave users the *option* to be able to raise a value to a different power. This is a case where you would set the default parameter value to square the input. To do this, you assign a value within the parentheses after the function name (within the function definition). 

# Create a function, that has a default values for a parameter
def exponentiate(number, exponent = 2):    
    return number ** exponent

In this function, we see there are two input parameters: `number` and `exponent`. `exponent` here takes the default value '2', as it is assigned within the function definition.

Within the function, `number` is raised to the power `exponent`. This means, that under default conditions, the `number` provided will be squared and returned:

# Use the function, using default value
exponentiate(2)

As seen above, when we pass the value 2 to the `number` parameter, the function returns $2^2$, or 4. Notice that when a default value is specified, if you want the function to use that default value provided, you do not have to specify any inputs for that parameter.

However, if you want to use a *different* value for your `exponent`, you still have that option. You could so so using the following:

# Call the function, over-riding default value with something else
# python assumes values are in order of parameters specified in definition
exponentiate(2, 3)

Notice here that Python returns 8 as it has raised $2^3$. Python in this case assumes values are provided in the order of the parameters specified within the function definition, `number` then `exponent`.

However, an equivalent function call would be as you see here:

# you can always state this explicitly
exponentiate(number = 2, exponent = 3)

In each of the two previous function calls, Python uses the `exponent` value 3, specifed during the function call. This overrides the default value provided (2), using the exponent value provided instead (3).

## Positional vs. Keyword Arguments

In the previous example we demonstrated that it is possible to use positional arguments (`exponentiate(2, 3)`) or keyword arguments (`exponentiate(number = 2, exponent = 3)`)when calling a function without explicitly explaining what's going on.

Here, we'll explain exactly what is meant by **positional** and **keyword** arguments.

<div class="alert alert-success">
Arguments to a function can be indicated by either position or keyword.
</div>

When we call a function and ask Python to use the position or order of the values provided, we're using **positional arguments**. Python will always use the inputs in the order specified in the function definition.

As `exponentiate` was defined as follows:

```python
def exponentiate(number, exponent = 2):    
    return number ** exponent
```

we know that in the following function call, '2' refers to the `number` (the first argument in the function definition) and '3' to the `exponent` (the second argument in the function definition).

# Positional arguments use the position to 
# infer which argument each value relates to
exponentiate(2, 3)

Equivalently and more explicitly, keywords can be used when calling a function by including the parameter, the assignment operator (`=`), and the value you'd like to use for your function call. 

As noted previously, this function call below is equivalent to `exponentiate(2, 3)`; however, you can see that it's clearer to readers of your code as to what's going on. It can be beneficial when writing code to use keyword arguments to make it crystal clear to those reading your code what's going on:

# Keyword arguments are explicitly named as to 
# which argument each value relates to
exponentiate(number = 2, exponent = 3)

One important point about keyword arguments it that their order does *not* matter when calling the function. The following is equivalent to the example above.

Now, again, to make it easier on readers, it's best to keep things in the order of the function documentation; however, know that Python will know how to handle the input if you change the order of your input variables when using keyword arguments:

exponentiate(exponent = 3, number = 2)

Finally for now, we'll note that you *cannot* mix keyword and positional arguments. Once you specify a keyword or use a positional argument, you'll have to use that for the remainder of your function call.

As such the following code would produce an error as a keyword (`number = 2`) and positional argument (`3`) are attempted to be used in the same function call: 

# Note: once you have a keyword argument, 
# you can't have other positional arguments afterwards
# this cell will produce an error
exponentiate(number = 2, 3)

## Docstrings

So far, we've mainly focused on writing code that will execute; however, it's important that your code executes *and* that other people know how to use it. We'll talk more extensively about documentation later, but we'll introduce one piece of documentation now: the **docstring**.

Docstrings allow you to include documentation within the function itself informing others of what the function does.

Docstrings are specified by text within triple quotes in the first line after your function is defined.

For example, in the example here, `"""return list of dictionary values"""` is the docstring:

def list_dictionary(my_dictionary):
    """return list of dictionary values"""
    
    # create empty list
    output = []
    
    # loop through dictionary input
    for item in my_dictionary:
        value = my_dictionary[item]
        output.append(value)
    
    return output

To access this documentation within a Jupyter notebook, you can now use the familiar help (`?`) after the name of the function: `list_dictionary?`.

## Exercises

Q1. **Given the function here, what would `print(remainder(12, 5) + remainder(2, 2))` return?**

```python
def remainder(number, divider):
    
    r = number % divider
    
    return r
```

Q2. **Write a function `greet` that takes the parameter `name`. Inside the function, concatenate 'Hello', the person's name, and 'Good morning!". Assign this to `output` and return `output`.**
<br>

Q3. **Update your `greet` function to include an informative docstring**.
<br>

Q4. **Given the following, what would `print_numbers(5, 12.2)` print?**

```python
an_int = 2
a_float = 11.5

def print_numbers(an_int, a_float):
    print(an_int, ',', a_float)
```

Q5. **Given the following function, what would `string_manipulator('abcde')` return?**

```python
def string_manipulator(string):
    
    output = ''
    for char in string:
        if char == 'a' or char == 'e':
            char = 'z' 
        output = output + char
    
    return output
```

Q6. **Given the following function, what would `exponentiate(exponent = 2, number = 4)` return**?

```python
def exponentiate(number, exponent = 2):    
    return number ** exponent
```