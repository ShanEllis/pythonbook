# Classes 

Similar to functions where we introduced functions like `len()` and `type()` before discussing how to define your own functions, there are many available object types (either in the standard library or that can be imported - like `date`-type objects) *and* you can define your own objects and their associated attributes and methods. Just as we used `def` to define functions, in this chapter we'll discuss `class` to create your own classes of objects. 

We'll also introduce the concept of instances and return to the concept of object-oriented programming and what that means in python.

As discussed earlier, objects are a way to combine associated data (attributes) and procedures (methods) that can be carried out on that data in a systematized and organized manner. 

## `class` defintion

With the definition of objects fresh in our mind, we can delve into how to create our own object types. To do this, we  use the `class` keyword. This opens a code block within which we can specify the instructions to create objects of our specified type. 

<div class="alert alert-success">
<b>Classes</b> define objects. The <code>class</code> keyword opens a code block for instructions on how to create objects of a particular type.
</div>

A helpful analogy is to think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.). They specify the plan, explain how each component fits together, and keeps everything organized. 

## `class`: Dog

Here, we introduce our first object type. We use `class` to define a `Dog`-type object.

Note that, unlike variables and functions (where we use snake_case), for `class`es, we'll use CapWords to specify class names. 

Here, the `class` keyword indicates that we're defining a new `class` of objects that we're going to call `Dog`. The colon (`:`) opens up the code block.

Within the `class` definition, we define one attribute `sound`. Note that since attributes store pieces of data, attribute definition will take the format of variable assignment.

After defining the `sound` attrribute, we see what looks like a function definition. This is because methods *are* functions. They're just a specific kind of function, one that is defined within a `class` definition and designed to operate directly on the object type within which it is defined. 

However, one unique aspect about `class` definitions is the concept of an **instance**. We'll define this in more detail in a second, but this comes into play in the method definition below. We see the method `speak` takes an input parameter `self`. This `self` specifies that we want to operate on the current object (or the current 'instance' of the object'). Thus, within the function, whenever you see `self`, you know it refers to the current `Dog`. We'll delve into this more momentarily!

A final note about `class` objects for now is that, like functions, a new namespace is created within a `class`. They only have access to the variables passed into or definied within them. 

# Define a class with `class`. 
class Dog():
    
    # Class attributes for objects of type Dog
    sound = 'Woof'
    
    # Class methods for objects of type Dog
    def speak(self):
        print('Dog says:', self.sound)

After a `class` has been defined, we can create objects of that type. For example, here we create a `Dog` type object, storing that object in the varaible `lexi`

# Initialize a dog object
lexi = Dog()

After `lexi` has been defined, we're able to access information stored in this object type. We do this using the syntax described in the previous chapter, first specifying the object, followed by a `.` and then the attribute name.

# lexi, has 'sound' attribute(s) from Dog()
print(lexi.sound)

As a reminder, when we access an attribute, we are looking up information about the object and that information is returned. There are no operations being carried out.

Alternatively, when we execute a method, we are running the code within the method specified directly on the object itself.

For example, when we call `speak()` on `lexi`, the code within the `speak()` method executes.

# lexi, has 'Dog' method(s)
# remember we used `self`
lexi.speak()

### **`class`** Summary:

- classes tend to use **CapWords** convention
    - instead of snake_case (functions and variable names)
- `()` after `Dog` indicate that this is callable
    - like functions, Classes must be executed before any objects are created
- can define **attributes** & **methods** within `class`
- `self` is a special parameter for use by an object
    - refers to the thing (object) itself
- like functions, a new namespace is created within a Class


### Using our `Dog` Object

Now that we've defined a `Dog`-type object, we can create multiple `Dog`s. 

For example, we could create a list of four different `Dog` type objects. Note that every time `Dog()` is called, a new `Dog`-type object is created. This is what we refer to as an **instance** of an object. When you call `Dog()` here, you are creating another **instance** of a `Dog()`-type object.

# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

