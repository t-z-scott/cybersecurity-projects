"""checker.py gives user-entered password a strength on a scale of 1-4 (weak=1, moderate=2, strong=3, very strong=4)."""

import re


"""check the user-entered password's validility
Args:
    pwd (string): user-entered password to be checked

Returns:
    sum (integer): password strength score. Defaults to 4.
"""
def check_pwd(pwd):
    # if pwd shorter than 12 letters, return 0
    if len(pwd) < 12:
        return 0
    
    else:
        sum = 4     # password strength tracker variable
        
        # check for at least one uppercase letter
        if not re.search(r'[A-Z]', pwd):
            change_feedback(1)
            sum -= 1
            
        # check for at least one lowercase letter
        if not re.search(r'[a-z]', pwd):
            change_feedback(2)
            sum -= 1
            
        # check for at least one digit
        if not re.search(r'\d', pwd):
            change_feedback(3)
            sum -= 1
            
        # check for at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
            change_feedback(4)
            sum -= 1
            
        return sum
    
    
"""gives the user feedback based on the errors found in the entered password
Args:
    errcode (integer): error code as determined in check_pwd

Returns:
    feedback (string): feedback based on password entered. Defaults to 'Great job!'.
"""
def change_feedback(errcode):
    if errcode == 1:
        feedback += 'Please add an uppercase letter.\n'
    if errcode == 2:
        feedback += 'Please add a lowercase letter.\n'
    if errcode == 3:
        feedback += 'Please add a number.\n'
    if errcode == 4:
        feedback += 'Please add a special character.\n'
    
    if feedback == '':
        return 'Great job!'
    return feedback
    
    
# main program
password = input('Enter your password: ')
score = check_pwd(password)
print(f'Your score is {score}.')
print(change_feedback)
