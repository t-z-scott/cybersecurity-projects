# simple password strength checker

## problem
Simple passwords can be easily cracked with free, open-source software and tools, increasing the risk for most users. To get back in the swing of projects, I have implemented a password strength checker tool in Python.

## requirements
The password entered must have:
- *12 or more characters,*
- 1 uppercase letter,
- 1 lowercase letter,
- 1 number, and
- 1 special character.
The top requirement is required. If this condition is not met, the user gets a score of zero.

### advantages of requirements
The 12-letter requirement raises the crack time of a password matching the rest of the requirements from 3 hours to 17 hours at 10k guesses/sec, according to [zxcvbn](https://lowe.github.io/tryzxcvbn/). This was tested with common words. The more time it would take for an attacker to decode a user's password, the better. This is a common deterrent from password brute-force attacks.

## tips
- Use a password manager to generate and store secure passwords.
- If a password must be made manually, choose phrases, song lyrics, or quotes for easy memorization. Keep track of useful hints in a secure note-taking application.
- Never write passwords on paper.
- Do not use Show Password in a public place, such as on a plane or in a restaurant. A bad actor could look over a user's shoulder and learn their password. This is called **shoulder surfing**.
