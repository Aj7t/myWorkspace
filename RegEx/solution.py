

import re

panNoValidation = r'[A-Z]{5}[0-9]{4}[A-Z]{1}'

def check(panNo):
    if re.fullmatch(panNoValidation, panNo):
        print("Valid pan No:", panNo)
    else:
        print("Invalid pan No:", panNo)


if __name__ == '__main__':

    panNo = "123"
    check(panNo)

    panNo = "10"
    check(panNo)

    panNo = "Iy6"
    check(panNo)

    panNo = "123458"
    check(panNo)

    panNo = "1"
    check(panNo)
