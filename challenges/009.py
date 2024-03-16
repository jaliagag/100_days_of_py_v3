
#Anagrams
#
#Two strings are anagrams if you can make one from the other by rearranging the letters.
#
#Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.
#
#For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.


def is_anagram(par1: str, par2: str):
    if len(par1) == len(par2):
        my_dict_1 = {}
        my_dict_2 = {}
        for i in par1:
            if i in my_dict_1.keys():
                my_dict_1[i] += 1
            else:
                my_dict_1[i] = 1

        for i in par2:
            if i in my_dict_2.keys():
                my_dict_2[i] += 1
            else:
                my_dict_2[i] = 1

        if my_dict_1 == my_dict_2:
            return True
        else:
            return False
    else:
        return False

print(is_anagram("typhoon","opython"))
print(is_anagram("Alice","Bob"))
print(is_anagram('test', 'tess'))

# ...
# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)
