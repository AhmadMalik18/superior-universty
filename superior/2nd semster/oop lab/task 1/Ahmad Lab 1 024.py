import math

def is_prime(number):
    """
    Check whether a given number is prime or not.
    
    Parameters:
    number (int): The number to be checked.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True

def main():
    while True:
        try:
            # Ask the user to input a number
            num = int(input("Enter a number (or type '0' to exit): "))
            
            if num == 0:
                print("Exiting the program.")
                break
            
            # Call the is_prime() function and display the result
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Run the main function to start the program
if __name__ == "__main__":
    main()
    
