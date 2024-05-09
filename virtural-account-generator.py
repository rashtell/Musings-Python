import json
import random

# Function to generate a random 10-digit string
def generate_random_string():
    return ''.join(random.choices('0123456789', k=10))

# Generate 1000 random strings
random_strings = [generate_random_string() for _ in range(1000)]

# Store the strings in a JSON array
json_array = json.dumps(random_strings)

print(json_array)
