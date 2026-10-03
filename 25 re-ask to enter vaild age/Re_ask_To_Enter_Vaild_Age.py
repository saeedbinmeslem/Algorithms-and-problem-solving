def VaildAge():
    while True:    
        age = int(input('How old are you? '))
        if age > 18 and age < 45:
            return "Vaild age"


print(VaildAge())