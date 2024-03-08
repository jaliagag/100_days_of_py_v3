#Middle letter
#
#Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
#
#For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(par: str):
    length = len(list(par))
    if length % 2 == 0:
        return ""
    else:
        middle = round(length / 2)

        return par[ middle - 1 ]



print(mid("abc"))

print(mid("abcdefg"))

print(mid("aaaa"))
