x=int(input("Enter first number "))
y=int(input("Enter second number "))
try:
    z=x/y
    print("Divison result",z)
except ZeroDivisionError:
    print("Invalid attempt of diviosn ")
    print("hello this line is last line ")

