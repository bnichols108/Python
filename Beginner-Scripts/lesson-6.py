# While loop that iterates 5 times
spam = 0
while spam < 5:
    print('Hello World!')
    spam = spam + 1

# A cheeky while loop checking for 'your name' from the user's input
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you!')

# While loop with built in infinite loop but utilized a break statement depending upon the user's input
name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# While loop with a continue statement to force the execution back to the start of the loop to reevaluate the loop's condition. This causes "spam is 3" to never show in the output
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))