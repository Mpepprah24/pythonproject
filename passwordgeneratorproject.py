print("Password Generator")
print("If you need help coming up with a password you have came to the right place")

import random
import string

def generate_password(length=10):
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a pool of characters to choose from
    pool = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password by randomly selecting characters from the pool
    password = random.choices(pool, k=length)

    # Convert the password list into a string
    password = ''.join(password)

    return password

# Example usage
generated_password = generate_password()
print(generated_password)
