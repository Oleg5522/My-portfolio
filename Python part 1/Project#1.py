import re
u, Username = '','' #initialization
p, Password = '','' #initialization
taken_u = ['admin', 'admin123', 'superuser', 'superuser123']

#Greetings and username verification
print('Hello, valuable customer of our online store. In order to receive a monthly discount on our products, you need to register on our website. Please create a username and password.')
while True:
    u = input('Please, create Username. The username must begin with a lowercase letter and can only contain letters, numbers, and underscores:    ', )
    print(u)
    p = input('Please, create Password. The password must be: At least 8 characters long, Contains at least one uppercase letter,Contains at least one lowercase letter,Contains at least one digit,Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -, Does not contain any spaces:     ', )
    print(p)
    if u[0].islower() and u.isidentifier():
        print('Username meets requeriments')
    else:
        print('Username is incorrect, please, follow requeriments')
        continue
#Checking for discrepancies with already taken usernames
    if u not in taken_u:
        print('Username is correct')
    else:
        print('Username is taken, please create different one')
        continue
#Password length check
    if len(p)>=8:
        print(f"Password passed, {p} is greater than 8")
    else:
        print(f"Password failed, {p} is less than 8")
        continue
#Checking for an uppercase in a password
    uppercase_test_regex = bool(re.match(r'\w*[A-Z]\w*', p))
    if uppercase_test_regex:
        print(f'Password passed, {p} contains uppercase letter')
    else:
        print(f'Password failed, {p} does not contain an uppercase letter')
        continue
        
#Checking for a lowercase in a password
    lowletter_test_regex = bool(re.match(r'\w*[a-z]\w*', p))
    if lowletter_test_regex:
        print(f'Password passed, {p} contains lowercase letter')
    else:
        print(f'Password failed, {p} does not contain a lowercase letter')
        continue


 #Checking for a space in a password       
    has_space = re.search(r'\s', p)
    if not has_space:
        print(f'Password passed, {p} does not contain any space')        
    else:
        print(f'Password failed, {p} contains space')
        continue   
    
 # Checking for a digit in a password   
    digit_re = bool(re.match(r'\w*[0-9]\w*', p))
    if digit_re:
       print(f'Password passed {p} contains digit')
    else:
       print(f'Password failed, {p} does not contain a digit')
       continue
#Checking for a special character in a password
    special_character = bool(re.match(r'\w*[!, ?, @, #, $, ^, &, *, _, -]\w*', p))
    if special_character:
       print(f'Password passed, {p} contains special character')
       print('You signed up succesfully!')
    else:
       print(f'Password failed, {p} does not contain any special character')
       continue


  #input username and password to log in  
    Username = input('Please, enter your Username', )
    Password = input('Please, enter your password', )
#Checking that the username and password correspond to those that were created during registration
    if  Username == u and  Password == p:
        print("Login Successful!")
        break
    else:
        print("Incorrect username and/or password, please, try again")
    continue



















    
    


