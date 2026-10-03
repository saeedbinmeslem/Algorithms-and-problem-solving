def VaildAge(age):
    while True:    
        if age > 18 and age < 45:
            return "Vaild age"
        else:
            age = int(input('How old are you? '))

age = int(input('How old are you? '))
print(VaildAge(age))