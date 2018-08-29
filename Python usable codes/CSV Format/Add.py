import csv

trainingFolder = trainingFolder = 'C:\Project 300\Python codes\Ongoing Match Data\TrainingData\\'
filename = trainingFolder+str(1)+".csv"
filename1 = trainingFolder+str(3)+".csv"
filename2 = "C:\Project 300\Python codes\Ongoing Match Data\Marge Data\out1.csv"

with open(filename) as in1,  open(filename1) as out, open(filename2, 'wb') as marge:
    reader1 = csv.reader(in1)
    reader2 = csv.reader(out)
    writer = csv.writer(marge)
    for row in reader1:
        row1 = reader2.next()
        row.extend(str(row1[15]))
        writer.writerow(row)
