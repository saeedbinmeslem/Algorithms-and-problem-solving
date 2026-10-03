def Prime(n):
    count = 1
    while True:
        if n <= 0:
            n = int(input("Please, Do not enter a number lower than 1.\nEnter a number again: "))
        else:
            if n == 1:
                return "It is NOT a Prime Number"
            else:
                while True:
                    if count >= n/2:
                        return "It is a Prime Number"
                    else:
                        count = count + 1
                        if n % count == 0:
                            return "It is NOT a Prime Number"
                    
                
num = int(input('Enter an intger number: '))

print(Prime(num))