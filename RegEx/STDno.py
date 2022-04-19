import re

stdValidation = r'^[0-9]{2,3}$'

def check (stdNo):
    if re.fullmatch(stdValidation,stdNo):
        print("Valid STD No:", stdNo)
    else:
        print("Invalid STD No:", stdNo)
        
        
        
if __name__ == '__main__':
    
    stdNo = "123"
    check(stdNo)
    
    stdNo = "10"
    check(stdNo)
    
    stdNo = "Iy6"
    check(stdNo)

    stdNo = "123458"
    check(stdNo)

    stdNo = "1"
    check(stdNo)
