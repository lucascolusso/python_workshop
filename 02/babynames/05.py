#What are the boys names that are never girls names? How many?

import ssadata

list_names = [];
counter = 0;

for name in ssadata.boys.keys():
    if name not in ssadata.girls.keys():
        list_names.append(name);
        counter = counter + 1;
        
#print "The list of boys names which are never girls names is: " , list_names
print "The number of different boys names is: " ,len(ssadata.boys)
print "The number of different girls names is: " ,len(ssadata.girls)
print "The number of boys names that are never girls names is: " , counter
