# Rename

Python module to implement the `@rename` decorator, 
which can dynamically rename global objects at runtime

#
*Note that `rename` needs python 3.6 as the minimum version.*

Rename the object, after which the new name will replace the old one,
making the old object not callable anymore
```python

@rename("hi")
def hello(name):
  print(f"Hi: {name}!")

hi("John")

# Throws a TypeError
hello("John")
```
Attempting to call the old object will raise a TypeError,
that will look like this for the context given above:  
`Name 'hello' is not defined. Maybe you meant 'hi'?`
  


#

(c) 2025 Jobe
