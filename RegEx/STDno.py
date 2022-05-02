import re


# STD number should have 3 to 5 digit starting with either 0 or 4
stdValidation = r'^0?[1-9][0-9]{1,3}$'

def check (stdNo):
    if re.fullmatch(stdValidation,stdNo):
        print("Valid STD No:", stdNo)
    else:
        print("Invalid STD No:", stdNo)
        
        
        
if __name__ == '__main__':
    
    stdNo = "7141"
    check(stdNo)
    
    stdNo = "06111"
    check(stdNo)
    
    stdNo = "Iy6"
    check(stdNo)

    stdNo = "04"
    check(stdNo)

    stdNo = "1"
    check(stdNo)
    
    stdNo = "1125"
    check(stdNo)
    
    stdNo = "000"
    check(stdNo)








