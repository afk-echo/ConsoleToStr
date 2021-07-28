# ConsoleToStr
A light-weight module written in Python that converts the console outputs from a running Python program into a Python String.

## Installation
1. Grab the latest release of the module from the [releases](https://github.com/afk-echo/ConsoleToStr/releases) page.
2. Place the `ConsoleToStr.py` in your working project directory.

## Usage
````python
from ConsoleToStr import ConsoleToStrConverter

conv = ConsoleToStrConverter()  # returns an instance of the ConsoleToStrConverter class that can be used in the current program.
````

## Methods
1. `ConsoleToStrConverter.start()`:
Starts the converter.
````python
conv.start()  # Stops printing any outputs on the console window.
````

2. `ConsoleToStrConverter.curr()`:
Returns a string containing all the outputs on the console window after calling the start() method.
````python
conv.curr()  # Does not affect the current state of the converter.
````

3. `ConsoleToStrConverter.stop()`:
Stops the converter, and all subsequent console outputs are printed on the console window.
Returns a string containing all the outputs on the console window after calling the start() method.
````python
conv.stop()  # All console outputs post will be printed on the console after this call.
````
* Object once called can be reused by using `conv.start()` even after it has been stopped.

## Examples

1. A basic example - helps in understanding how the respective methods work.
```python
from ConsoleToStr import ConsoleToStrConverter

conv = ConsoleToStrConverter()

print("The beginning!")
conv.start() # initialises the converter - all outputs to the console stops while the value is being stored

print("Line 1")
print("Line 2")
mid = conv.curr()  # retrieves the current console string

print("Line 3")
print("Line 4")

final = conv.stop()
print("The end.")  # stops the converter - all future outputs go back to the default console

print("The string returned from the curr method is: ", mid)
print("The string returned the stop method is: ", final)

conv.start()  # demonstrates reuse of the object once initialised
print("Resurrection!")
print("This object is reusable.")
mid = conv.stop()
print("Output on reuse:", mid)

'''OUTPUT:
The beginning!
The end.
The string returned from the curr method is:  Line 1
Line 2
The string returned the stop method is:  Line 1
Line 2
Line 3
Line 4
Output on reuse: Resurrection!
This object is reusable.
'''
```

2. Usage of the converter to extract the output from the help() method, which does not return a string as an output.
```python
from ConsoleToStr import ConsoleToStrConverter

conv = ConsoleToStrConverter()

# The inbuilt help() function only prints the output on the console, rather than returning a string.
# We can use help() to demonstrate an application of the converter.

conv.start()

help(list.pop)

result = conv.stop()
print(result)  # Prints the same output from the help() function called earlier, but returns a string that we can manipulate.

'''OUTPUT:
Help on method_descriptor:
pop(self, index=-1, /)
    Remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.
'''
```
