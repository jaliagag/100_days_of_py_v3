#All equal
#
#Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
#
#For example, calling all_equal([1, 1, 1]) should return True.

def all_equal(par: list):
    if len(par) < 1:
        return True
    else:
        first = par[0]
        final = 0
        for i in par:
            if i != first:
                final = 1
    
        if final == 0:
            return True
        else:
            return False

print(all_equal([1,1,1]))
print(all_equal([1,2,1]))
print(all_equal([]))

###
# naive solution
#def all_equal(items):
#    for item1 in items:
#        for item2 in items:
#            if item1 != item2:
#                return False
#    return True
#
#
## one-liner with nested list comprehension
## and the all() built-in
#def all_equal(items):
#    return all(item1 == item2 for item1 in items for item2 in items)