After defining `pack_of_dogs`, if we were to take a look at what is stored within this list, you'll notice that each element of the list indicates that a `Dog` type object is being stored.

# take a look at this
pack_of_dogs

We can then iterate over this list (as we've done for lists previously) and call a method on each `dog` in our list, using the following approach:

for dog in pack_of_dogs:
    dog.speak()

We demonstrate this here for two reasons: 1) to indicate that all of the code constructs previously introduced (loops, conditionals, etc.) are still available when working with classes and 2) to demonstrate that methods operate directoy on their associated objects using the syntax `object.method()`.

## Instances & `self`

While referenced above, we've yet to formally define what an **instance** is. An **instance** refers to a particular instantiation of a `class` object. Every time a `class` object is executed (created), a new **instance** of that `class` object is created. 

To refer to the *current* instance, we use the word `self`.

<div class="alert alert-success">
An <b>instance</b> is particular instantiation of a class object. <code>self</code> refers to the current instance. 
</div>

# Initialize a dog object
lexi = Dog()

From the example we discussed above:

- Dog is the `class` object we created
- `lexi` was an _instance_ of that class
- `self` refers to whatever the _current_ instance is

### Instance Attributes

With this concept of instances now made a little more clear, we can introduce the concept of **instance attributes**. So far, we have only demonstrated how to define a **class attribute**. A **class attribute** is an attribute that *all* objects of this `class` will share. For our `Dog` example, all `Dog`-type objects shared the class attribute 'sound'. Every dog stored 'Woof' in the attribute `sound`. 

Alternatively, an instance attribute specific to the current instance of the `class` object. This allows for different instances of the `class` object to store different data in an instance attribute.

To do use we use the special `__init__` method when defining instance attributes. (Note that those are two leading and two trailing underscores around the word 'init'.)

<div class="alert alert-success">
Instance attributes are attributes that we can make be different for each instance of a class. <code>__init__</code> is a special method used to define instance attributes. 
</div>

class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specify instance-specific attributes
    # leading and trailing double underscores indicates that this is special to Python
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print('Dog says:', self.sound)

With this updated `Dog` class definition, we can now initialize a new instance of `Dog()`:

# Initialize a dog
gary = Dog(name = 'Gary') 

In the code above, we now see that we have to pass `name` when we create an instance of the `Dog()` object, specifying what the `name` is of *this* particular instance of `Dog()`. 

As with class attributes, we can access what is stored in an instance attribute using the general syntax `object.attribute`:

# Check gary's attributes
print(gary.sound)    # This is an class attribute
print(gary.name)     # This is a instance attribute

For completeness' sake, note that we are still able to carry out the associated `Dog` methods on `gary`:

# Check gary's methods
gary.speak()

**A word of caution about `self`**

The use of `self` as the first parameter in instance attribute definition is a frequent criticism of the Python programming language. This is partially because `self` is what Pythonistas have agreed to use as the first parameter passed during instance attribute definition - it is *not* a keyword. In theory, you could use any word to refer to the current instance of a `class` object; however, you (and others reading your code) will have to remember later on what you used to refer to the current instance. As such, we tacitly agree that we'll use `self` as the first parameter in instance attribute definition to refer to the current instance of a `class` object.

## Class Inheritance

With an understanding of `class` definition and instance attributes, we can now introduce the concept of `class` inheritance. The concept here is taht objects can be built from other objects, inheriting the other objects' properties and building off of them. This allows for `class` objects to be related in a hierarchical order.

For examplle, with our `Dog()` example above, we could also create a `Cat` object. If we then wanted to create a general `Animal` class, we could then have `Dog` and `Cat` inherit any general animal properties from `Animal()`.

To look at a specific example, let's consider the general class `Tool` and how what the syntax would look like if we wanted to inherit `Tool`'s properties in the more specific class `Hammer`:

class Tool():
    
    # define instance attributes
    def __init__(self):       
        self.is_tool = True
        self.tool_type = None
    
    # define class method
    def use_tool(self):
        print('Using tool.')

