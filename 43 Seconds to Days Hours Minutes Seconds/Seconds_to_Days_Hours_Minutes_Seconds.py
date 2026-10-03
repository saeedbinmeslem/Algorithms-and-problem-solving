def ToSeconds(seconds):
    month = 60 * 60 * 24 * 30
    days = 60 * 60 * 24
    hours = 60 * 60
    minutes = 60

    manyMonth = int(seconds / month)
    modMonth = seconds - month * manyMonth

    manyDays = int(modMonth / days)
    modDays = modMonth - days * manyDays

    manyHours = int(modDays / hours)
    modHours = modDays - hours * manyHours

    manyMinutes = int(modHours / minutes)
    modMinutes = modHours - minutes * manyMinutes

    manyseconds = modMinutes

    return str(manyMonth) + ":" + str(manyDays) + ":" + str(manyHours) + ":" + str(manyMinutes) + ":" + str(manyseconds)


seconds = int(input("Enter seconds to show how many\ndays,hours,minutes, and seconds include it: "))
print(ToSeconds(seconds))


