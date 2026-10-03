def Commission_Percentage(e):
    Percentage = 0
    if e >= 1000000:
        Percentage = .01
    elif e >= 500000:
        Percentage = .02
    elif e >= 100000:
        Percentage = .03
    elif e >= 50000:
        Percentage = .05
    else:
        Percentage = 0

    TotalCommission = e * Percentage
    return TotalCommission


num = int(input('Enter your total sale: '))
print(Commission_Percentage(num))
