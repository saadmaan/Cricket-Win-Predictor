import csv
trainingFolder = 'C:\Project 300\Python codes\Ongoing Match Data\TrainingData\\'
testingFolder = 'C:\Project 300\Python codes\Ongoing Match Data\TestingData\\'


for i in range(3, 4):
    filename = trainingFolder+str(i)+".csv"
    file = open(filename, "r")
    reader = csv.reader(file)
    row0 = reader.next()
    row0.append('Day/Day-Night')
    for item in reader:
      item.append(1)
