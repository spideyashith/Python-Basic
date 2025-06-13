# n = int(input("Enter the number :"))

# sum = 0
# temp = n

# while temp > 0:
#     d = temp  % 10
#     sum = sum + d ** 3
#     temp //= 10 


# if sum == n:
#     print("Armstrong",sum)
# else:
#     print("Not Armstrong")





class PasswordValidationError(Exception):
    """Custom exception for password validation errors."""
    pass

def validate_password(password):
    # Check length
    if not (6 <= len(password) <= 12):
        raise PasswordValidationError("Password must be between 6 and 12 characters long.")
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_characters = "$#@"

    # Check each character in the password
    for char in password:
        if 'a' <= char <= 'z':
            has_lower = True
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Raise exceptions if any criteria are not met
    if not has_lower:
        raise PasswordValidationError("Password must contain at least one lowercase letter (a-z).")
    if not has_upper:
        raise PasswordValidationError("Password must contain at least one uppercase letter (A-Z).")
    if not has_digit:
        raise PasswordValidationError("Password must contain at least one digit (0-9).")
    if not has_special:
        raise PasswordValidationError("Password must contain at least one special character ($, #, or @).")
    
    return True

def main():
    password = input("Enter your password: ")
    
    try:
        if validate_password(password):
            print("Password is valid.")
    except PasswordValidationError as e:
        print(f"Invalid password: {e}")

if __name__ == "__main__":
    main()
    
    