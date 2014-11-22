#what is the longest name?

import ssadata

str_len = 0
longest_name = "initial"
largedataset = ssadata.boys.keys() + ssadata.girls.keys()


for name in largedataset:
    if len(name) >= str_len:
        str_len = len(name)
        longest_name = name
        
print "The longest name is " + longest_name + " and it has " + str(str_len) + " letters."