import re  

def check_password_strength(password):  
    strength = 0  
    feedback = []  

    # Check length
    if len(password) >= 8:  
        strength += 1  
    else:  
        feedback.append("❌ Password should be at least 8 characters long.")  

    # Check for uppercase & lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):  
        strength += 1  
    else:  
        feedback.append("❌ Include both uppercase and lowercase letters.")  

    # Check for numbers
    if re.search(r'\d', password):  
        strength += 1  
    else:  
        feedback.append("❌ Include at least one number.")  

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  
        strength += 1  
    else:  
        feedback.append("❌ Include at least one special character (!@#$%^&*).")  

    # Provide feedback
    if strength == 4:  
        return "✅ Strong password!"  
    else:  
        return "Weak password:\n" + "\n".join(feedback)  

# Test the function
if __name__ == "__main__":  
    user_password = input("Enter your password: ")  
    print(check_password_strength(user_password))  
