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
![example_1.py](./examples/example_1.py)

2. Usage of the converter to extract the output from the help() method, which does not return a string as an output.
![example_2.py](./examples/example_2.py)
