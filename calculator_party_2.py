print("Welcome!")
print("This is a calculator for only whole numbers")
print("So you want to either add, subtract, multiply, or divide?")
choose = input("Choose one of the four! ")
number = input("what is your first number? ")
number2 = input("what is your second number? ")
number = int(number)
number2 = int(number2)
if choose == ("add"):
    finalnumber = number + number2
    print (finalnumber)
if choose == ("subtract"):
    finalnumber = number - number2
    print(finalnumber)
if choose == ("multiply"):
    finalnumber = number * number2
    print(finalnumber)
if choose == ("divide"):
    finalnumber = number / number2
    print(finalnumber)
    print("If you want to do a new search, click Run.")
