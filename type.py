print("===== Number Operations Program =====")

# Get user input
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert input
int_num1 = int(num1)
float_num2 = float(num2)

# Perform operations
addition = int_num1 + float_num2
subtraction = int_num1 - float_num2
multiplication = int_num1 * float_num2
division = int_num1 / float_num2

# Display results
print("\n----- Results -----")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Convert numeric value to string
num_string = str(int_num1)

# Print string value
print("\nNumeric value converted to string:", num_string)
print("Data type of converted value:", type(num_string))
