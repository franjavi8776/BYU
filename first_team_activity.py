# area of the square
square_length = float(input("What is the length of a side of the square? "))
square_area = square_length  ** 2
print(f"The area of the square is: {square_area:.2f}")

# area of the rectangle
rectangle_length = float(input("What is the length of a rectangle? "))
rectangle_width = float(input("What is the width of a rectangle? "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rectangle_area:.2f}")

# area of the circle
circle_radius = float(input("What is the radius of a circle? "))
circle_area = 3.14 * (circle_radius ** 2)
print(f"The area of the circle is: {circle_area:.2f}")

# area of the circle with math.pi
circle_radius = float(input("What is the radius of a circle? "))
import math
circle_area = math.pi * (circle_radius ** 2)
print(f"The area of the circle is: {circle_area:.2f}")

print()

# all areas with the same value
value = float(input("What is the value? "))
square_area = value ** 2
circle_area = math.pi * (value ** 2)
cube_volume = value ** 3
sphere_volume = (4 / 3) * math.pi * (value ** 3)
print(f"The area of the square is: {square_area:.2f}")
print(f"The area of the circle is: {circle_area:.2f}")
print(f"The volume of the cube is: {cube_volume:.2f}")
print(f"The volume of the sphere is: {sphere_volume:.2f}")

print()

# area of the square in cm^2 and m^2
square_length = float(input("What is the length of a side of the square in cm? "))
square_area = square_length  ** 2
print(f"The area of the square is: {square_area:.2f} cm^2")
print(f"The area of the square is: {square_area/10000:.2f} m^2")

# area of the rectangle in cm^2 and m^2
rectangle_length = float(input("What is the length of a rectangle in cm? "))
rectangle_width = float(input("What is the width of a rectangle cm? "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rectangle_area:.2f} cm^2")
print(f"The area of the rectangle is: {rectangle_area/10000:.2f} m^2")

# area of the circle with math.pi in cm^2 and m^2
circle_radius = float(input("What is the radius of a circle in cm? "))
import math
circle_area = math.pi * (circle_radius ** 2)
print(f"The area of the circle is: {circle_area:.2f} cm^2")
print(f"The area of the circle is: {circle_area/10000:.2f} m^2")