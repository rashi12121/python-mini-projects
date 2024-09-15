import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special = string.punctuation if include_special else ''
    
    # Combine character sets
    characters = lowercase + uppercase + digits + special
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Ensure password meets criteria
    if include_uppercase and not any(c.isupper() for c in password):
        password = password[:length-1] + random.choice(uppercase)
    if include_digits and not any(c.isdigit() for c in password):
        password = password[:length-1] + random.choice(digits)
    if include_special and not any(c in special for c in password):
        password = password[:length-1] + random.choice(special)
    
    return password

def main():
    print("Welcome to the Enhanced Password Generator!")
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    # Generate and display the password
    password = generate_password(length, include_uppercase, include_digits, include_special)
    print(f"Generated password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
