import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """
    Generates a secure, random password.
    
    Args:
        length (int): The desired length of the password.
        use_uppercase (bool): Whether to include uppercase letters.
        use_digits (bool): Whether to include digits (0-9).
        use_symbols (bool): Whether to include symbols (e.g., @, #, $).
    """
    
    # 1. Start with a base character set (lowercase letters)
    char_pool = list(string.ascii_lowercase)
    
    # 2. Add other character types to the pool based on user's choice
    if use_uppercase:
        char_pool.extend(string.ascii_uppercase)
    if use_digits:
        char_pool.extend(string.digits)
    if use_symbols:
        char_pool.extend(string.punctuation)
        
    # Ensure the pool isn't empty if all options are False
    if not char_pool:
        print("Error: At least one character type must be selected.")
        return None

    # 3. Shuffle the pool to make the selection more random
    random.shuffle(char_pool)
    
    # 4. Build the password
    password = []
    for _ in range(length):
        # Pick a random character from the pool and add it to the password list
        random_char = random.choice(char_pool)
        password.append(random_char)
        
    # 5. Join the list of characters into a final string and return it
    return "".join(password)

# --- Main part of the script ---
if __name__ == "__main__":
    try:
        # Get password length from the user
        pass_length = int(input("Enter desired password length (e.g., 16): "))
        
        # You could also ask the user for the other options (True/False)
        
        # Generate the password
        new_password = generate_password(
            length=pass_length, 
            use_uppercase=True, 
            use_digits=True, 
            use_symbols=True
        )
        
        if new_password:
            print("-" * 30)
            print(f"Your new secure password is:")
            print(f"  {new_password}")
            print("-" * 30)
            
    except ValueError:
        print("Invalid input. Please enter a number for the length.")