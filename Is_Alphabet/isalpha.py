# function calculate the length of array or strings

def length(array):
    count = 0
    for i in array:
        count = count + 1
    return count


# function use to add add element to array

def addElementToArray(array,element):
    array[length(array) : ] = [element]
    return array


# function add all alphabets in array

def alphabet():
    smallletter = 96
    alphabetletters = [" "]
    for i in range(26):
        smallletter = smallletter + 1
        letter = chr(smallletter)
        addElementToArray(alphabetletters,letter)
    capitalletter = 64
    for i in range(26):
        capitalletter = capitalletter + 1
        letter = chr(capitalletter)
        addElementToArray(alphabetletters,letter)
    return alphabetletters        


# functoin test statements if contian any data not alphabet or not
# if contain return False, else return True

def isalphabet(statement):
    elements = []
    for i in statement:
        addElementToArray(elements,i)
    check = True
    for i in elements:
        for j in range(length(alphabet())):
            if i == alphabet()[j]:
                check = True
                break
            else:
                check = False
        if check == False:
            return False
    return True



element ="saeed mohammed saeed abood bin musllam"
print(isalphabet(element))  
