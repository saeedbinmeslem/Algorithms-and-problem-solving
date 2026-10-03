recommendation = None

while True:
    print('do you have recommendation? ')
    print('Enter y if Yes : ')
    print('Enter n if no : ')
    choise_recommendation = input('Enter y or n : ')
    if choise_recommendation == 'y':
        recommendation = True
        break
    elif choise_recommendation == 'n':
        recommendation = False
        break
    else:
        print('invaild value, please enter y or n ')

if recommendation == True:
    print('hired')
else:
    drive_license = None
    age = int(input('How old are you? '))
    while True:
        print('do you have drive license? ')
        print('enter y if yes')
        print('enter n if no')
        choise_drive_license = input('enter y or n : ')
        if choise_drive_license == 'y':
            drive_license = True
            break
        elif choise_drive_license == 'n':
            drive_license = False
            break
        else:
            print('invaild value, please enter y or n')

    result = int(age > 21) and drive_license == True
    if result:
        print('hired')
    else:
        print('Rejected')