# Create an algorithm and a flowchart
# that will output the largest number
# among the three numbers.
def biggestof3(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


def biggestNumber(array):
    biggest = array[0]
    for i in array:
        if i > biggest:
            biggest = i

    return biggest        

print(biggestof3(12,15,46))
print(biggestNumber([12,15,64,45,48,351,10,0,151231531,45]))
print(max([12,15,64]))
