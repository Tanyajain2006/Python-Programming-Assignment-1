import csv

# writing a csv file
with open("names.csv", 'w') as csv_file:
    names = [
        {"name" : "Riya", "class" : 13},
        {"name" : "Harshita", "class" : 14},
        {"name" : "Aarushi", "class" : 12}
    ]
    field_name = ["name", "class"]
    writer = csv.DictWriter(csv_file, fieldnames = field_name)
    
    writer.writeheader()
    for i in names:
        writer.writerow(i)

# reading a csv file
with open("names.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)

    for i in reader:
        print(i) # printing the data of csv file on console