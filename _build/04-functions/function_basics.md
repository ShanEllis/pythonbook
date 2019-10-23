---
redirect_from:
  - "/04-functions/function-basics"
interact_link: content/04-functions/function_basics.ipynb
kernel_name: python3
title: 'Function Basics'
prev_page:
  url: /04-functions/functions
  title: 'Functions'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Function Basics

So far, we've introduced a number of data types (integers, floats, lists, dictionaries, etc) and code constructs (conditionals and loops). Here, we'll introduce **functions**, which provide your code with seemingly infinite flexibiltiy and reusability once mastered.

We'll discuss how to define a function, using `def`, how to get that function to `return` important information, how to specify input parameters to the function you define, and discuss how functions have a special, separate namespace.

## Functions

Functions are a way to write a few lines of code to accomplish a goal that can be reused over and over again, carrying out the *same operations* on *different inputs*. 

<div class="alert alert-success">
A function is a re-usable piece of code that performs operations on a specified set of variables, and returns the result.
</div>

You've been *using* functions without us really discussing it. For example, `type()` is a function that takes an input (a variable whose type you want to know). The function always carries out the same operation - it determines the input variable's type, and returns that information to the viewer. *But*, it can take any variable as input. So, the inputs differ, but the procedure (what `type` does behind the scenes) remains the same.



{:.input_area}
```python
# you've seen functions before
my_var = [3, 4, 5]
type(my_var)
```





{:.output .output_data_text}
```
list
```



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



{:.input_area}
```python
# define a function: print_value
# num is a parameter for the function
def print_value(num):
    
    # do some operation
    print(num)
```


All the code above has done is define (or create) the function. We haven't yet *used* the function. 

To use - or execute - this function, meaning, to get it to actually print out the `num` provided, we first call the function name `print_value()` and then provide a value to the parameter `num` within the parentheses.

In the example below, we provide the value '6' as the input parameter `num`. 

This means that when the code executes, `num` refers to the value '6'. Accordingly, upon execution, the function prints the value stored in `num` - 6:



{:.input_area}
```python
# excecute a function by calling function by name
# adding input within parentheses
print_value(num = 6)
```


{:.output .output_stream}
```
6

```

Note that this function can be equivalently called without specifying `num =`. The function execution below is equivalent to the example above:



{:.input_area}
```python
# equivalent function call
# without specifying parameter
print_value(6)
```


{:.output .output_stream}
```
6

```

##  `return` statements

When this function executes, the code within the function runs using the specified input. The code within this function says to `print()` the variable. 

However, what if we wanted to *store* that output for use later. What if we wanted to store the value '6'?

Well, as the function is *currently* defined, we are unable to do that because currently the function *only* prints the value. It does not store and return it:

If we try to store the output from the function in a new variable `new_var`. As the function is currently defined, nothing is stored and returned from the function. The first line of code `prints()` the input value 6. The second line of code (`print(new_var)`), returns 'None'. 



{:.input_area}
```python
## why is it printing None?
## lets look at return below
new_var = print_value(6)
print(new_var)
```


{:.output .output_stream}
```
6
None

```

All this function is doing currently is printing the input. It's not actually *storing* any new information. To do that, we need to use `return`.

Here we define a function `return_value`. As with the previous `print_value()` function, it takes `num` as an input parameter. 

However, within the body of the function, we now store the input parameter `num` in the variable `output` and then **`return`** the variable `output`.



{:.input_area}
```python
# improving that function using return
def return_value(num):
    
    # do some operation
    output = num
    
    # return an answer
    return output
```


Remember that the code above defines the function. It does *not* execute it. 

To do that, we call the function name `return_value` and provide a value to the input parameter `num`:



{:.input_area}
```python
# excecute that function
return_value(6)
```





{:.output .output_data_text}
```
6
```



The output appears similar to what we saw with the `print_value()` function; however, we'll notice the difference with this new function when we try to assign the output to a variable:



{:.input_area}
```python
# execute function but assign output 
# store that output in variable new_val
new_val = return_value(6)
print(new_val)
```


{:.output .output_stream}
```
6

```

