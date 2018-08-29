import csv
trainingFolder = 'C:\Project 300\Python codes\Ongoing Match Data\TrainingData\\'
filename = trainingFolder+str(3)+".csv"
cr = csv.reader(open(filename,"r"))
cr.next()
b= sum(float(x[26]) for x in cr)
c= sum(float(x[25]) for x in cr)
print c
try:
    print b/c
except ZeroDivisionError:
    print "You can't divide by zero, you're silly."