Here, se see that there are two *instance* attributes: `is_tool` and `tool_type`. The class `Tool` specifies that any `Tool` will have the value `True` for `is_tool` and `None` for `tool_type`, as this is the more general class.

There's also the `Tool` method `use_tool`, which, for a given instance, when executed will print `'Using tool.'`

As previously, we can initialize a `Tool` type object, storing it in `my_tool`. We can then access the attributes of `Tool` and carry out any `Tool` methods:

# access attribute
my_tool = Tool()
my_tool.is_tool

# use method
my_tool.use_tool()

However, what we're most interested in here is the concept of **inheritance**. In the code below, we see how you can inherit `Tool` properties within a new `class` object `Hammer`.

By passing `Tool` in when creating the `class` `Hammer`, `Hammer`-type objects will have the attributes and methods specifed within `Tool`.

We also see with the code here that we're specifying that `tool_type` for a `Hammer` will be `'Hammer'` and provide an additional instance attribute `why`, giving the `Hammer` a purpose - `'To hammer things.'`

class Hammer(Tool): #inherit Tool class
    
    def __init__(self):        
        self.tool_type = 'Hammer'
        self.why = 'To hammer things.'

We can now create a `Hammer`-type object and use the methods from `Tool` - such as `use_tool`- since that is inherited.

# Hammer has Tool attributes and methods
my_hammer = Hammer()
my_hammer.use_tool()

And, we can also access the `Hammer`-specific attributes:

# Hammer has Hammer attributes
my_hammer.why

However, you'll note that `Hammer` does *not* have access to the *attributes* from `Tool`:

# this code will error
my_hammer.is_tool

This is becuase our `Hammer` `class` defines its own *instance attributes*, overriding the instance attributes of the inherited class. We'll see in just a second how to avoid this using `super()`.

Further, note that inheritance is a one-way street. If you created a `Tool` class object (which is the parent class here) and does *not* inherit from `Hammer`, it only has access to `Tool` attributes and methods, so the following would execute without issue:

# Tool objects only have Tool attributes & methods
my_tool = Tool()
my_tool.is_tool

However, if you tried to access the `why` attribute on a `Tool` type object, you would encounter an `AttributeError`, as there is no attribute `why` in the `Tool` class object:

# Tool does NOT inherit from Hammer
# this code will produce an error
my_tool.why

Note in the example above that `tool_type` of `Hammer` class overrides the `tool_type` specified in the `Tool` class that it inherits. The `class` definition can and will override attributes and methods defined in the Parent class.

### `super()`

`super()` allows you to refer to the inherited, parent class, without naming it specifically.

This is particularly helpful when you want to extend the functionality of a class from which you are inheriting.

In the example above, we inherited from `Tool` in our `Hammer` definition and saw that while the `Tool` method were availalbe, the `Tool` instance attraibutes were *not*, due to the fact that our `Hammer` definition had overridden the `Tool` instance attribute definition. 

So...how do we avoid that? This is where `super()` comes in. In the example below, we've added a single line of code (`super().__init__()`) to our `Hammer` definition from above. This specifies that we want to inherit the instance attributes from our parent class `Tool`.

class Hammer(Tool): #inherit Tool class
    
    def __init__(self):        
        super().__init__()
        self.tool_type = 'Hammer'
        self.why = 'To hammer things.'

With this revised `Hammer` definition, we now are able to access the instance attributes from the parent class

new_tool = Hammer()
new_tool.is_tool

Note, however, that for attributes defined in both `Hammer` and `Tool`, even when we inherit instance attributes from the parent `Tool` class, the child class `Hammer` takes precendence, such that `tool_type` still stores 'Hammer' (from the `Hammer` definition), rather than `None` (from the parent `Tool` class definition)

new_tool.tool_type

## `class`: Summary
- `class` creates a new class type
    - names tend to use CapWords case
    - can have attributes (including instance attributes) and methods
        - `obj.attribute` accesses data stored in attribute
        - `obj.method()` carries out code defined within method 
