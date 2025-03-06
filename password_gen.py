import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive number.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
        
        again = input("Generate another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
