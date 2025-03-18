"""checker.py gives user-entered password a strength on a scale of 1-4 (weak=1, moderate=2, strong=3, very strong=4)."""

import re


"""check the user-entered password's validility
Args:
    pwd (string): user-entered password to be checked

Returns:
    strength (integer): password strength score. Defaults to 4.
    feedback (string): feedback based on password entered. Defaults to 'Great job!'.
"""
def check_pwd(pwd):
    # if pwd shorter than 12 letters, return 0
    if len(pwd) < 12:
        return 0
    
    else:
        strength = 4         # password strength tracker int
        feedback = ''   # feedback string
        
        # check for at least one uppercase letter
        if not re.search(r'[A-Z]', pwd):
            feedback += 'Please add an uppercase letter.\n'
            strength -= 1
            
        # check for at least one lowercase letter
        if not re.search(r'[a-z]', pwd):
            feedback += 'Please add a lowercase letter.\n'
            strength -= 1
            
        # check for at least one digit
        if not re.search(r'\d', pwd):
            feedback += 'Please add a number.\n'
            strength -= 1
            
        # check for at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
            feedback += 'Please add a special character.\n'
            strength -= 1
            
        if feedback == '':
            feedback == 'Great job!'
        
        return strength, feedback
    
    
# main program
password = input('Enter your password: ')
score, str = check_pwd(password)
print(f'Your score is {score}.\n{str}')
