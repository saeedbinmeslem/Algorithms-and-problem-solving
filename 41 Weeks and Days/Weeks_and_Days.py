def Hours(n):
    Day = n/24
    Week = Day / 7
    result = [str(Day) + " Day" , str(Week) + " Week"]
    return result

num = float(input("Enter the numbers of hours to see how many\ndays and weeks those hours equal: "))
print(Hours(num))