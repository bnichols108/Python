# Simple if statement/conditional/flow control
name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')

# Simple if else statement/conditional/flow control
password = 'swordfish'
if password == 'swordfish':
    print('Access Granted')
else:
    print('Wrong Password')

# Simple flow control with if and elif statements
name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie')

# Showing "Truthy" and "Falsey" values
print('Enter a name.')
name = input()
if name:
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')

# Showing "Truthy" and "Falsey" values by checking with the bool function
print('Enter a name.')
name = input()
if bool(name):
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')