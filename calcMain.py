def convertString(str):
    try:
        returnValue = int(str)
    except ValueError:
        returnValue = float(str)
    return returnValue

def addition(a, B):
    return convertString(a) + convertString(B)

def subtraction(a, B):
    return convertString(a) - convertString(B)

def multiplication(a, B):
    return convertString(a) * convertString(B)

def division(a, B):
    return convertString(a) / convertString(B)

keepProgramRunning = True

print "Welcome to the Calculator!"

while keepProgramRunning:
    print "Please choose what you'd like to do:"

    print "0: Addition"
    print "1: Subtraction"
    print "2: Multiplication"
    print "3: Division"
    print "4: Quit Application"    

 
    choice = raw_input()    

    if choice == "0":
        numberA = raw_input("Enter your first number: ")
        numberB = raw_input("Enter your second number: ")
        print "Your result is:"
        print addition(numberA, numberB)
    elif choice == "1":
        numberA = raw_input("Enter your first number: ")
        numberB = raw_input("Enter your second number: ")
        print "Your result is:"
        print subtraction(numberA, numberB)
    elif choice == "2":
        numberA = raw_input("Enter your first number: ")
        numberB = raw_input("Enter your second number: ")
        print "Your result is:"
        print multiplication(numberA, numberB)
    elif choice == "3":
        numberA = raw_input("Enter your first number: ")
        numberB = raw_input("Enter your second number: ")
        print "Your result is:"
        print division(numberA, numberB)
    elif choice == "4":
        print "Bye!"
        keepProgramRunning = False
    else:
        print "Please choose a valid option."
        print "\n"
