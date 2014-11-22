import csv

csv_file = open("hp_wiki.csv", "rb")

rows = csv_file.readlines()

day_edits = {}

for row_dict in csv.DictReader(rows):

    day = row_dict["timestamp"]
    day = day[0:10]

    if day_edits.has_key(day):
        day_edits[day] = day_edits[day] + 1
    else:
        day_edits[day] = 1
        
output_file = open("hp_edits.html", "wb")
output_file.write("date\teditcount</br>")
  
for day in day_edits.keys():
    edit_count = day_edits[day]
    data_list = [day, str(edit_count)]
    
    output_file.write("\t".join(data_list) + "</br>")

output_file.close()