- instance attributes defined with `__init__`
    - `__init__` is a reserved method in Python
    - This "binds the attributes with the given arguments"
    - `self` refers to current instance
    - `super()` refers to the inherited `class`
- to create an object (instance) of a specified class type (`ClassType`):
    - `object_name = ClassType(input1, input2)`
    - `self` is not given an input when creating an object of a specified class

## Everything in Python is an Object!

We mentioned the fact that Python is an object-oriented programming (OOP) language before without providing a formal definition or discussing it in much detail. OOP is a programming paradigm in which code is organized around objects. Now that we have a better undersatnding of what `class` objects are, we can better understand why this is a helpful paradigm. 

<div class="alert alert-success">
<b>Object-oriented programming (OOP)</b> is a programming paradigm in which code is organized around objects. Python is an OOP programming langauge. 
</div>

To drive this point home, below we use `isinstance()` which checks whether the first parameter is of the second parameter's specified type. For example, we see below that the following returns `True`, as 6 is an `int` type object:

isinstance(6, int)

Alternatively, the following returns `False` as 'hi' is a `str` type object and _not_ an `int`:

isinstance('hi', int)

With this logic we can see that everything we've discussed thus far in this textbook is an `object`, as every `isinstanc()` statement below demonstrates that everything is in fact an object in Python:

### Data variables are objects

print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a = 3
print(isinstance(a, object))

### Functions are objects

print(isinstance(sum, object))
print(isinstance(max, object))

# Custom function are also objects
def my_function():
    print('yay Python!')
    
isinstance(my_function, object)

### Class definitions & instances are objects

class MyClass():
    def __init__(self):
        self.data = 13

my_instance = MyClass()

print(isinstance(MyClass, object))
print(isinstance(my_instance, object))

## `class`: `ProfCourses`

With the basic explanations of concepts and provided examples thus far, you should have a sense that new objects can be created to store information (in the form of attributes) that are *attached* or *belong* to the object type *and* that methods are functions that are *attached* or *operate on* the object type directly. However, to this point, the examples have been somewhat contribed. Let's work through an example that incorporates concepts discussed up to this point to get a sense for how object-oriented programming and creating new objects can be beneficial.

For this example, envision that you're a professor who teaches a handful of different courses each year. And, you want to be able to keep track of these courses and carry out a handful of operations on these courses. For this example, we'll build the code as we go, adding on additional pieces throughout this section, explaining each as we add it on. To get started, let's focus on a few instance attributes.

class ProfCourses():
    
    # create three instance attributes
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof

In the example provided above we three instance attributes, two of which (`n_classes` and `classes`) are initialized with values, and one (`prof`) which requires definition upon creation of an instance of a `ProfCourses` object. If we think about these variables, when we first initalize an instance of a `ProfCourses` object, it makes good sense that `n_class` (standing in for number of classes) should be zero and the list of those `classes` should be an empty list. Eventually, we'll write a method that will add to and update these attributes. On the contrary, `prof` has to be specified upon initialization, so we know which prof's courses we're talking about.

Let's do that now, and create an instance of our `ProfCourses` object!

ellis_courses = ProfCourses('Ellis')
print(ellis_courses.n_classes)
print(ellis_courses.classes)
print(ellis_courses.prof)

Above, the output `print`ed matches our expectation. The `n_classes` and `classes` attributes are zero and an empty list, respectively, while the `prof` attribute stores 'Ellis', which was the value provided when the `ProfCourses` object was initialized. So, we've got some attributes, but now let's add a method to actually add classes to this object!

While the example will get more and more involved, at each step only a handful of lines will change, adding to what was in the previous step. Here, we add the `add_class` method.

class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    # add method that will add classes as a dictionary
    # to our attribute (classes)...which is a list
    def add_class(self, course_name, quarter, n_students):
        
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        # increase value store in n_classes
        # by 1 any time a class is added
        self.n_classes += 1

