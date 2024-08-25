# workhard_TRYhard
Repository of the challenge #6
## Add the required exceptions in the Reto 1 code assigments.
### 1.1
```python
def basic_operations(a: float, b: float, operation: str):
    """Perform basic arithmetic operations based on the given operation."""
    try:
        # Determine the operation to be performed
        if operation == "+":
            print(f"The sum of {a} and {b} is: {a + b}")
        elif operation == "-":
            print(f"The subtraction of {b} from {a} is: {a - b}")
        elif operation == "*":
            print(f"The multiplication of {a} and {b} is: {a * b}")
        elif operation == "/":
            if b == 0:  # Check for division by zero
                raise ZeroDivisionError("Division by zero is not allowed.")
            print(f"The division of {a} by {b} is: {a / b}")
        elif operation == "Todas":
            # Perform and print all operations
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            print(f"Sum: {a + b}\nSubtraction: {a - b}\nMultiplication: {a * b}\nDivision: {a / b}")
        else:
            raise ValueError("Invalid operation.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Define variables and get user input
        a = input("Enter a real number: ")
        b = input("Enter another real number: ")

        # Validate if inputs are valid real numbers
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise ValueError("Please enter valid real numbers.")

        # List of valid operations
        l_operations = ["+", "-", "*", "/", "Todas"]

        # Get the operation from the user
        operation = input("What operation would you like to perform with these two numbers?\n"
                          "Enter + for addition\n"
                          "Enter - for subtraction\n"
                          "Enter * for multiplication\n"
                          "Enter / for division\n"
                          "Enter 'Todas' to perform all operations.\n")
        
        # Validate if the operation is valid
        while operation not in l_operations:
            operation = input("Please enter a valid operation: ")

        # Perform the operation
        basic_operations(a, b, operation)

    except ValueError as e:
        print(e)
```
### 1.2
```python
def palindrome(W_list):
    try:
        # Check if the word is a palindrome by comparing it with its reversed version
        if W_list == W_list[::-1]:
            print("The word is a palindrome")
        else:
            print("The word is not a palindrome")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        word = input("Enter a word to check if it's a palindrome: ")
        if not word.isalpha():
            raise ValueError("Please enter only alphabetic characters.")
        
        # Convert the word to a list of characters, converting to lowercase for case insensitivity
        W_list = list(word.lower())
        palindrome(W_list)
    except ValueError as e:
        print(e)
```
### 1.3 
```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(N_list):
    """Return a list of prime numbers from a list of integers."""
    P_list = []
    for n in N_list:
        if is_prime(n):
            P_list.append(n)
    return P_list

if __name__ == "__main__":
    try:
        N_list = []
        cant = int(input("Enter the number of elements in your list: "))
        
        if cant <= 0:
            raise ValueError("The number of elements must be a positive number.")
        
        # Collect elements for the list
        for i in range(cant):
            while True:
                try:
                    num = int(input(f"Element {i+1} -> "))
                    if num < 0:
                        raise ValueError("Please enter a non-negative integer.")
                    N_list.append(num)
                    break
                except ValueError as e:
                    print(e)

        primes_in_list = primes(N_list)
        print(f"The prime numbers in the list {N_list} are {primes_in_list}")
    
    except ValueError as e:
        print(e)
```
### 1.4
```python
def biggest_addition(N_list):
    # Check if the list has at least two elements
    if len(N_list) < 2:
        raise ValueError("The list must contain at least two elements.")
    
    A_list = []  # List to store all the consecutive sums
    counter = 0
    
    # Iterate through the list and sum consecutive elements
    while counter < len(N_list) - 1:
        n = N_list[counter] + N_list[counter + 1]
        A_list.append(n)
        counter += 1
    
    # Find the maximum sum in the list
    biggest = max(A_list)
    return biggest

if __name__ == "__main__":
    try:
        N_list = []
        cant = int(input("Enter the number of elements in your list: "))
        
        if cant <= 0:
            raise ValueError("The number of elements must be a positive number.")
        
        # Collect elements for the list
        for i in range(cant):
            while True:
                try:
                    num = int(input(f"Element {i+1} -> "))
                    N_list.append(num)
                    break
                except ValueError:
                    print("Please enter a valid integer.")
        
        print(f"The list you entered is: {N_list}")
        
        result = biggest_addition(N_list)
        print(f"The largest sum of consecutive elements is: {result}")
    
    except ValueError as e:
        print(e)
```
### 1.5
```python
def find_anagrams(W_list):
    """Find and return all pairs of anagram words from the list."""
    Ord_list = []
    
    # Iterate through each word in the list
    for i in range(len(W_list)):
        for j in range(i + 1, len(W_list)):
            # Convert words to lists of characters and sort them
            sorted_word1 = sorted(W_list[i].lower())  # Convert to lowercase to avoid case sensitivity
            sorted_word2 = sorted(W_list[j].lower())
            
            # Check if sorted characters of both words match
            if sorted_word1 == sorted_word2:
                # Add both words to the result list if they are anagrams
                if W_list[i] not in Ord_list:
                    Ord_list.append(W_list[i])
                if W_list[j] not in Ord_list:
                    Ord_list.append(W_list[j])
    
    return Ord_list

if __name__ == "__main__":
    try:
        W_list = []
        cant = int(input("Enter the number of elements in your list: "))
        
        if cant <= 0:
            raise ValueError("The number of elements must be a positive number.")
        
        # Collect words from user input
        for i in range(cant):
            word = input(f"Element {i + 1} -> ").strip()
            if not word.isalpha():
                raise ValueError("Please enter only words with alphabetic characters.")
            W_list.append(word)
        
        # Find and print anagrams from the list
        anagrams = find_anagrams(W_list)
        if anagrams:
            print(f"The words with the same characters are: {anagrams}")
        else:
            print("No words with the same characters were found.")

    except ValueError as e:
        print(e)
```
# Pckage shape with exceptions 
## Point
```python
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
```
## Line
```python
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
```
## Rectangle 
```python
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
```