Now, the output returned from the function `return_value(6)` can be stored in `new_val`. When we print the contents of this variable, it now stores the output, thanks to the use of `return` within the function!

## Multiple Input Parameters

So far, the functions we've defined have only printed out the input provided to the function. That's not very practical. Typically functions carry out a meaningul operation. To demonstrate this, let's generate a function that takes two values as its input parameters, adds them together, and then returns the sum of the values as its output.

We'll call this function `add_two_numbers`:



{:.input_area}
```python
# define function
def add_two_numbers(num1, num2):
    
    # Do some operations on the input variables
    answer = num1 + num2
    
    # Return the answer
    return answer
```


Notice in the function defined above that there are two input parameters specified within the function - `num1` and `num2`. 

Within the body of the function, we store the addition of these two parameters in `answer` and `return` that variable.

With the code above, `add_two_numbers` has been defined. 

To execute that function, we will call the function and provide it with two input values, one for each of its required input parameters:



{:.input_area}
```python
# execute function
add_two_numbers(-1, 4)
```





{:.output .output_data_text}
```
3
```



Since this function includes a `return` statement, we can store the output of that function in a variable (here: `output`), allowing us to use the output from the function elsewhere in our code.



{:.input_area}
```python
# Execute our function again, on some other inputs
output = add_two_numbers(-1, 4)
print(output)
```


{:.output .output_stream}
```
3

```

## Multiple Operations

Further, we aren't limited to a single operation within a user-defined function. We can use multiple operations and all of the concepts we've used previously (including, for example, loops and conditionals).

For example, here we define a function called `even_odd`. It takes a single input parameter `value`.

Within the body of the function we use conditionals to determine `if` the input parameter value is even (`value % 2 == 0`). If even, the function stores 'even' in the variable `out`. Otherwise (`else`) it stores 'odd' in the variable `out`.

This variable `out` is `return`-ed.



{:.input_area}
```python
# determine if a value is even or odd
# and return that value
def even_odd(value): 
    if (value % 2 == 0): 
        out = 'even'
    else: 
        out = 'odd'
    
    return out
```


Upon execution, the function determines whether the input variable (here, `value = -1`) is even or odd, `return`ing that information:



{:.input_area}
```python
# Execute our function
even_odd(-1)
```





{:.output .output_data_text}
```
'odd'
```



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



{:.input_area}
```python
def even_odd(value): 
    if (value % 2 == 0): 
        out = 'even'
    else: 
        out = 'odd'
    
    return out
```


This means that any variables created in a notebook outside of a function as you write code are *not* usable within the defined function. 

This is what allows functions to be indpendent and self-contained pieces of code. This means that if you created a variable called `my_fav_variable` outside of the function, you *cannot* use or refer to that variable within a function because `my_fav_variable` is in a *separate namespace*.

Previously, we noted that within a Jupyter notebook, you can check the variables currently defined using `%whos`:



{:.input_area}
```python
# Remember, you can check defined variables with `%whos`
%whos
```


{:.output .output_stream}
```
Variable          Type        Data/Info
---------------------------------------
add_two_numbers   function    <function add_two_numbers at 0x10e0ee8c8>
even_odd          function    <function even_odd at 0x10e0df598>
my_var            list        n=3
new_val           int         6
new_var           NoneType    None
output            int         3
print_value       function    <function print_value at 0x10e0b1ae8>
return_value      function    <function return_value at 0x10e0db7b8>

```

This returns all the variables created and stored in your *global* namespace. These are available for use in operations in your notebook.

However, each function *only* has access to the variables defined within the function or passed in as variables.

To determine what variables a function has access to, we'll create a function called `check_function_namespace()`. This takes an input and uses the  `locals()` function to return information about what variables the function has access to:



{:.input_area}
```python
def check_function_namespace(function_input):
    # Check what is defined and available inside the function
    print(locals())
```


When we provide `check_function_namespace()` with the value '1' as its input, it returns that the *only* variable it has access to is the input variable '1'.



{:.input_area}
```python
# Functions don't `see` everything
check_function_namespace(1)
```


