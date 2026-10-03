# Create an algorithm and a flowchart that
# will compute the sum of two numbers. If the
# sum is below or equal to 20, two
# numbers will be entered again. If the sum is
# above 20, it will display the sum


def sumof2numbers(a,b):
    while True:
        if a + b > 20:
            result = a + b
            return result
        else:
            print('the sum of numbers must be above than 20, please enter the numbers again: ')
            a = float(input("Enter number a: "))
            b = float(input("Enter number b: "))

a = float(input("Enter number a: "))
b = float(input("Enter number b: "))

print(sumof2numbers(a,b))

            

