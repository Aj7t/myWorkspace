
import re

#regular expression for validating an Email
emailValidation = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):

	# fullmatch() method
	if(re.fullmatch(emailValidation, email)):
		print("Valid Email")

	else:
		print("Invalid Email")


# Driver Code
if __name__ == '__main__':

	email = "krajito%$@gmail.com"
	check(email)

	email = "ajit@yahoo.com"
	check(email)

	email = "ajit$@.co"
	check(email)
