import math

shape = input('Please enter the shape of the building: square, rectangle, or round. ')

if shape == 'Square' or shape == 'square': 
    side_len = float(input('Enter the length of one side of the building: '))
    area_sq = side_len*side_len
    print(round(area_sq, 2))

if shape == 'Rectangle' or shape == 'rectangle':
    length = float(input('Enter the lenght of the building: '))
    width = float(input('Enter the width of the building: '))
    area_rec = length*width 
    print(round(area_rec, 2))

if shape == 'Round' or shape == 'round': 
    radius = float(input('Enter the length of the radius of the circle: '))
    area_circ = (radius**2)*math.pi
    print(round(area_circ, 2))