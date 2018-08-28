import csv

arr = []

with open('App.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        arr.append(line)
    print(arr)
        

