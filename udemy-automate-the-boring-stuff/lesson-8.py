# Import the random module
import random

# Use the randint() function from the random module
random.randint(1, 10)

# Import all functions from the random module and call only the randint function without having to specify the randint
# module (random.)
from random import *
randint(1, 10)

# Import the sys module, print hello, use the exit function from the sys module, and exit the program.
# Goodbye will not be printed.
import sys
print('Hello')
sys.exit()
print('Goodbye')