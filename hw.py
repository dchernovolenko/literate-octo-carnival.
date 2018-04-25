
from string import digits

def check_upper(input):
    f = [char for char in input if char.isupper()]
    if len(f) > 0:
        return True
    else:
        return False

def check_lower(input):
    f = [char for char in input if char.islower()]
    if len(f) > 0:
        return True
    else:
        return False

def check_num(input):
    f = [char for char in input if char in digits]
    if len(f) > 0:
        return True
    else:
        return False

def check_misc(input):
    f = [char for char in input if char in """!@$%^&*()_-+={}[]|\,.></?~`"':;"""]
    if len(f) > 0:
        return True
    else:
        return False

def check_len(input, num):
    if len(input) > num:
        return True
    else:
        return False

def issafe(input):
    if check_lower(input) and check_upper(input) and check_num(input):
        return True
    else:
        return False

def calcstrength(input):
    val = 0
    if check_upper(input) and check_lower(input):
        val += 3
    if check_num(input):
        val += 2
    if check_misc(input):
        val += 2
    if check_len(input, 5):
        val += 1
    if check_len(input, 8):
        val += 2
    if check_len(input, 15) and val < 10:
        val += 2
    return val

print issafe("Tr0ub4dor&3")
print issafe("correcthorsebatterystaple")
print calcstrength("Tr0ub4dor&3")
print calcstrength("correcthorsebatterystaple")
