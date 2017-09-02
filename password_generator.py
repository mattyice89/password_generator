'''
Prompt: Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a
main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords,
pick a word or two from a list.
'''

import random
import smtplib

# This is the first set to pull from for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# This is the second set to pull from for the password
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# This is the second set the pull from for the password
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+']

# This is where we'll store the password
password = []

# this function adds the number of letters specified above into our password
def generate_letters(num_letters):
    password_letters = []
    while len(password_letters) < (int(num_letters)):
        a = letters[random.randint(0,len(letters)-1)]
        password_letters.append(a)
        password.append(a)

# this function adds the number of numers specified above into our password
def generate_numbers(num_numbers):
    password_numbers = []
    while len(password_numbers) < (int(num_numbers)):
        a = numbers[random.randint(0,len(numbers)-1)]
        password_numbers.append(a)
        password.append(a)

# this function adds the number of symbols specified above into our password
def generate_symbols(num_symbols):
    password_symbols = []
    while len(password_symbols) < (int(num_symbols)):
        a = symbols[random.randint(0,len(symbols)-1)]
        password_symbols.append(a)
        password.append(a)

# this function shuffles our password in a random order
def password_shuffle(password):
    random.shuffle(password)

# this function saves our passwords to a file that logs all our previously used
# passwords
def save_password(parameter):
    pwd_file = open('used_pwds.txt', 'a')
    pwd_file.write("\n")
    pwd_file.write(parameter)
    pwd_file.close()

# If the user inputs they would like a strong password,
def main_strong():
    print('Enter the numbers of letters you\'d like in your password:')
    letters_count = int(input("> "))
    print('Enter the number of numbers you\'d like in your password:')
    numbers_count = int(input("> "))
    print('Enter the number of symbols you\'d like in your password:')
    symbols_count = int(input("> "))
    generate_letters(letters_count)
    generate_numbers(numbers_count)
    generate_symbols(symbols_count)
    password_shuffle(password)
    password_str = ''.join(password)
    save_password(password_str)
    print('Your Password is:')
    print(*password, sep='')
    email_password(password_str)

# This function is called if the user inputs "weak" for password type.
# This function grabs a random line from words.txt,
def main_weak():
    #grab a random line from words.txt
    with open('words.txt') as f:
        for i, a in enumerate(f, 1):
            if i == (random.randint(0,851)):
                break
    # this strips out the '\n' from the end of the line that's pulled in above
    b = a.rstrip('\n')
    # adds this value to the password
    password.append(b)
    # grabs 1 number and appends it to password
    generate_numbers(1)
    # grabs 1 symbol and appends it to password
    generate_symbols(1)
    print(password)
    # this converts the password list to a string
    password_str = ''.join(password)
    save_password(password_str)
    print('Your Password is:')
    print(*password, sep='')
    email_password(password_str)

def email_password(parameter):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    print("Please enter sender's e-mail address")
    sender_email = input("> ")
    print("Please enter password")
    email_password = input("> ")
    print("Please enter recipient's e-mail address")
    recipient_email = input("> ")
    smtpObj.login(sender_email, email_password)
    smtpObj.sendmail(sender_email,recipient_email, ('Subject: Your new Password\n\nDear User, your new password is: ' + str(parameter)))
    {}
    smtpObj.quit()

def prompt():
    print('The purpose of this program is to generate a password')
    print('Would you like a strong or weak password? (weak/strong)')
    pwd_strength = input("> ")
    if pwd_strength.lower() == 'weak':
        main_weak()
    elif pwd_strength.lower() == 'strong':
        main_strong()
    else:
        print("Sorry, I don't understand that...")

prompt()
