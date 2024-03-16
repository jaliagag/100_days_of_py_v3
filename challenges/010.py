#Flatten a list
#
#Write a function that takes a list of lists and flattens it into a one-dimensional list.
#
#Name your function flatten. It should take a single parameter and return a list.
#
#For example, calling:
#
#flatten([[1, 2], [3, 4]])
#
#Should return the list:
#
#[1, 2, 3, 4]
#

def flatten(par: list):
    final = []
    for ele in par:
        if type(ele) == list:
            for i in ele:
                if i in final:
                    pass
                else:
                    final.append(i)
        else:
            final.append(ele)

    return final

print(flatten([[1,2],[3,4]]))
