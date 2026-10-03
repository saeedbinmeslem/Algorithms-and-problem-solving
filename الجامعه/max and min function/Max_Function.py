num = [5,4,2,3,1,6]

def maxnum(num):
    biggest = num[0]
    for i in num:
        if i > biggest:
            biggest = i
    return biggest
   


print(maxnum(num))