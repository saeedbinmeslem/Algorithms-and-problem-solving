def addElement(array,element):
    array[len(array):] = [element]

def addArray(array,EnteredArray):
    array[len(array):] = EnteredArray    

# first way
def FromOneToN(e):
    Numbers = []
    for i in range(1,e + 1):
        addElement(Numbers,i)
    return Numbers

# second way
def PrintNumbersFrom1ToN(e):
    count = 0
    Numbers = []
    for i in range(e):
        count += 1
        addElement(Numbers,count)
    return Numbers     