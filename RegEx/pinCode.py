import re 

pinCodeValid = r'^[0-9]{6}$'


def check(pinCode):
    if re.fullmatch(pinCodeValid, pinCode):
        print("Valid PinCode:", pinCode)
    else:
        print("Invalid PinCode:", pinCode)
        
        
if __name__ == '__main__':
    
    pincode ="847201"
    check(pincode)
    
    pincode = "125"
    check(pincode)
    
    pincode = "8Ty201"
    check(pincode)
