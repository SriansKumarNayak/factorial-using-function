print("=== Find factorial of a number ===")

def factorial():
    num = int(input("Enter the number: "))
    factorial = 1
    if num < 0:
        print("Factorial is not defined for negative numbers")
    else:
        for i in range(1, num+1):
            factorial = factorial*i
        print("The factorial of", num, "is", factorial)

while True:
    factorial()
    a = input("Do you want to continue (YES/NO): ")
    if a.lower() == "yes":
        continue
    elif a.lower() == "no":
        print("Thank You!")
        break
    else:
        print("Invalid input, continuing...")