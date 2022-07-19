import instaloader
from getpass import getpass

L = instaloader.Instaloader()

#// Ask for instagram username
USER = ""
USER = input('Enter Instagram Username: ')

#// Ask for instagram password
PASSWORD = ""
PASSWORD = getpass('Enter Password: ')

# #// logging in to instagram profile
L.login(USER , PASSWORD)
print('Successfully Logged in to profile:' , USER ,'!')