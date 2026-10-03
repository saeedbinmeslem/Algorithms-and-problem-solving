age = int(input("How old are you? "))

# نعرف المتغير مبدئياً
drive_license = None 

# حلقة تكرار تجبر المستخدم على اختيار 1 أو 2 فقط
while True:
    print("Do you have a driving license?")
    print("1: Yes")
    print("2: No")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        drive_license = True # هنا أخذها كـ Boolean حقيقي
        break # نخرج من الحلقة
    elif choice == '2':
        drive_license = False # هنا أخذها كـ Boolean حقيقي
        break # نخرج من الحلقة
    else:
        print("Invalid choice. Please type 1 or 2 only.\n")

# الآن المتغير drive_license يحمل قيمة منطقية (True أو False)
if age > 21 and drive_license == True:
    print("hired")
else:
    print("Rejected")