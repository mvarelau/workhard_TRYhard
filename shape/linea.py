from punto import Point

class Line:
    def __init__(self, start: Point, end: Point):
        try:
            # Check if the start and end points are instances of the Point class
            if not isinstance(start, Point) or not isinstance(end, Point):
                # Raise an error if the inputs are not valid Point instances
                raise TypeError("Start and end points must be instances of the Point class.")
            # Assign the valid points to the instance variables
            self.start = start
            self.end = end
        except TypeError as e:
            # Handle the error by printing a message and assigning default points
            print(f"Error in __init__: {e}")
            self.start = Point()  # Assign default points if an error occurs
            self.end = Point()

    def compute_length(self) -> float:
        try:
            # Calculate the length of the line segment using the distance formula
            length = (((self.end.x - self.start.x) ** 2) + ((self.end.y - self.start.y) ** 2)) ** 0.5
            return length
        except Exception as e:
            # Handle any unexpected errors during the length calculation
            print(f"Error in compute_length: {e}")
            return 0.0  # Return 0.0 as a fallback value if an error occurs

    def compute_slope(self) -> float:
        try:
            # Check if the x-coordinates are the same, which would result in an undefined slope
            if self.end.x == self.start.x:
                raise ZeroDivisionError("The slope is undefined (division by zero).")
            # Calculate the slope of the line
            slope = (self.end.y - self.start.y) / (self.end.x - self.start.x)
            return slope
        except ZeroDivisionError as e:
            # Handle the case where the slope is undefined (vertical line)
            print(f"Error in compute_slope: {e}")
            return float('inf')  # Return infinity to indicate an undefined slope
        except Exception as e:
            # Handle any other unexpected errors during the slope calculation
            print(f"Error in compute_slope: {e}")
            return None  # Return None as a fallback value for unexpected errors
