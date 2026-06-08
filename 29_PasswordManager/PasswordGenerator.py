import random
import string

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
chars = list(string.punctuation)

password_list = []
def generate_password(alpha, upper, ndigit, nchar):
    password_list.clear()
    if upper == 0:
        password_list.extend(random.choices(lowercase_letters, k=alpha))
    else:
        password_list.extend(random.choices(uppercase_letters, k=upper))
        password_list.extend(random.choices(lowercase_letters, k=alpha - upper))
    password_list.extend(random.choices(digits, k=ndigit))
    password_list.extend(random.choices(chars, k=nchar))
    random.shuffle(password_list)
    password ="".join(password_list)  
    return password
