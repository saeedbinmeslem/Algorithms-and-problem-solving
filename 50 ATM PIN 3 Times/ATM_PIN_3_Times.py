def ATMPassWord(PassWord):
    balance = 7500
    count = 1
    while True:
        if PassWord == 1234:
            return balance
        else:
            if count == 3:
                return "ATM Locked"
            else:
                count = count + 1
                print('wrong PassWord')
                PassWord = int(input("Enter the PassWord: "))

PassWord = int(input("Enter the PassWord: "))
print(ATMPassWord(PassWord))