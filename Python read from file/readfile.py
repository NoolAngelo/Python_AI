import csv

with open('cereal.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)