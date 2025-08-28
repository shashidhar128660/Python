length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = (2*(length + breadth))

print("The area of the rectangle is: ",area)
print("The perimeter of the rectangle is: ",perimeter)

number = int(input("Enter a number to check it is even or odd: "))
if number %2 == 0:
    print("Entered number if even number")
else:
    print("Entered number is odd number")
    
side = int(input("Enter the side length of th ecube: "))
area = 6 * (side * side)
volume = side * side * side
print("The area of the cube is: ",area)
print("The volume of the cube is: ",volume)

x = int(input("Give a value for x: "))
y = int(input("Give a value for y: "))
print("z = (x + y) * (x - y)")
z = (x + y) * (x - y)
print("z=",z)

x = int(input("Give a value for x: "))
y = int(input("Give a value for y: "))
z = ((x + y) * (x + y) - 2 * x * y)
print("z=(x+y)*(x+y)-2xy")
print("The calculated value of z is: ",z)

celcius = float(input("Enter the celcius: "))
fahrenheit = ((celcius * (9 / 5)) + 32)
print(f"{celcius} degree celcius in fahrenheit is: {fahrenheit}")

    
