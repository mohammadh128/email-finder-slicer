# importing the libraries
import re


# using regex to get the emails from any given document
my_str = "Hi my name is momo and email address is momo.h@somecompany.co.au and my friend's email is erfi@gmail.com and my other frinds email is mamsoudi@yahoo.com"
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)


# slicing the email into the USER name and domain name
user_name = []
domains_name = []

for email in emails:
    user_name.append(email[:email.index("@")])
    domains_name.append(email[email.index("@")+1:])


# showing the result
print(f"Your usernames are {user_name} and your domain name is {domains_name}")
