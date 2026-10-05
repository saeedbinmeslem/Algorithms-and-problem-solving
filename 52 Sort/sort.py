def length(array):
    count = 0
    for i in array:
        count = count + 1
    return count


def sortToBig(array):
    for i in range(length(array)):
        swapped = False
        for j in range(length(array) - 1 ):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if swapped == False:
            break               
    return array


def sortToSmall(array):
    for i in range(length(array)):
        swapped = False
        for j in range(length(array) - 1 ):
            if array[j] <  array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if swapped == False:
            break               
    return array
          

mark = [99.8,99.2,96,97,98.5,99.8,100]
print(sortToSmall(mark))
