"""
Title: Password Strength Checker
Author: Clinton Jake Cai
Description: A password strength checker for users (employees) to make their
passwords better secure, with feedbacks provided to them for improvement and learning.
Enhancement: I made it a user_friendly program through 1) taking note of the user's name and 2) counting of their password strength checks using the assignment operator +=
"""
from pathlib import Path
wordlist_file = Path(__file__).parent / "wordlist.txt"
top_password_file = Path(__file__).parent / "toppasswords.txt"

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def main():
    """
    Purpose: Provides the user input loop. The loop asks the user for a 
    password to test. If that password is anything but "q" or "Q" call the 
    password_strength function and report the results to the user. If the user 
    enters "q" or "Q", quit the program.
    Parameters: N/A
    Return: N/A
    """
    # User input while loop, password_strength() function
    
    user_name = input("\nWelcome! This is a password strength checker program. What's your name? ").title()
    check_count = 0
    run = "yes"
    
    while run == "yes":
        password = input(f"{user_name}, please enter the password (Type 'q' to quit): ")
        if password.lower() == "q":
            break
        
        check_count += 1
        
        strength = password_strength(password)
        print(f"The password '{password}' has a strength value of {strength}.")
        
        run = input(f"\n{user_name}, would you like to try again? (YES or NO) ").lower()
        
    print(f"\nYou made a total of {check_count} check count/s!")
    print(f"{user_name}, thanks for having us : )")
        
def password_strength(password, min_length=10, strong_length=16):
    """
    Purpose: This function checks length requirements, checks dictionary and 
    known-passwords, calls word_complexity to calculate the word's complexity then 
    determines the password's strength based on the user requirements. It should 
    print the messages defined in the requirements and return the password's 
    strength as a number from 0 to 5. The strength score will be calculated as a 
    base score of 1 plus the complexity score.The min_length parameter should have
    a default value of 10. The strong_length parameter should have a default value 
    of 16.
    Parameters: password, min_length=10, strong_length=16
    Return: Integer
    """
    # If Statements, len() function, word_complexity() function, print the requirements.  
     
    wordlist_match = word_in_file(password, wordlist_file)
    top_password_match = word_in_file(password, top_password_file)
        
    if wordlist_match:
        print("\nPassword is a dictionary word and is not secure.")
        return 0
    elif top_password_match:
        print("\nPassword is a commonly used password and is not secure.")
        return 0
    elif len(password) < min_length:
        print("\nPassword is too short and is not secure.")
        return 1
    elif len(password) >= strong_length:
        print("\nPassword is long, length trumps complexity. This is a good password.")
        return 5
    else:
        complexity = word_complexity(password)
        
        base = 1
        if complexity == 4:
            complexity += base
            return complexity
        elif complexity == 3:
            complexity += base
            return complexity
        elif complexity == 2:
            complexity += base
            return complexity
        elif complexity == 1:
            complexity += base
            return complexity
        else:
            complexity += 1
            return complexity
        
def word_in_file(word, filename, case_sensitive=False):
    """
    Purpose: Reads a file per line for word which is then compared to the word 
    parameter argument.
    Parameter: 
    1. word: A word from the user.
    2. filename: The dictionary and the top password list files
    3. case_sensitive: If case_sensitive parameter is True, a case sensitive
    matching is performed. Default value is case_sensitive=False. For checking 
    using the dictionary, it is case insensitive, meaning False. While using the 
    password list, it is case sensitive, which is True.
    Return: Boolean
    - Returns a True if word in file is same to the word from the user.
    """
    # open() function, If Statements
    
    with open(filename, "r", encoding="utf-8") as file_info:
        for item in file_info:
            file_data = item.strip()
            if case_sensitive:
                if word == file_data:
                    return True
            else:
                if word.lower() == file_data.lower():
                    return True
        return False

def word_has_character(word, character_list):
    """
    Purpose: Loops through each character in the string passed in the word 
    parameter to see if that character is in the list of characters passed in the
    character_list parameter. If any of the characters in the word are present in
    the character list return a true, If none of the characters in the word are in 
    the character list return false.
    Parameters: word, character_list
    Return: Boolean
    """
    # For Loop & If Statements
    
    for letter in word:
        if letter in character_list:
            return True
    return False
    
def word_complexity(word):
    """
    Purpose: This function creates a numeric complexity value based on the types of
    characters the word parameter contains. One point of complexity is given for
    each type of character in the word. The function calls the word_has_character
    function for each of the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL).
    If the word has that kind of character a point is added to complexity rating. 
    Since there are 4 kinds of characters the complexity rating will range from 0 
    to 4. (0 would be returned only if word contained no characters or only contains
    characters that are not in any of the lists.)
    Parameters: word
    Return: Integer
    """
    # If Statements and Assignment operators, calls word_has_character() function
    complexity = 0
    
    lower_character_check = word_has_character(word, LOWER)
    if lower_character_check:
        complexity += 1
        
    upper_character_check = word_has_character(word, UPPER)
    if upper_character_check:
        complexity += 1
    
    digits_character_check = word_has_character(word, DIGITS)
    if digits_character_check:
        complexity +=1
    
    special_character_check = word_has_character(word, SPECIAL)
    if special_character_check:
        complexity +=1

    return complexity
    
if __name__ == "__main__":
    main()