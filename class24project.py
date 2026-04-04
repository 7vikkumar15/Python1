import random
import string

def generate_password(length=10):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits

    # Combine all characters
    all_chars = lowercase + uppercase + numbers

    # Ensure at least one from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers)
    ]

    # Fill the remaining length
    for _ in range(length - 3):
        password.append(random.choice(all_chars))

    # Shuffle the password
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Generate and print password
print("Generated Password:", generate_password(12))