class Point:
    def __init__(self, given_x: float = 0, given_y: float = 0):
        # Check if initial values are numeric (either int or float)
        if not isinstance(given_x, (int, float)) or not isinstance(given_y, (int, float)):
            # Raise an error if the coordinates are not numbers
            raise ValueError("Coordinates must be numbers.")
        # Assign the valid numeric values to the instance variables
        self.x = given_x
        self.y = given_y

    def move(self, new_x: float, new_y: float):
        # Check if the new coordinates are numeric (either int or float)
        if not isinstance(new_x, (int, float)) or not isinstance(new_y, (int, float)):
            # Raise an error if the new coordinates are not numbers
            raise ValueError("New coordinates must be numbers.")
        # Update the point's position with the valid new coordinates
        self.x = new_x
        self.y = new_y

    def reset(self):
        # Reset the point's coordinates to the origin (0, 0)
        self.x = 0
        self.y = 0
