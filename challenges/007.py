#Adding and removing dots
#
#Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
#
#Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
#
#If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
#
#(You may assume that the input to add_dots does not itself contain any dots.)

def add_dots(par: str):
    myl = list(par)
    dotted = []
    for index,i in enumerate(myl):
        dotted.append(i)
        if index != len(myl)-1:
            dotted.append(".")
    return "".join(dotted)

def remove_dots(par: str):
    myl = list(par)
    final = []
    for i in myl:
        if i != ".":
            final.append(i)
    return "".join(final)

print(remove_dots(add_dots("test")))
