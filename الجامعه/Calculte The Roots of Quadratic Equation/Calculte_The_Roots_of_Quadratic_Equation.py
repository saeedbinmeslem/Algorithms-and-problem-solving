def squrt(d):
    result = d ** 0.5
    return result

def Roots(a,b,c):
    d = squrt((b ** 2 ) - (4 * a * c))
    Theroots = [(-b - d)/(2 * a),(-b +d)/ (2 * a)]

    return Theroots

num1 = float(input('Enter a: '))
num2 = float(input('Enter b: '))
num3 = float(input('Enter c: '))

print(Roots(num1,num2,num3))
