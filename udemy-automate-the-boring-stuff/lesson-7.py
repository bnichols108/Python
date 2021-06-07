# For loop that iterates 5 times
print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

# For loop to add all of the numbers from 0 to 100. The range must be set to 101 to include 100.
total = 0
for num in range(101):
    total = total + num
print(total)

# While loop similar to the first for loop. This while loop also iterates 5 times.
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times ' + str(i))
    i = i + 1

# Same for loop as the first example except we use range function from 12-16 (not including 16).
print('My name is')
for i in range(12, 16):
    print('Jimmy Five Times ' + str(i))

# Same for loop as the first example except we use range function from 0-10 (not including 10) and stepping by 2.
print('My name is')
for i in range(0, 10, 2):
    print('Jimmy Five Times ' + str(i))

# Same for loop as previous example except going backwards. We use range function from 5 to -1
# (not including -1) and stepping by -1.
print('My name is')
for i in range(5, -1, -1):
    print('Jimmy Five Times ' + str(i))