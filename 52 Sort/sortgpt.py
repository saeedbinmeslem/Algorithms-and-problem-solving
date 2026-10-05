# Enter number of elements: 5

# Enter element 1: 7
# Enter element 2: 2
# Enter element 3: 9
# Enter element 4: 1
# Enter element 5: 4

# Original Array:
# [7, 2, 9, 1, 4]

# Sorted Array:
# [1, 2, 4, 7, 9]

import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def length(array):
    count = 0
    for i in array:
        count = count + 1
    return count   

def addElementToArray(array,element):
    array[length(array): ] = [element]
    return array

def SortBig(array):
    for i in range(length(array)):
        swapped = False
        for j in range(length(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
            else:
                continue

        if swapped == False:
            break
    return array


def main():
    clear()
    while True:  
        try:
            number = int(input('how many element do you want to add to list\nnotice: most be an integer number: '))
            break
        except ValueError:
            print("we said an integer number.....")
            time.sleep(3)
            clear()
            continue
        
    clear()
    original = []
    for i in range(1,number + 1):
        while True:    
            try:
                num = int(input(f"Enter Element {i}: "))
                break
            except ValueError:
                print("Enter an integr number...")
                continue
        addElementToArray(original,num)
    clear()    
    print(f"original array: {original}\n")
    time.sleep(3)

    return f"And this after sorted: {SortBig(original)}"


print(main())

    

