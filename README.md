# Rename

Python module to implement the `@rename` decorators, 
that can dynamically rename objects at runtime. 

#
*Note that `rename` needs python 3.6 or above.*

## rename

Rename the object, after which the new name will replace the old one,
making the old object not callable anymore. This will make the new object behave just like the old one:
```python

@rename("hi")
def hello(name):
  print(f"Hi: {name}!")

hi("John")

# Throws a NameError
hello("John")
```
Attempting to call the old object will now raise a NameError,
that will look like this for the context given above:  
`Name 'hello' is not defined. Maybe you meant 'hi'?`

Note that when doing something like:
```python

@rename("hi")
def hi(name):
  print(f"Hi: {name}!")
```
We will get a TypeError
`New name 'hi' cannot match object name 'hi'.`, as the old name cannot be equal to the new name.

Note that `@rename` works for classes and functions too.
```python

class cls():

  @rename("cls.hi", _local=True)
  def hello(name):
    print(f"Hi: {name}!")

cls.hi("John")

# Throws a NameError
cls.hello("John")
```
  


#

(c) 2025 Jobe
