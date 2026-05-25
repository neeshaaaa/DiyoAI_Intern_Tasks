def check_password(password):
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    length = len(password) >= 8
    
    score = sum([upper, lower, digit, length])
    
    if score < 2:
        return "Weak Password"
    elif score < 4:
        return "Medium Password"
    else:
        return "Strong Password"

pwd = input("Enter password: ")
print(check_password(pwd))
