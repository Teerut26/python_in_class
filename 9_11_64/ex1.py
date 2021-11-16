import math
x1 = int(input("x1 : "))
x2 = int(input("x2 : "))
y1 = int(input("y1 : "))
y2 = int(input("y2 : "))

pos1 = ((x1 - x2) ** 2 )
pos2 = ((y1 - y2) ** 2 )
distance = math.sqrt(pos1+pos2)
print(distance)