def add(a , b):
    return a + b
def substract(a , b):
    return a - b
def multiply(a , b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid number")
def get_choice():
    choice = input("Choose operation: ")
    while choice not in ["1" , "2", "3","4"]:
        print("Invalid choice")
        choice = input("Choose operation: ")
    return choice

print("Simple calculator")
print("1. Add")
print("2. Subscract")
print("3. Multiply")
print("4. Divide")

choice = get_choice()

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

if choice == "1":
    print(add(num1 , num2))
elif choice == "2":
    print(substract(num1 , num2))
elif choice == "3":
    print(multiply(num1 , num2))
elif choice == "4":
    print(divide(num1 , num2))
else:
    print("invalid choice")    