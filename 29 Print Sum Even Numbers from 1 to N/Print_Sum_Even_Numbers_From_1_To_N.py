def PrintSumEvenNumbersFrom1ToN(e):
    sum = 0
    count = e + 1
    for i in range(count):
        if i % 2 == 0:
            sum = sum + i
        else:
            None
    return sum


num = int(input('Enter a number: '))

print(PrintSumEvenNumbersFrom1ToN(num))