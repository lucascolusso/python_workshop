#how many boys and girls total?

import ssadata

counter = 0
largedataset = ssadata.boys.keys() + ssadata.girls.keys()

for name in largedataset:
    counter = counter + 1
        
print "The total number of boys and girls in the list is " + str(counter) + " ."