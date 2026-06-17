import random
import string

length = int(input("Enter password length: "))

password = ""

if length > 0:
    characters = string.ascii_letters + string.digits

    for i in range(length):
        password = password + random.choice(characters)

    print("Your Password is:", password)
else:
   print("Invalid Length")
