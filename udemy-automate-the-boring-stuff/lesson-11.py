# This code uses the try and except statements to get around a function call that divided by zero.
def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

# This code again uses the try and except statements for input validation.
print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        if int(numCats) < 0:
            print('Don''t think you can have negative cats...')
        else:
            print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')