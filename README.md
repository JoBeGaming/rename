# Rename

Python module to implement the `@rename` and `@rename_local` decorators, 
which can dynamically rename objects at runtime

#
*Note that `rename` and `rename_local` need python 3.6 as the minimum version.*

## rename

Rename the object, after which the new name will replace the old one,
making the old object not callable anymore`:
```python

@rename("hi")
def hello(name):
  print(f"Hi: {name}!")

hi("John")

# Throws a NameError
hello("John")
```
Attempting to call the old object will raise a NameError,
that will look like this for the context given above:  
`Name 'hello' is not defined. Maybe you meant 'hi'?`
Note that `@rename` works for classes and functions.

When doing something like
```python

@rename("hi")
def hi(name):
  print(f"Hi: {name}!")
```
We will raise a TypeError:
`New name 'hi' cannot match object name 'hi'.`

## rename_local

When wanting to rename methods, use `@rename_local` and a syntax like:
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
