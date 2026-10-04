import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def user_options():
    while True:
        clear()
        L1 = "yes"
        L2 = "no"
        message = input("Do you want to be active in this activity?\n(please answer yes / no):").strip().lower()
        if message.isalpha():
            if message == L1:
                return True
            elif message == L2:
                return False
            else:
                print("please insert (yes / no)")
                time.sleep(3)
                clear()
        else:
            print("don't joke, just insert (yes / no)")
            time.sleep(3)
            clear()
def game_activity():
    while True:
        letter = "We want two numbers their total are 20"
        print(letter)
        time.sleep(3)
        clear()
        try:
            a = int(input("insert the first number: "))
            clear()
            b = int(input("insert the second number: "))
            clear()
            x = a + b
        except ValueError:
            clear()
            print("insert integer numbers ...")
            time.sleep(3)
            clear()
            continue
        if x == 20:
            print(f"correct! {a} + {b} = {x}")
            time.sleep(3)
            clear()
            print("have a greatful day")
            break
        else:
            print("no! try again")
            time.sleep(3)
            clear()
def main():
    if user_options():
        game_activity()
    else:
        print("ok, have a nice day")
main()