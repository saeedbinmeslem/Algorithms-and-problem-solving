# this function to add new element in array
def addElement(array,element):
    array[len(array):] = [element]

# this function to print numbers that from that number enterd by user to 1
def PrintNumbersFromNTo1(e):
    one = 1
    count = e + 1
    Numbers = []
    while True:
        if count == one:
            break
        count -= 1
        addElement(Numbers,count)
    return Numbers


# this function to print even numbers that from number enterd by user to 0
def PrintEvenNumbersFromNTo0(e):
    zero = 0
    count = e + 1
    EvenNumbers = []
    while True:
         count -= 1
         if count == zero:
             break
         if count % 2 == zero:
             addElement(EvenNumbers,count)
         else:
             None
    return EvenNumbers               

num = int(input('Enter a number: '))

print(PrintNumbersFromNTo1(num))
print(PrintEvenNumbersFromNTo0(num))