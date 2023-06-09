"""
    The function calculates a person's age in minutes based on their date of birth and returns the age
    in words.
    """
import sys
    
from datetime import date


def main():
    # Prompt the user for their date of birth
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

    # Parse the date of birth
    try:
        dob = date.fromisoformat(dob_str)
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
        sys.exit(1)

    # Calculate the user's age in minutes
    age_in_minutes = (date.today() - dob).total_seconds() // 60

    # Print the user's age in words
    print(age_in_words(age_in_minutes))


def age_in_words(minutes):
    # Define the words for the different units of time
    words = [
        ("year", 60 * 24 * 365),
        ("month", 60 * 24 * 30),
        ("day", 60 * 24),
        ("hour", 60),
        ("minute", 1),
    ]

    
    units = [int(minutes // w[1]) for w in words]


    age_words = [f"{units[i]} {words[i][0]}" for i in range(len(units)) if units[i] != 0]


    if len(age_words) == 0:
        return "0 minutes"
    elif len(age_words) == 1:
        return age_words[0]
    else:
        return ", ".join(age_words[:-1]) + " and " + age_words[-1]


    if _name_ == "_main_":
        main()