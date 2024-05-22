import re

def password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[\W_]', password))  # \W matches any non-word character (special characters)
    
    # Strength assessment
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    # Feedback based on criteria met
    feedback = "Password strength: "
    if criteria_met == 5:
        feedback += "Very Strong"
    elif criteria_met == 4:
        feedback += "Strong"
    elif criteria_met == 3:
        feedback += "Moderate"
    elif criteria_met == 2:
        feedback += "Weak"
    else:
        feedback += "Very Weak"
    
    # Detailed feedback
    detailed_feedback = "\nDetailed Feedback:\n"
    if not length_criteria:
        detailed_feedback += "- Password should be at least 8 characters long.\n"
    if not uppercase_criteria:
        detailed_feedback += "- Password should contain at least one uppercase letter.\n"
    if not lowercase_criteria:
        detailed_feedback += "- Password should contain at least one lowercase letter.\n"
    if not number_criteria:
        detailed_feedback += "- Password should contain at least one number.\n"
    if not special_criteria:
        detailed_feedback += "- Password should contain at least one special character.\n"

    return feedback + detailed_feedback

def main():
    password = input("Enter a password to check its strength: ")
    print(password_strength(password))

if __name__ == "__main__":
    main()
