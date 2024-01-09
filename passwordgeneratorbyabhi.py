import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, symbols=True):
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if not any([uppercase, lowercase, digits, symbols]):
        print("Please enable at least one character type.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the length of the password: "))
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        password = generate_password(length, uppercase, lowercase, digits, symbols)
        
        if password:
            print("Generated Password:", password)
        else:
            print("Password generation failed.")
    
    except ValueError:
        print("Invalid input. Please enter a valid length.")

if __name__ == "__main__":
    main()
