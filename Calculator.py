#SIMPLE CALCULATOR
#Select numbers
num1 = int(input("Please choose your first number"))
num2 = int(input("Please choose your second number"))
calculation = input("Now choose the calculation (- or + or * (multiply))")
if (calculation == "+") :
  print(num1 + num2)
elif (calculation == "-") :
  print(num1 - num2)
elif (calculation == "*") :
    print(num1 * num2)
else:
  print("I can't do that")
 
