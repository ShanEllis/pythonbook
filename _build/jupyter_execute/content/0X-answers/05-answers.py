# Answers: Classes

Provided here are answers to the practice questions at the end of "Classes".

## Objects

**Objects Q1**. 

# specific strings will differ
true_var = 'asdf123'.isalnum()
false_var = '!!!!'.isalnum()

**Objects Q2**.

days_summary = {}

for day in days_of_week:
    days_summary[day] = site_days.count(day)

**Objects Q3**.

from random import choice
rand_int = choice(range(0,10))

## Classes

**Classes Q1**.

class ClassRoster():
        
    def __init__(self, course):
        self.students = []
        self.course = course
        
    def add_student(self, pid, name):
        self.students.append({pid: name})

**Classes Q2**.

class ToDo():
    
    def __init__(self):
        self.to_do = []
        
    def add_item(self, item, top=True):
        if top:
            self.to_do.insert(0, item)
        else: 
            self.to_do.append(item)
        
    def remove_item(self, item):
        self.to_do.remove(item)

**Classes Q3**.

class NewYear():
    
    zodiac_signs = {
    'Ox' : [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
    'Tiger' : [1938, 1950, 1962, 1974, 1986, 1998, 2010], 
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
    
    
    def __init__(self, year):
        self.year = year
    
    def return_sign(self):
        for key in self.zodiac_signs:
            if self.year in self.zodiac_signs[key]:
                out = key
                break # answer would be fine without break here
                
        return 'You were born in the year of the ' + out + '!'


**Classes Q4**.

Part I.

class Kingdom():
    
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def introduce(self):
        return 'Hello, my name is ' + self.name + ', and I am a ' + self.title + '.'


Part II. 

import random

class CourtJester(Kingdom):

    headwear = "fool's cap"
        
    def tell_a_joke(self):
        joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
 'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']
        out_joke = random.choice(joke_list)
        return out_joke
    

**Classes Q5**.

class StudentInfo():
    
    def __init__(self, name, year, school, proj_grade):
        self.name = name
        self.year = year
        self.school = school
        self.proj_grade = proj_grade
        
    def follow_up(self):
        out = {}
        if self.proj_grade <= 65:
            out[self.name] = self.proj_grade
        return out