# Password & Username Validator

A Python console application that guides a user through registration and login with input validation.

## What it does

- Prompts the user to create a username and password
- Validates the username: must start with a lowercase letter, can only contain letters, numbers, and underscores, and must not already be taken
- Validates the password against multiple requirements: minimum 8 characters, at least one uppercase letter, one lowercase letter, one digit, one special character, and no spaces
- After successful registration, prompts the user to log in and verifies the credentials

## Technologies

- Python 3
- `re` module (regular expressions)

## How to run

```bash
python project1_passwords.py
```

## Notes

This is a course project completed as part of a Python fundamentals course. Input validation is handled using regular expressions.