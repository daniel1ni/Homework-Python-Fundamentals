print("Hello World")
name = (input("What's your name? "))
print(f"Hello, {name}, you are welcome here!")
number1 = int((input(f"{name}, give me a number 1: ")))
number2 = int((input(f"{name}, give me a number 2: ")))
sum = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 // number2
print (f"The sum of {number1} and {number2} is {sum}")
print (f"The difference of {number1} and {number2} is {difference}")
print (f"The product of {number1} and {number2} is {product}")
print (f"The quotient of {number1} and {number2} is {quotient}")
age = int(input("How old are you now? "))
ageNext = int(age + 1)
print(f"Next year you'll be {ageNext} years old.")
