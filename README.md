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

