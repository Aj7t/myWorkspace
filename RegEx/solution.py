

import re

panNoValidation = r'[A-Z]{5}[0-9]{4}[A-Z]{1}'

def check(panNo):
    if re.fullmatch(panNoValidation, panNo):
        print("Valid pan No:", panNo)
    else:
        print("Invalid pan No:", panNo)


if __name__ == '__main__':

    panNo = "BNZAA23184"
    check(panNo)

    panNo = "BNZAA2318"
    check(panNo)

    panNo = "Iy6"
    check(panNo)

    panNo = "BN7AA23184"
    check(panNo)

    panNo = "BNZAA2318A"
    check(panNo)
