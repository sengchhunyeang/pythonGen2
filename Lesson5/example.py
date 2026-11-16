def calculate_grade(score):
    """
    Determines the letter grade based on a numeric score.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# --- Example Usage ---
# Prompt the user for an input score
try:
    user_score = float(input("Enter the student's score (0-100): "))
    
    # Check if the score falls within a realistic range
    if 0 <= user_score <= 100:
        final_grade = calculate_grade(user_score)
        print(f"A score of {user_score} earns a grade of: {final_grade}")
    else:
        print("Please enter a valid score between 0 and 100.")
        
except ValueError:
    print("Invalid input. Please enter a numeric value.")