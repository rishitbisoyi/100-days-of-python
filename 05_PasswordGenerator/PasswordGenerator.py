import random
import string
print("Welcome to the PyPassword Generator!")
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
chars = list(string.punctuation)
alpha = int(input("Enter number of alphabets you want in your password: "))
upper = int(input(f"The number of uppercase letters in {alpha} letters: "))
ndigit = int(input("Enter the number of digits you want in your password: "))
nchar = int(input("Enter the number of special characters you want in your password: "))
password_list = []
if upper == 0:
    password_list.extend(random.choices(lowercase_letters, k=alpha))
else:
    password_list.extend(random.choices(uppercase_letters, k=upper))
    password_list.extend(random.choices(lowercase_letters, k=alpha - upper))
password_list.extend(random.choices(digits, k=ndigit))
password_list.extend(random.choices(chars, k=nchar))
random.shuffle(password_list)
password ="".join(password_list)  
# password=""
# for i in password_list:    can use whichever we want
#     password+=i                       
print(f"Your generated password is: {password}")