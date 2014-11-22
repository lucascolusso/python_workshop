import csv

csv_file = open("hp_wiki.csv", "rb")

rows = csv_file.readlines()

top_users = {}

for row_dict in csv.DictReader(rows):

    user = row_dict["user"]

    if top_users.has_key(user):
        top_users[user] = top_users[user] + 1
    else:
        top_users[user] = 1
        
output_file = open("top_users.tsv", "wb")
output_file.write("user\teditcount\n")
  
for user in top_users.keys():
    edit_count = top_users[user]
    data_list = [user, str(edit_count)]
    
    output_file.write("\t".join(data_list) + "\n")

output_file.close()