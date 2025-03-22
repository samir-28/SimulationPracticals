def mid_square_method(seed: int, count: int):
    """Generates pseudo-random numbers using the Mid-Square Method."""
    n_digits = len(str(seed))  # Determine the number of digits in seed
    current_number = seed
    random_numbers = []

    for i in range(count):
        squared_number = current_number ** 2  # Square the number
        squared_str = str(squared_number).zfill(2 * n_digits)  # Zero-padding ensures at least 2n digits
        mid_index = len(squared_str) // 2  # Find middle index
        new_number = int(squared_str[mid_index - n_digits // 2 : mid_index + n_digits // 2])  # Extract n middle digits
        
        # Handle zero case (to prevent getting stuck at 0)
        if new_number == 0:
            print("Generated a zero! Stopping early to avoid repetition.")
            break
        
        random_numbers.append(new_number)
        current_number = new_number  # Update for next iteration

    return random_numbers


# Input from user 

seed_value = int(input("Enter the seed value (n-digit number): "))
count = int(input("Enter how many random numbers you want to generate: "))

# Generate numbers using the Mid-Square Method
random_sequence = mid_square_method(seed_value, count)

# Display results
print("\nGenerated Random Numbers[Samir Bajgain]:")
print(", ".join(f"x{i}={num}" for i, num in enumerate(random_sequence)))
