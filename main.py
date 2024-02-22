# Importing classes from shapes.py
from shapes import Rectangle, Circle

# Function to print details of a shape
def print_details(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Instantiating objects of Rectangle and Circle
rectangle = Rectangle(4, 6)
circle = Circle(5)

# Demonstrate polymorphism by calling print_details() with instances of both Rectangle and Circle
print("Details of Rectangle:")
print_details(rectangle)

print("\nDetails of Circle:")
print_details(circle)
