# Take input from the user
num = int(input("Enter a number: "))

# Store the original number for comparison
temp = num
digit_sum = 0

# Find the total number of digits
num_digits = len(str(num))

# Calculate the sum of the powers of its digits
while temp > 0:
    digit = temp % 10          # Extracts the last digit
    digit_sum += digit ** num_digits  # Raises digit to power and adds to sum
    temp //= 10                # Removes the last digit

# Output the result
if num == digit_sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
