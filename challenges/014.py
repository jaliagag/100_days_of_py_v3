#Palindrome
#
#A string is a palindrome when it is the same when read backwards.
#
#For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".
#
#Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.

def palindrome(par: str):
    word = []
    for i in par:
        word.append(i)

    drow = word[::-1]

    if word == drow:
        return True

    return False



print(palindrome("bob"))
