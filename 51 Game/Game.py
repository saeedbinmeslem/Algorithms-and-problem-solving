import time
import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def Agree():
    clear()
    massage = str(input("Do you want to be active in this activity? \n(please answer yes / no) :")).strip().lower()
    while True:
        if massage.isalpha():        
            if massage == "yes":
                return Game_Activty()
            elif massage == "no":
                return "ok , have a nice day"
            else:
                massage = str(input("please insert (yes / no): ")).strip().lower()
        else:
            print("don't joke, just insert (yes / no)")
            time.sleep(3)
            clear()
            massage = str(input("Do you want to be active in this activity? \n(please answer yes / no) :")).strip().lower()        
def Game_Activty():
    clear()
    print("We want two numbers their total are 20")
    time.sleep(3)
    clear()
    while True:
        try:
            a = int(input("insert the first number: "))
            clear()
            b = int(input("insert the second number: "))
            clear()
        except ValueError:
            clear()
            print("insert integer numbers ...")
            time.sleep(3)
            clear()
            continue
        result = a + b    
        if result == 20:
            return f"correct {a} + {b} = {result}\nhave a greatful day"
        else:
            print("no! try again")
            time.sleep(2)
            clear()
print(Agree())