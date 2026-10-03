# sum until enter -99

def sumUntil(n):
    sum = 0
    while True:
        if n == -99:
            break
        else:
            sum = n + sum
            n = float(input("Enter a number: "))

    return sum

num = float(input("Enter a number: "))        
print(sumUntil(num))