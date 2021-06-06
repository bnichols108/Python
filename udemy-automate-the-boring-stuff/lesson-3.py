# This program says hello then asks for your name and age

# Call the print function
print('Hello World')

# Call the print function and ask the user for their name
print('What is your name?')

# Call the input function and wait for user to type in their name
myName = input()

# Call the print function and print meeting statement with myName input
print('It is good to meet you, ' + myName)

# Call the print function and begin to display user's name length
print('The length of your name is:')

# Call the len function to evaluate the integer for the string argument and print length of the myName variable
print(len(myName))

# Call the print function and ask the user for their age
print('What is your age?')

# Call the input function and wait for user to type in their age
myAge = input()

# Call the print function, string, and int function and print the user's age next year by adding one
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
