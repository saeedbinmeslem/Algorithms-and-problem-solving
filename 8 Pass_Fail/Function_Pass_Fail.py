def Pass(s):
    if s >= 50:
        return "PASS"
    else:
        return "FAIL"

mark = float(input('Enter your mark: '))
print(mark)
print(Pass(mark))