![alt text](https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto/gigs/69090491/original/dcafeb1f95fbe2501376c8e9629109ba979d6a67/learn-python-programming-language.jpg)

# Python Standard Library Quick Reference

## Overview

This markdown contains a list of great standard libary, built in functions that can be used during coding challenges, classes projects, and white board coding to boost perfomance, limit lines of codes, and give a more pythonic syntax.


## Why

After taking my coding challenge for the 2019 Software Engineering Intership with JP Morgan, I realisezd that if I will be using python for coding challenges and plan on succeeding, I must know it and its tricks like the back of my hand.


## Table of Contents

* Loops
* Arithmetics
* Strings
* Lists
* Tuples
* Dictionaries
* Sets



### Loops


### Strings

1. Replace

You can use the str.replace(old_value, new_value) method to replace the occurence of one string to another.

You can slice elements with [start:end] operator :
```python

    str = 'Medi Assumani'
    
    new_str = str.replace('Assumani', 'Boss')
    
```

2. Join

The join function is a more flexible way for concatenating string. With join function, you can add any character into the string.

```python

str = 'Python is very flexible. It is also good to use python for Data Science.'
char = "🐍"
print(char.join("python")) # will put python everytime after 🐍 .
```

3. Split

The split function breaks up a string into a list of words given a specific character.

```python

str = "I dont want to frow up"
str.split(" ") # will split the string each time it sees a space
['I', 'dont', 'want', 'to', 'frow', 'up']
```

4. Count

The count(element) method takes in an element and returns its occurences in the string.

```python

str = "I ate like for times like i was like you know like"
str.count("like") # returns 3 because like appears three times in the string

```

5. Find & Rfind

### Lists

1. Slicing

You can slice elements with [start:end] operator :
```python

#general syntax
list2 = list1[start:stop:step]  


list_one = [1,2,3,4,5,6,7,8,9,10]

    # 1. gets elements from 1st to 5th index exclusive
    answer_one = list_one[1:4] 
    
    # 2. gets all even numbers from 1st to 8th elementself. :2 tells python to increment by 2
    
      answer_two = list_one[1:7:2]
    
    # 3. get list backward
    backward_list = list_one[::-1]
    
    # 4. Get all elements but the last
  
    exclude_last = list_one[:-1]

```

2. zip(listOne, listTwo)

3. expand()



### Tuples



### Dictionaries



### Sets

Sets are mutable objects that does not allow duplicates. No <b>indexing</b> or <b>slicing</b>. We can add and remove value from sets(mutable). However, elements in the set themeselves are immutable.

#### Two Types of Sets(object) in Python:

* <light>Set</light> object : mutable 
* <light>frozenset</light> object: immutable

```python

    a = set() #empy set
    b = frozenset() #empty frozen set 
```

1. add()

2. remove()

3. s.difference(t) = get a set of elements in S that arent in t

4. s.intersection(t) = get a set of elements that are both found in S and T

5. s.isdisjoint(t) = returns True or False if S and T have nothing in common.

6. s.union(t) = unifies both sets without duplicates


### OrderedDict

OrderedDict are dictionaries subclass that keeps track of the inserted keys.

```python
from collections import Counter

  
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
  
for key, value in d.items(): 
    print(key, value) 
  
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items(): 
    print(key, value) 

This is a Dict:
('a', 1)
('c', 3)
('b', 2)
('d', 4)

This is an Ordered Dict:
('a', 1)
('b', 2)
('c', 3)
('d', 4)
```


### Lambda Funtions

Lambda are anonymous functions used for short and powerful computation

```python
    
    # 
    lambda arguments: expression
    
    cube_root = lambda x: x*x*x
    list_one = 1,2,3,4,5,6,7
    
    even_numbers = list(filter(lambda x: (x%2 ==0), list_one))
    squared = list(map(lambda x: x**2), list_one)
    summed = reduce((lambda x,y: x*2), list_one)
```
