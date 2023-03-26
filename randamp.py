import random
import string

# define the characters to be used in the password
characters = string.ascii_letters + string.digits + string.punctuation

# set the desired password length
password_length = 10

# generate a password
password = ''.join(random.choice(characters) for i in range(password_length))

# print the password
print("Your new password is:", password)
