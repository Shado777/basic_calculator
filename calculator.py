#Basic Calculator program
def sum():
    try:
        num1 = int(input("\n=============================\nEnter the first number: "))
        num2 = int(input("Enter the number to add: "))
        totalNum = num1 + num2
        print("The sum of the two numbers are: "+str(totalNum))
    except:
        print("Not a valid number!!")

def minus():
    try:
        num1 = int(input("\n=============================\nEnter the first number: "))
        num2 = int(input("\nEnter the number to subtract: "))
        totalNum = num1 - num2
        print("The difference of the two numbers are: "+str(totalNum))
    except:
        print("Not a valid number!!")

def multiply():
    try:
        num1 = int(input("\n=============================\nEnter the first number: "))
        num2 = int(input("\nEnter the number to multiply by: "))
        totalNum = num1 * num2
        print("The answer is: "+str(totalNum))
    except:
        print("Not a valid number!!")

def divide():
    try:
        num1 = int(input("\n=============================\nEnter the first number: "))
        num2 = int(input("Enter the number to add: "))
        totalNum = num1 / num2
        print("The answer is: "+str(totalNum))
    except:
        print("Not a valid number!!")

def resume():
    res = str(input("=======================\nDo you want to continue\nChoose Y or N: "))
    if (res == "Y"):
        while(res == "Y"):
            menu()
            break
    else:
        print("Goodbye!")

def menu():
    print("\n=============================\nWelcome to my Calculator app\nChoose an option below by entering the number\n")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")

    try:
        choose = int(input("\nEnter the number here: "))
        if (choose == 1):
            sum()
            resume()
        elif(choose == 2):
            minus()
            resume()
        elif(choose == 3):
            multiply()
            resume()
        elif(choose == 4):
            divide()
            resume()
    except:
        print("Not a valid number!")
        resume()

menu()
