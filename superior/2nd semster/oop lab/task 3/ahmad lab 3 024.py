class Rectangle:
    def __init__(self, width, height):
        """
        Constructor method to initialize the width and height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Method to return a string representation of the rectangle in the format:
        "Rectangle: [width] x [height]"
        """
        return f"Rectangle: {self.width} x {self.height}"

    def area(self):
        """
        Method to calculate and return the area of the rectangle.
        Formula: width * height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method to calculate and return the perimeter of the rectangle.
        Formula: 2 * (width + height)
        """
        return 2 * (self.width + self.height)


# Main program to create a Rectangle object and perform operations
if __name__ == "__main__":
    # Get user input for width and height
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    # Create an instance of Rectangle
    rect = Rectangle(width, height)

    # Display rectangle details using __str__
    print(rect)

    # Calculate and display the area of the rectangle
    print(f"Area of the rectangle: {rect.area()}")

    # Calculate and display the perimeter of the rectangle
    print(f"Perimeter of the rectangle: {rect.perimeter()}")
