#Write a function which has no input parameter. The function asks the user to 
# enter numbers. The user can enter repeated numbers but if the user entered a 
# number which was already entered, the function will provide an error message to 
# the user and ask the user to enter another one. The user can enter numbers as long 
# as s/he has not entered 0. Once a 0 is entered, the function returns the sum of all 
# distinct numbers the user had entered. 


def checkNumbers(list, num):
    if num in list:
        print("ERROR:Number already exist in this list")
        return False
    else:
        return True

def InputList():
    number = int
    numbers = []
    while number != 0:
        number = int(input("Number:"))
        if checkNumbers(numbers, number):
          numbers.append(number)
    Sum = sum(numbers)
    print("Sum: ", Sum)

InputList()
