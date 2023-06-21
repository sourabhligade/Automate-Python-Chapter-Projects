import re
def UpperCaseCheck(password):
    if re.compile(r'[A-Z]',password):
        return True
    return False

def LowerCaseCheck(password):
    if re.compile(r'[a-z]',password):
        return True
    return False

def NumCheck(password):
    if re.compile(r'[1-9]',password):
        return True
    return False



def PassWordChecker(password):
    print ('ENter  a password which should be 8 characters long ,should have a capital and small letter and digits')
    password=input('Enter a password:')
    if len(password)>=8 and UpperCaseCheck(password) and LowerCaseCheck(password):
        print('strong password')
    else:
        print('weak password')


