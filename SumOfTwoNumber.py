# Sum Of Two Numbers Program

num1= int(input("Enter Number :"))
num2= int(input("Enter Number : "))
print(f"Sum of {num1} + {num2} = {num1+ num2}")

# Sum of two Number Using Functions
def sumOfTwoNum(a: int, b: int):
    return a+ b

print(sumOfTwoNum(10, 20))


# Using try And except Bloccks
def SumOfTwoNum(a: int, b: int):
    return a+ b

while True:
    try:
        num1= int(input("Enter Number :"))
        num2= int(input("Enter Number :"))
        print(f"Sum of {num1} + {num2} = {SumOfTwoNum(num1, num2)}")
        break
    except ValueError:
        print("Please Enter Valid Number")