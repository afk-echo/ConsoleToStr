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
