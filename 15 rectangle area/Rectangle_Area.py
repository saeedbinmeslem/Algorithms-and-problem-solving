high = float(input('Enter a high for the rectangle: '))
width = float(input('Enter a width for the rectangle: '))

def rectangleArea(h,w):
    Area = h * w
    return 'the rectangle area is ' + str(Area)

print(rectangleArea(high,width))