#Task 1 calculate area and hypo
import math

height = int(input('Enter first side: '))
base = int(input('Enter second side: '))

x = height**2 + base**2
math.sqrt(x)
print(x)

area = int((1/2)*base*height)
print(bin(area))


#Task 2

numbers = [2,56,12,67,1000, 32,89,29,44,39,200,11,21]
print(max(numbers))
print(min(numbers))