{:.output .output_stream}
```
{'function_input': 1}

```

When we provide `check_function_namespace()` with the value `True` as its input, it returns that the *only* variable it has access to is the input variable `True`. Note that it no longer has access to the value '1', as that was *not* passed in as an input on this execution of hte function.



{:.input_area}
```python
# Functions don't `see` everything
check_function_namespace(True)
```


{:.output .output_stream}
```
{'function_input': True}

```

The logic follows that if you pass two inputs into the function, the function will have access to both inputs, but the fact remains that those are the *only* variables to which the function has access. It cannot access the other variables stored outside the function in the global namespace:



{:.input_area}
```python
# using two different inputs to a function
def check_function_namespace2(function_input, other_name):
    # Check what is defined and available inside the function
    print(locals())
```




{:.input_area}
```python
# returning what each input is storing
check_function_namespace2(1, True)
```


{:.output .output_stream}
```
{'other_name': True, 'function_input': 1}

```

Names defined inside a function only exist within the function.

For example, if we define a global variable `my_var` and store a string in that variable:



{:.input_area}
```python
my_var = 'I am a variable'
```


The above line of code creates the variable `my_var`, storing 'I am a variable' in that varaible in the global namespace.

Now, if we run our check_function_namespace, and pass that variable into the function, the function will have access to that variable:



{:.input_area}
```python
check_function_namespace(my_var)
```


{:.output .output_stream}
```
{'function_input': 'I am a variable'}

```

*But*, if we pass a different variable into that function, `my_var` is no longer available within the function, as it was not passed into the function upon execution.



{:.input_area}
```python
check_function_namespace('new string')
```


{:.output .output_stream}
```
{'function_input': 'new string'}

```

Regardless of whether or not the variable is available for use within the function, `my_var` still exists in the global namespace:



{:.input_area}
```python
print(my_var)
```


{:.output .output_stream}
```
I am a variable

```

Given all of the above discussion about namespaces, it logically follows that a variable of the same name can exist in the global namespace *and* within a function, with each storing different information.

This can be confusing when reading code, so it's best to avoid these situations when writing code and choosing variable names, but it's important to understand that it is logically possible.

To demonstrate this point, let's define a function called `change_var`. This function takes an input variable `my_var`. Within the function it stores 'I am something else' in `my_var` and prints 'Inside function:' and the value stored in `my_var` within the function:



{:.input_area}
```python
def change_var(my_var):
    my_var = 'I am something else'
    print('Inside function: \t\t', my_var)
```


Remember, that we've already created `my_var` in the global namespace:



{:.input_area}
```python
# my_var in the global namespace
my_var
```





{:.output .output_data_text}
```
'I am a variable'
```



Now, when we execute our `change_var()` function, we see that despite passing `my_var` (which stores 'I am a variable') into the function, within the function, `my_var` gets defined as the string 'I am something else':



{:.input_area}
```python
# my_var within the function
change_var(my_var)
```


{:.output .output_stream}
```
Inside function: 		 I am something else

```

But, because the namespace within a function is separate, this change only occurs within the function. The value stored in `my_var` in the global namespace (outside the function) remains unchanged:



{:.input_area}
```python
# my_var in the global namespace remains unchanged
my_var
```





{:.output .output_data_text}
```
'I am a variable'
```



To summarize, `my_var` outside the function remains unchanged, only storing 'I am somthing else' within the`change_var()` function:



{:.input_area}
```python
print('Outside, before function: \t', my_var)
change_var(my_var)
print('Outside, after function: \t', my_var)
```


{:.output .output_stream}
```
Outside, before function: 	 I am a variable
Inside function: 		 I am something else
Outside, after function: 	 I am a variable

```

## Exercises

1. **Given the function here, what would `print(remainder(12, 5) + remainder(2, 2))` return?**

```python
def remainder(number, divider):
    
    r = number % divider
    
    return r
```

2. **Write a function `greet` that takes the parameter `name`. Inside the function, concatenate 'Hello', the person's name, and 'Good morning!". Assign this to `output` and return `output`.**

AVOCADO - need more exercises here!
