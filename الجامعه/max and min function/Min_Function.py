num = [5,4,2,3,1,6]

def minnum(num):
    smallest = num[0]
    for i in num:
        if i < smallest:
            smallest = i
    return smallest


print(minnum(num))    