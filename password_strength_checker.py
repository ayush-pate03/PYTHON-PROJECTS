import re


def check_password_strength(password):

    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("====================================")
print("       PASSWORD STRENGTH CHECKER")
print("====================================")

password = input("Enter your password: ")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:

    print("\nSuggestions:")

    for suggestion in suggestions:
        print("-", suggestion)

else:

    print("Excellent! Your password meets all requirements.")