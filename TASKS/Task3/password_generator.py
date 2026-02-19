import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):

    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_special)
    
    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
