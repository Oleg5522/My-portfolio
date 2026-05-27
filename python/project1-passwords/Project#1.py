import re

u, Username = '', ''  # initialization
p, Password = '', ''  # initialization
taken_u = ['admin', 'admin123', 'superuser', 'superuser123']

# Greetings and username verification
print('Hello, valuable customer of our online store. In order to receive a monthly discount on our products, you need to register on our website. Please create a username and password.')

while True:
    u = input('Please, create Username. The username must begin with a lowercase letter and can only contain letters, numbers, and underscores:    ')
    print(u)
    p = input('Please, create Password. The password must be: At least 8 characters long, Contains at least one uppercase letter, Contains at least one lowercase letter, Contains at least one digit, Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -, Does not contain any spaces:     ')
    print(p)

    if u[0].islower() and u.isidentifier():
        print('Username meets requirements')
    else:
        print('Invalid username')
        continue

    # Checking for discrepancies with already taken usernames
    if u not in taken_u:
        print('Username is correct')
    else:
        print('Username taken')
        continue

    # Password length check
    if len(p) >= 8:
        print(f"Password passed, {p} is at least 8 characters")
    else:
        print('Invalid password')
        continue

    # Checking for an uppercase in a password
    if re.search(r'[A-Z]', p):
        print(f'Password passed, {p} contains uppercase letter')
    else:
        print('Invalid password')
        continue

    # Checking for a lowercase in a password
    if re.search(r'[a-z]', p):
        print(f'Password passed, {p} contains lowercase letter')
    else:
        print('Invalid password')
        continue

    # Checking for a space in a password
    if not re.search(r'\s', p):
        print(f'Password passed, {p} does not contain any space')
    else:
        print('Invalid password')
        continue

    # Checking for a digit in a password
    if re.search(r'[0-9]', p):
        print(f'Password passed, {p} contains digit')
    else:
        print('Invalid password')
        continue

    # Checking for a special character in a password
    if re.search(r'[!?@#$^&*_-]', p):
        print(f'Password passed, {p} contains special character')
        print('Sign up successful!')
    else:
        print('Invalid password')
        continue

    # Input username and password to log in
    while True:
        Username = input('Please, enter your Username: ')
        Password = input('Please, enter your Password: ')

        if Username == u and Password == p:
            print("Login successful!")
            break
        else:
            print("Incorrect username or password")

    break