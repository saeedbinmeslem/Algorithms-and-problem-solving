# mark1 = float(input('enter your mark1: '))
# mark2 = float(input('enter your mark2: '))
# mark3 = float(input('enter your mark3: '))
# mark4 = float(input('enter your mark4: '))
# mark5 = float(input('enter your mark5: '))
# mark6 = float(input('enter your mark6: '))
# mark7 = float(input('enter your mark7: '))
# mark8 = float(input('enter your mark8: '))



# marks = [mark1,mark2,mark3,mark4,mark5,mark6,mark7,mark8]
movies = [65,54,21,52,65,522,71]
series = [75,54,80,52,65,522,71]

def sumaverage(s):
    sum = 0
    Average = 0
    for i in s:
        sum = sum + i
        Average += 1
    return sum/Average  

print(int(sumaverage(series)))