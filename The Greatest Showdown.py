# Task1

number1 = int(input("enter 1st number:"))
number2 = int(input("enter 2nd number:"))
number3 = int(input("enter 3rd number:"))

if number1 >= number2 >= number3:
    print(number1, number3)
elif number1 <= number2 <= number3:
    print(number3, number2)
elif number2 >= number3 >= number1:
    print(number2, number1)
else:
    print("no number is greater or less")
