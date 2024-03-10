#Double letters
#
#The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
#
#
#Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(par: str):
    myl = list(par)
    for index,i in enumerate(myl):
        if index+1 < len(myl):
            if myl[index] == myl[index+1]:
                return True
                print("hay dos letras iguales")
    return False


print(double_letters("hello"))
print(double_letters("nono"))
print(double_letters("hha"))
