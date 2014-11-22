# number of names that are subsets of other names?

import ssadata

largedataset = ssadata.boys.keys() + ssadata.girls.keys();
counter = 0;
subsets_list = []

for metaname in largedataset:
    for name in largedataset:
        if metaname in name:
            subsets_list.append(metaname);

print "The number of names that are subsets of other name is: " , len(subsets_list)


