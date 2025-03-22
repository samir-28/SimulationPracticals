# Multiplicative Congruential Method (MCM) for Random Number Generation
def multiplicative_congruential_method(seed: int, multiplier: int, modulus: int, count: int):
    """Generates pseudo-random numbers using the Multiplicative Congruential Method."""
    random_numbers = []
    current_value = seed

    for _ in range(count):
        current_value = (multiplier * current_value) % modulus
        random_numbers.append(current_value)

    return random_numbers


# User input
seed_value = int(input("Enter the seed value: "))
multiplier = int(input("Enter the multiplier: "))
modulus = int(input("Enter the modulus: "))
num_count = int(input("How many random numbers to generate? "))

# Generate random numbers
random_sequence = multiplicative_congruential_method(seed_value, multiplier, modulus, num_count)

# Display results
print("\nGenerated Random Numbers[Samir Bajgain]:")
# print(", ".join(map(str, random_sequence)))
print(", ".join(f"x{i}={num}" for i, num in enumerate(random_sequence)))
