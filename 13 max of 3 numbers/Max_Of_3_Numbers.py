num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))
num3 = float(input('Enter a number: '))


if num1 > num2:
    if num1 > num3:
        print(int(num1))   
    else:
        print(int(num3))
else:
    if num2 > num3:
        print(int(num2))
    else:
        print(int(num3))
if num1 == num2 == num3:
    print('all have the same value')
elif num1 == num2:
    print('nam1 and num2 are the same')
elif num1 == num3:
    print('num1 and num3 are the same')
elif num2 == num3:
    print('num2 and num3 are the same')    
                                        