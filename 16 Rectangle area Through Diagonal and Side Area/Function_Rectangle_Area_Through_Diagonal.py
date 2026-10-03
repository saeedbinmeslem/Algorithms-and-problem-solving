def rectangleAreaByDiagonal(a,d):
    Area = a * ((d** 2 - a ** 2) ** .5 )
    return 'the rectangle area is ' + str(Area)


a = float(input('Enter a number: '))
Diagonal = float(input('Enter the Diagonal: '))

print(rectangleAreaByDiagonal(a,Diagonal))
