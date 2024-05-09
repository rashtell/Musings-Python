import json
import random
import sys

# Function to generate a random 10-digit string
def generate_random_string(num_length):
    return ''.join(random.choices('0123456789', k=num_length))

def generate_random_strings(num_length, num_strings):
    # Generate random strings
    random_strings = [generate_random_string(num_length) for _ in range(num_strings)]
    return random_strings

if __name__ == "__main__":
    print(sys.argv)

    # Check if the number of command line arguments is correct
    if len(sys.argv) != 3:
        print("Usage: python virtual-account-generator.py <length_of_string> <number_of_strings>")
        sys.exit(1)

    # Get the number of strings from command line argument
    try:
        num_length = int(sys.argv[1])
        num_strings = int(sys.argv[2])
    except ValueError:
        print("Invalid number of strings")
        sys.exit(1)

    # Generate random strings
    random_strings = generate_random_strings(num_length, num_strings)

    # Store the strings in a JSON array
    json_array = json.dumps(random_strings)

    print(json_array)
