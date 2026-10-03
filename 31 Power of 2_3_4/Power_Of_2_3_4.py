def PowerOf234(e):
    power = 1
    powerOf = []
    for i in range(3):
        power += 1
        result = e ** power
        powerOf.append(result)
    return powerOf      
        
num = int(input('Enter a number to find the power of 2,3,and 4: '))

print(PowerOf234(num))