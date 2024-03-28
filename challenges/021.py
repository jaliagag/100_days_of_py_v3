#Solution validation
#
#The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.
#
#Write a function named validate that takes code represented as a string as its only parameter.
#
#Your function should check a few things:
#
#    the code must contain the def keyword
#        otherwise return "missing def"
#    the code must contain the : symbol
#        otherwise return "missing :"
#    the code must contain ( and ) for the parameter list
#        otherwise return "missing paren"
#    the code must not contain ()
#        otherwise return "missing param"
#    the code must contain four spaces for indentation
#        otherwise return "missing indent"
#    the code must contain validate
#        otherwise return "wrong name"
#    the code must contain a return statement
#        otherwise return "missing return"
#
#If all these conditions are satisfied, your code should return True.
#
#Here comes the twist: your solution must return True when validating itself.

def validate(par: str):
    spar = str(par)
    if "def" not in spar:
        return "missing def"
    elif ":" not in spar:
        return "missing :"
    elif "(" not in spar and ")" not in spar:
        return "missing paren"
    elif r"\\(\\)" in spar:
        return "missing param"
    elif "    " not in spar:
        return "missing indent"
    elif "validate" not in spar:
        return "wrong name"
    elif "return" not in spar:
        return "missing return"
    else:
        return True

    #elif ":" not in par



print(validate('def foo():\n print(123)'))
print(validate('\ndef validate(par):\n spar = str(par)\n if "def" not in spar:\n return    "missing def"\n elif ":" not in spar:\n return "missing :"\n elif "(" not in spar and ")" not in spar:\n return "missing paren"\n elif "()" in spar:\n return "missing param"\n elif " " not in spar:\n return "missing indent"\n elif "validate" not in spar:\n return "wrong name"\n elif "return" not in spar:\n return "missing return"\n else:\n return True\n'))

