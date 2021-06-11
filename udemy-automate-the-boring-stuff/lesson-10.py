# This section of code will fail. When we try to print the eggs variable, it's not define.
# The reason eggs is not defined is because it's defined from within the spam function local scope.
def spam():
    eggs = 99

spam()
print(eggs)

##############################

# This section of code will run properly and eggs will be printed as 99. This is because of the local scope for the
# bacon function. We set eggs to 0 in the local scope of bacon. But once the bacon function returns, those local
# variables are lost.
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

##############################

# This section of code will run properly and will print 42. The eggs variable is set in the global variables. The spam
# function uses the eggs global variable when calling the print function
def spam():
    print(eggs)

eggs = 42
spam()

##############################

# This section of code will run properly and will print both eggs variables. We have two egg variables,
# one in the global scope and another inside of the local scope of the spam function.
def spam():
    eggs = 'dog'
    print(eggs)

eggs = 42
spam()
print(eggs)

##############################

# This section of code below will run properly and will replace the global eggs variable with what is set in the
# spam function. You can see we tell the spam function to use the global variable eggs, we then set it to dog, then
# print eggs, which is dog. The spam function returns, then eggs is printed, which again, is dog, now that it's
# been set via the spam function.
def spam():
    # The line below tells the spam function to use the global variable for eggs, not the local.
    global eggs
    eggs = 'dog'
    print(eggs)

eggs = 42
spam()
print(eggs)