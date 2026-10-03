def FactorialOfN(e):
    one = 1
    count = e + 1
    factorial = 1
    while True:
        count -= 1
        if count == one:
            break
        factorial = factorial * count
    return factorial


num = int(input('Enter a number to find its factorial: '))
print(FactorialOfN(num))



