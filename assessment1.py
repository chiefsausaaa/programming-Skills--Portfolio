# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function
def main():
    # Ask the user for a number
    user_input = int(input("Enter a number: "))
    
    # Pass the number to the function and store the result
    result_message = check_even_odd(user_input)
    
    # Print the result message
    print(result_message)

# Run the main function
main()
