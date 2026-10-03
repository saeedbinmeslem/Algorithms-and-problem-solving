def abslute(n):
    result = 0
    if n >= 0:
        result = n
    else:
        result = -n
    return result

def AddToArray(array,element):
    array[len(array): ] = [element]
    return array


def Evaluate():
    a = -8
    result = []
    for i in range(6):
        x = float(input('Enter x: '))
        if x >= 0:
            y = 3 * x ** 2 - abslute(x)
        else:
            y = x + a
        AddToArray(result,y)    
    return result


print(Evaluate())          