The `add_class` method has three parameters: `course_name`, `quarter`, and `n_students`, none of which takes a default value. 

Within the function, we see that when the `add_class` method is executed, the values for each of the three input parameters will be stored in a dictionary. This dictionary will be appended to the `classes` attribute. We also see the value stored in `n_classes` will increment by 1.

After defining the above `class`, we can create an instance of this object, call the `add_class` method on that object and take a look at the attributes of that ojbect:

# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a class
ellis_courses.add_class('COGS18', 'fa20', 363)

# see output
print(ellis_courses.n_classes)
ellis_courses.classes

After calling the `add_class()` method, we see that, as we would expected `n_classes` increases to 1 and `classes` is a list that now stores a single dictionary, including the information about the course, as specified when `add_class()` was executed.

From here, we can add an additional method `compare`. This will function to compare values within the `classes` object, allowing us to return, for example, the class with the most students...or the fewest students.

class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    def add_class(self, course_name, quarter, n_students):
        
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        self.n_classes += 1
        
     
    # add method to compare values in classes
    def compare(self, attribute, direction='most'):
    
        fewest = self.classes[0]
        most = self.classes[0] 
        
        for my_class in self.classes:
            if my_class[attribute] <= fewest[attribute]:
                fewest = my_class
            elif my_class[attribute] >= most[attribute]:
                most = my_class
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output

While we won't walk through every line of code above, what you'll want to keep in mind is that `fewest` and `most` are both dictionaries. Before the `for` loop, they are initialized with the first dictionary in `classes`. From there, the value (dictionary) in each is updated, only if the value stored in the `attribute` (key specified) is lower (for `fewest`) or higher (for `most`) than the value in the previous iteration of the loop. At the end of the loop, a conditional is used to determine what should `return`ed from the loop by considering what the input to `direction` (method parameter) is.

Here, we'll create an instance of the `ProfCourses` object and call the `add_class` method a number of times to add multiple classes to the `classes` attribute of our object:

# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_class('COGS18', 'fa20', 363)
ellis_courses.add_class('COGS108', 'fa20', 447)
ellis_courses.add_class('COGS18', 'su20', 88)
ellis_courses.add_class('COGS108', 'sp20', 469)
ellis_courses.add_class('COGS108', 'sp19', 825)

# see the courses
print(ellis_courses.n_classes)
ellis_courses.classes

Above we see that `ellis_courses` now stores information about 5 different courses, each of which is stored as a dictionary in the list `classes`, which is an attribute of the `ProfCourses` class. 

With this, we can now use our `compare` method:

# make comparison among all courses
# returns the class with the most students
ellis_courses.compare('n_students')

Given the code, and as we see above, if the attribute is `n_students`, the dictionary corresponding to the quarter with the 'most' students will be returned by default. 

Of course, if we wanted it to return the `'fewest'`, we could specify that in the `direction` parameter: 

# return the class with the fewest students
ellis_courses.compare('n_students', 'fewest')

Given our current setup, the only attribute that could be used for meaningful comparison is `n_students`, but, what if for each class there were additional `'attribute`s?  

In this final iteration of `ProfCourses`, the instance attributes and `compare` methods remain unchanged. The only difference is that `add_class` has additional paramters, `n_exams` and `n_assigments`, for example.

class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    def add_class(self, course_name, quarter, 
                  n_students, n_exams, n_assignments):
        
        # add in additional key-value pairs
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students,
                             'n_exams' : n_exams,
                             'n_assignments' : n_assignments})
        self.n_classes += 1
        
     
    def compare(self, attribute, direction='most'):
    
        fewest = self.classes[0]
        most = self.classes[0] 
        
        for my_class in self.classes:
            if my_class[attribute] <= fewest[attribute]:
                fewest = my_class
            elif my_class[attribute] >= most[attribute]:
                most = my_class
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output

When we go to add classes to a `ProfCourses` object now, additional arguments are required for these additional parameters:

# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_class('COGS18', 'fa20', 363, 2, 5)
ellis_courses.add_class('COGS108', 'fa20', 447, 0, 6)
ellis_courses.add_class('COGS18', 'su20', 88, 3, 5)
ellis_courses.add_class('COGS108', 'sp20', 469, 0, 6)
ellis_courses.add_class('COGS108', 'sp19', 825, 0, 5)
ellis_courses.add_class('COGS18', 'fa19', 301, 2, 4)

# see the courses
print(ellis_courses.n_classes)

However, with this additional functionality we can do comparisons on additional arguments now, for example the class with the most exams:

# return the class with the most exams
ellis_courses.compare('n_exams', 'most')

...or the fewest assignments:

# return the class with the fewest assignments
ellis_courses.compare('n_assignments', 'fewest')

At this point, hopefully you have a sense for how it can be helpful to organize code into objects whenenver you have information (attributes) and operations (methods) that work together. However, this class is not perfect. See the exercises below for considerations to add additional functionality and improve this class!

## Exercises

Q1. **Which of the following is true about the following `Dog` class?**

```python
class Dog():
    
    sound = 'Woof'
    
    def speak(self):
        print(self.sound)
```

A) `Dog` is a class, `sound` is an attribute, and `speak` is a method.  
B) `Dog` is a function, `sound` is an attribute, and `speak` is a method.  
C) `Dog` is a class, `sound` is a method, and `speak` is an attribute.  
D) `Dog` is a function, `sound` is an method, and `speak` is an attribute.  

Q2. **Using the definition in the previous question, how many instances of `Dog()` are created below and how many times does the `speak()` method execute if the following code were to execute**:

```python
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

counter = 1

for doggie in pack_of_dogs:
    if counter <= 2:
        doggie.speak()
        counter += 1
    else:
        break
```

A) 2 instances, 2 method executions  
B) 2 instances, 4 method executions  
C) 4 instances, 2 method executions  
D) 4 instances, 4 method executions  

Q3. **Edit the `Dog()` code provided above to allow for each `Dog`-type object to have an attribute specifying its breed.**

Q4. **What will the following code snippet print out?

```python
class MyClass():
    
    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score
    
    def check_score(self):        
        if self.score <= 65:
            return self.email
        else:
            return None
        
student = MyClass('Rob', 'rob@python.com', 62)
student.check_score()
```

A) True  
B) 'Rob'  
C) False   
D) 'rob@python.com'  
E) None  

Q5. **Given the following set of classes, what will the code provided print out?**

```python
class Brain(): 
    
    def __init__(self, size = None, folded = None):
        self.size = size
        self.folded = folded
        
    def print_info(self):
        folded_string = ''
        if not self.folded:
            folded_string = 'not'
        print('This brain is ' + self.size + ' and is ' + folded_string + ' folded.')
         
class SheepBrain(Brain):
    
    def __init__(self, size = 'medium', folded = False):
        super().__init__(size, folded)
        
sheep = SheepBrain()
sheep.print_info()
```

A) This brain is medium and folded.  
B) This brain is large and folded.  
C) This brain is medium and not folded.  
D) This brain is medium and False.

Q6. **If we were to add an additional class on top of those in the previous question using the following code, what would the following print out?**

```python
class HumanBrain(Brain):
    def __init__(self, size = 'large', folded = True):
        super().__init__(size, folded)
        
sheep = SheepBrain()
human = HumanBrain()
human.folded and sheep.folded
```

A) True  
B) False  
C) None  
D) AssertionError  

Q7. **This question builds on `ProfCourses` from above. If you haven't worked through that example, do so first and then return here. How would you improve the `ProfCourses` class in this chapter to accomplish each of the following**:

1) account for ties when using the `compare` method?
2) refactor (meaning improve and simplify) the `compare()` method to reduce the need for creating two different objects, only one of which gets `return`ed from the method?
3) add a method to put the dictionary in time order?


**Give any/all of these a try to solidify your `class` understanding!**