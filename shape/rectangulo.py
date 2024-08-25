from punto import Point
from linea import Line

class Rectangle:
    def __init__(self, method: int, *args):
        try:
            if method == 1:
                # Method 1: Construct a rectangle from the bottom-left point, width, and height
                bottom_left = args[0]
                width = args[1]
                height = args[2]
                
                # Validate the types of the arguments
                if not isinstance(bottom_left, Point) or not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                    raise ValueError("Invalid arguments for method 1.")
                
                # Calculate the center based on the bottom-left corner, width, and height
                self.center = Point(
                    given_x=bottom_left.x + width / 2,
                    given_y=bottom_left.y + height / 2
                )
                self.width = width
                self.height = height

            elif method == 2:
                # Method 2: Construct a rectangle from the center point, width, and height
                center = args[0]
                width = args[1]
                height = args[2]
                
                # Validate the types of the arguments
                if not isinstance(center, Point) or not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                    raise ValueError("Invalid arguments for method 2.")
                
                # Assign values directly
                self.center = center
                self.width = width
                self.height = height

            elif method == 3:
                # Method 3: Construct a rectangle from two diagonal points
                point1 = args[0]
                point2 = args[1]
                
                # Validate that both arguments are Point instances
                if not isinstance(point1, Point) or not isinstance(point2, Point):
                    raise ValueError("Invalid arguments for method 3.")
                
                # Calculate the center, width, and height based on the diagonal points
                self.center = Point(
                    given_x=(point1.x + point2.x) / 2,
                    given_y=(point1.y + point2.y) / 2
                )
                self.width = abs(point2.x - point1.x)
                self.height = abs(point2.y - point1.y)

            elif method == 4:
                # Method 4: Construct a rectangle from two opposite sides (lines)
                line1 = args[0]
                line3 = args[2]
                
                # Validate that both arguments are Line instances
                if not isinstance(line1, Line) or not isinstance(line3, Line):
                    raise ValueError("Invalid arguments for method 4.")
                
                # Calculate the center based on the start of line1 and the end of line3
                self.center = Point(
                    given_x=(line1.start.x + line3.end.x) / 2,
                    given_y=(line1.start.y + line3.end.y) / 2
                )
                self.width = line1.compute_length()
                self.height = line3.compute_length()

            else:
                # Raise an error if the method value is invalid
                raise ValueError("Invalid method.")

        except (IndexError, ValueError) as e:
            # Handle exceptions for missing or invalid arguments
            print(f"Error in __init__: {e}")
            # Set default values in case of an error
            self.center = Point()
            self.width = 0
            self.height = 0

    def compute_area(self) -> float:
        try:
            # Calculate the area of the rectangle
            return self.width * self.height
        except Exception as e:
            # Handle any unexpected error during the calculation
            print(f"Error in compute_area: {e}")
            return 0.0  # Return 0 as a safe fallback value

    def compute_perimeter(self) -> float:
        try:
            # Calculate the perimeter of the rectangle
            return 2 * (self.width + self.height)
        except Exception as e:
            # Handle any unexpected error during the calculation
            print(f"Error in compute_perimeter: {e}")
            return 0.0  # Return 0 as a safe fallback value

    def compute_interference_point(self, point: Point) -> bool:
        try:
            # Validate that the input is a Point instance
            if not isinstance(point, Point):
                raise ValueError("Argument must be an instance of Point.")
            
            # Calculate the boundaries of the rectangle
            left_x = self.center.x - self.width / 2
            right_x = self.center.x + self.width / 2
            bottom_y = self.center.y - self.height / 2
            top_y = self.center.y + self.height / 2
            
            # Check if the point lies within the rectangle
            return left_x <= point.x <= right_x and bottom_y <= point.y <= top_y
        except ValueError as e:
            # Handle invalid argument errors
            print(f"Error in compute_interference_point: {e}")
            return False  # Return False as a safe fallback
