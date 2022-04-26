
import re

#indian phoneNo validation
phoneNoValidation = r'\+?(0|91)?[6-9][0-9]{9}'

def check(phoneNo):

	if(re.fullmatch(phoneNoValidation, phoneNo)):
		print("Valid phoneNo:", phoneNo)

	else:
		print("Invalid phoneNo :", phoneNo)


# Driver Code
if __name__ == '__main__':

	phoneNo = "0739253408"
	check(phoneNo)

	phoneNo = "+917667695714"
	check(phoneNo)

	phoneNo = "917667695714"
	check(phoneNo)
 
	phoneNo = "07667695714"
	check(phoneNo)
