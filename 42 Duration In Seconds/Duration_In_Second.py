def Seconds(days,hours,minutes,seconds):
    days = days * 24 * 60 * 60
    hours= hours * 60 * 60
    minutes = minutes * 60
    result = days + hours + minutes + seconds

    return result


num1 = int(input("Enter days: "))
num2 = int(input("Enter hours: "))
num3 = int(input("Enter minutes: "))
num4 = int(input("Enter seconds: "))

print(Seconds(num1,num2,num3,num4))






