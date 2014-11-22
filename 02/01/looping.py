names = ["lucas", "lauren", "elena", "rafal", "ahmer", "andrew", "kristin", "john", "cindy"]

counter = 0

# set name equal to each item in the list names
for name in names:
    if name[0].lower() in "lu":
        counter = counter +1
        
print(counter)

   