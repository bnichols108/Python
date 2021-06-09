# Define a function named hello
def hello():
    # The body of the function is three print statements
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

# Calls the hello function three times
hello()
hello()
hello()

# Define a new function named hello2 that takes one parameter
def hello2(name):
    print('Hello ' + name)

# Call the hello2 function two times with different arguments
hello2('Alice')
hello2('Bob')

# Define a new function named plusOne that returns the parameter "number" plus 1
def plusOne(number):
    return number + 1

# Call the plusOne function passing an argument of 5 and setting that to the newNumber variable, then print
# that variable
newNumber = plusOne(5)
print(newNumber)

# By default, the print function includes the newline
print('Hello')
print('World')

# You can use the keyword argument end to overwrite the newline that the print function includes
print('Hello', end='')
print('World')

# You can also use the keyword argument sep to replace the separating character
print('cat', 'dog', 'mouse', sep='ABC')