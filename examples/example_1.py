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
