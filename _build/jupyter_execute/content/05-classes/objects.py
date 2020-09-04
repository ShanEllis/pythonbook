# Objects 

We'll get to *fully* understanding what this means, but, for now, take my word for it: **Everything in Python is an object**. There are objects we've covered so far, like integer-type objects and list-type objects. *But*, there are countless other types of objects in Python, with each object having special *attributes* and *methods* that make operationg on an object simpler.

In this chapter, we'll work with `date` and `datetime` objects to introduce the concepts of objects, object-oriented programming (OOP), and methods/attributes before we discuss how you can create your own object types in the next chapter.

## Object Motivation: Storing Dates

To motivate our thinking, consider how you might go about storing a date using the variable types we've discussed so far. You can likely think about a few possible approaches. Maybe you'd want to store the date as a string. And, while that is possible, you wouldn't be able to *operate* on that string. More specifically, if you tried to determine how many days there were between two dates stored as strings, you wouldn't be able to do it. That's not a property of strings.




# A date, stored as a string
date_string = '29/09/1988'
print(date_string)

In a similar vein, you could consider storing each compenent of your date as a separate element in a list. If stored as integers, you could slice this list and carry out operators on each integer, but the approach to determine the number of days between two lists of dates is not straightforward.


# A date, stored as a list of numbers
date_list = [29, 9, 1988]
date_list

Similar logic follows for other variable types we've discussed so far. It's _possible_ to _store_ the information using the variable types we've discussed thus far...

# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)

# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary

But, carrying out meaningful operations on a date with any of these variable types is _difficult_. This is where objects become very helpful! 

To formally define what an object is in Python. Objects are an organization of data (called **attributes**) and associated code that operates on taht data (which are specific functions defined on the objects directly, called **methods**).

Objects allow for information to be stored and operations to be carried out on them.

<div class="alert alert-success">
<b>Objects</b> are an organization of data (called <b>attributes</b>), with associated code to operate on that data (functions defined on the objects, called <b>methods</b>).
</div>

## Example Object: Date

While the standard library makes certain object types available to you, there are many other object types that exist within the Python ecosystem. To utilize these other object types, they must first be imported. We'll discuss the syntax for doing so in more detail shortly; however, for now, we'll just share how to do so for this example:

# Import a date object
from datetime import date

We'll now work create our first date type object! We'll do so by very explicitly first creating three variables, each of which stores an integer: `day`, `month`, and `year`:

# Set the data we want to store in our date object
day = 29
month = 9
year = 1988

We're now ready to define our first `date`-type object.

We do this using the following syntax:

# Create a date object
my_date = date(year, month, day)

Above we see that we call the object type `date(` and pass in the `year`, `month`, and `day` to create a `date`-type object, storing it in the variable `my_date`.

If we were to print the contents of the `date` type object, we would see that it stores the date '1988-09-29'.

print(my_date)

We can also see what the `type` of this variable is. Below, we see that `my_date` is a `datetime.date` object. We'll see now what *exactly* that means!

# Check what type of thing `my_date` is
type(my_date) 

## Attributes & Methods

<div class="alert alert-success">
Attributes and methods are accessed with a <code>.</code>, followed by the attribute/method name on the object. 
</div>

### `date` Attributes

Now that we've created a `date`-type object, we can delve into discussing exactly what that means.

First, `objects` have attributes. This allows for a particular object to store data, or information. When you access a particular attribute, you are specifying that you want to look up & return information about the object.

When you access an attribute for a particular object, you specify the object/variable name, followed by a `.` and then the name of the attribute you want to be returned.

In doing so, you are only asking Python to return the information to you. It is only returning information stored within the object. We say that attributes "maintain the object's state" because no _operations_ are being carried out. The information is just looked up and returned. (This is in contrast to methods, which we'll discuss in just a second.) 

In this first example, we're accessing the `day` attribute from the `my_date` object. Notice that the information is looked up and returned.

# Get the day attribute
my_date.day

The same syntax can be used for other pieces of information (attributes) stored in the `my_date` object.

# Get the month attribute
my_date.month

# Get the year attribute
my_date.year

### `date` Methods

Beyond the ability to look up information stored within an object, we have the ability to carry out operations directly on objects. This is where object definitions really shine! **methods** are _functions_ that *belong* to and operate on an object directly. 

Methods are what are going to allow us to operate on `date`-type objects in a meaningul way, which is something that is just not straightforward with any of the variable types we discussed prior to this chapter.

In contrast to attributes (which simply look up and return information already stored in the ojbect), methods modify the object's state. This means that there are operations carried out when a method is executed.

In this first example, we'll use the `weekday()` method. This is a method that takes the information stored in the `attributes` for a given `date`-type object, and determines the day of the week. 

Note that the syntax is similar to an attribute in that there is the object, followed by a `.` and then the method name. However, methods are executable functions that operate directly on an object. As such, there are parentheses after the method is called, indicating that it is executable. 

# Method to return what day of the week the date is
my_date.weekday()

The `weekday()` method returns a 0 for Mondays ....and a 6 for Sundays (with all of the other days returning integers between those two values, so, by using the `weekday()` method on our specified date, we determine that September 29th, 1988 was a Thursday.

While `weekday()` is a good method for introducing what a method is and what its syntax is, when working with dates, we ultimately really want to be able to operate across different `date`-type objects.

Here, we will define a second date. Note here that rather than defining three variables and passing them into our `date()` call, we're just passing in the year, month, and day directly. We're storing this date in the object `my_date2`.

# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)

Now that we have two dates defined, we can determine the difference between these two dates, using the `-` operator. Here, we're storing that information in the variable `time_diff`

# calculate the difference between times
time_diff = my_date - my_date2
time_diff

When we return the contents of `time_diff`, a `datetime.timedelta` type object is returned. This object has its own associated attributes, one of which is `days`. To access the number of days between these two dates, we can access that attribute from `time_diff`, using the same sytax as we specified previously:

# access days attribute
time_diff.days

Here we introduce `date` and `datetime` objects to demonstrate what attribute are and how methods operate on an object directly. We are intentionally not delving into all of the capabilities of these object types at this point; however, feel free to use `dir()` to access the attributes and methods of these object types to gain familiarity with reading documentation and working with new object types. 

## Objects: Summary

- Objects allow for data (attributes) and functions (methods) to be organized together
    - methods operate on the object type (modify state)
    - attributes store and return information (data) about the object (maintain state)
- `dir()` returns methods & attributes for an object
- Syntax:
    - `obj.method()`
    - `obj.attribute`
- `date` and `datetime` are two types of objects in Python

Now, with an understanding of why it can be helpful to have additional object types and a basic understanding of attributes and methods, we can discuss how you can define your own object types!

## Exercises

Q1. **Given the following code `my_date = date(year = 1050, month = 12, day = 12)`, which of the following is the best description?**

A) `my_date` is an object, with methods that store data, and attributes that store procedures  
B) `my_date` is variable, and can be used with functions  
C) `my_date` is an attribute, with methods attached to it  
D) `my_date` is a method, and also has attributes  
E) `my_date` is an object, with attributes that store data, and methods that store procedures  

Q2. **For an object `lets` with a method `do_something`, how would you execute that method?**

A) `do_something(lets)`  
B) `lets.do_something`  
C) `lets.do_something()`  
D) `lets.do.something()`  

Q3. **For an object `lets` with an attribute `name`, how would you return the information stored in `name` for the object `lets`?**

A) `name(lets)`  
B) `lets.name`  
C) `lets.name()`  
D) lets.get.name()  
