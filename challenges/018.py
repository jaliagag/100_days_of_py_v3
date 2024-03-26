#Boolean and
#
#Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

def triple_and(par1: bool, par2: bool, par3: bool):
    if par1 == True and par2 == True and par3 == True:
        return True
    else:
        return False
