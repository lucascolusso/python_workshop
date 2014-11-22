#boys names that are also girls names?

import ssadata

list_names = [];

for name in ssadata.boys.keys():
    if name in ssadata.girls.keys():
        list_names.append(name)
        
#print "The list of boys names which are also girls names is: " , list_names
print "The number of different boys names is: " ,len(ssadata.boys)
print "The number of different girls names is: " ,len(ssadata.girls)
print "The number of unisex names: " ,len(list_names)
