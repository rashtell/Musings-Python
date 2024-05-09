import json
import random
import sys

# Function to generate a random 10-digit string
def generate_random_string():
    return ''.join(random.choices('0123456789', k=10))

def generate_random_strings(num_strings):
    # Generate random strings
    random_strings = [generate_random_string() for _ in range(num_strings)]
    return random_strings

if __name__ == "__main__":
    # Check if the number of command line arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python virtual-account-generator.py <number_of_strings>")
        sys.exit(1)

    # Get the number of strings from command line argument
    try:
        num_strings = int(sys.argv[1])
    except ValueError:
        print("Invalid number of strings")
        sys.exit(1)

    # Generate random strings
    random_strings = generate_random_strings(num_strings)

    # Store the strings in a JSON array
    json_array = json.dumps(random_strings)

    print(json_array)
