# ConsoleToStr
A light-weight module written in Python that converts the console outputs from a running Python program into a Python String.

# Installation
1. Grab the latest release of the module from the [releases](https://github.com/afk-echo/ConsoleToStr/releases) page.
2. Place the `ConsoleToStr.py` in your working project directory.

## Usage
````python
from ConsoleToStr import ConsoleToStrConverter

conv = ConsoleToStrConverter()
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
