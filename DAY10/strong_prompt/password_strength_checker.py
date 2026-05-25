# Password Strength Checker Program
# This program checks how strong a password is based on specific criteria


'''prompt in github copilot (Claude Haiku 4.5) was like : 
Write a beginner-friendly Python program that checks password strength.

Requirements:
- Password should contain at least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number

Display:
- Weak Password
- Medium Password
- Strong Password

Add comments explaining each step.

make it on D:\DiyoAI_Intern_Tasks\DAY10\strong_Prompt_engineering folder '''




# Function to check password strength
def check_password_strength(password):
    """
    This function evaluates the strength of a password based on:
    - Length (at least 8 characters)
    - Uppercase letters (at least 1)
    - Lowercase letters (at least 1)
    - Numbers (at least 1)
    """
    
    # Initialize flags to track password criteria
    # These flags help us count how many criteria are met
    has_uppercase = False
    has_lowercase = False
    has_number = False
    
    # Check if password has at least 8 characters
    has_min_length = len(password) >= 8
    
    # Loop through each character in the password
    for char in password:
        # Check if character is an uppercase letter
        if char.isupper():
            has_uppercase = True
        
        # Check if character is a lowercase letter
        if char.islower():
            has_lowercase = True
        
        # Check if character is a number
        if char.isdigit():
            has_number = True
    
    # Count how many criteria the password meets
    criteria_met = 0
    
    if has_min_length:
        criteria_met += 1
    if has_uppercase:
        criteria_met += 1
    if has_lowercase:
        criteria_met += 1
    if has_number:
        criteria_met += 1
    
    # Determine password strength based on criteria met
    if criteria_met < 2:
        # Weak: meets less than 2 criteria
        strength = "Weak Password"
    elif criteria_met < 4:
        # Medium: meets 2 or 3 criteria
        strength = "Medium Password"
    else:
        # Strong: meets all 4 criteria
        strength = "Strong Password"
    
    # Return strength and details
    return strength, has_min_length, has_uppercase, has_lowercase, has_number


# Main program
def main():
    """
    Main function that runs the password strength checker program
    """
    
    print("=" * 50)
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    
    # Get password input from user
    password = input("\nEnter a password to check: ")
    
    # Call the function to check password strength
    strength, has_length, has_upper, has_lower, has_digit = check_password_strength(password)
    
    # Display the results
    print("\n" + "-" * 50)
    print("PASSWORD STRENGTH ANALYSIS")
    print("-" * 50)
    
    # Show criteria checks
    print("\nCriteria Check:")
    print(f"  ✓ At least 8 characters: {'YES' if has_length else 'NO'} (Current: {len(password)} characters)")
    print(f"  ✓ Contains uppercase letter: {'YES' if has_upper else 'NO'}")
    print(f"  ✓ Contains lowercase letter: {'YES' if has_lower else 'NO'}")
    print(f"  ✓ Contains number: {'YES' if has_digit else 'NO'}")
    
    # Show overall strength
    print("\n" + "=" * 50)
    print(f"RESULT: {strength}")
    print("=" * 50)
    
    # Provide recommendations for weak passwords
    if strength == "Weak Password":
        print("\nSuggestions to improve:")
        if not has_length:
            print("  - Add more characters (need at least 8)")
        if not has_upper:
            print("  - Add at least one UPPERCASE letter")
        if not has_lower:
            print("  - Add at least one lowercase letter")
        if not has_digit:
            print("  - Add at least one number (0-9)")


# Run the program
if __name__ == "__main__":
    main()
