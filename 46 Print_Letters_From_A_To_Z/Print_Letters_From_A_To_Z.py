def length(array):
    count = 0
    for i in array:
        count = count + 1
    return count


def AddToArray(array,element):
    array[length(array) : ] = [element]
    return array


def CapitalLetter():
    count = 64
    result = []
    for i in range(26):
        count = count + 1
        letter = chr(count)
        AddToArray(result,letter)
    return result

def SmallLetter():
    count = 96
    result = []
    for i in range(26):
        count = count + 1
        letter = chr(count)
        AddToArray(result,letter)
    return result


print(SmallLetter())    
        
