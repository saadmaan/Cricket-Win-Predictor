from  sklearn.neural_network import MLPClassifier
import csv
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

clf = MLPClassifier(solver='sgd', hidden_layer_sizes=(2, ), random_state=1, activation='tanh', momentum=0.5)
 
training_data = []
target = []
count = 0
testing_data = []
actual = []

trainingFolder = 'C:\Project 300\BallByBallDataSet\\'
testingFolder = 'C:\Project 300\BallByBallDataSet\\'

print("Training the data")
for i in range(1, 600):
    filename = trainingFolder+str(i)+".csv"
    file = open(filename, "r")
    reader = csv.reader(file)
    #print(filename)
    count = 0

    for line in reader:
        if count == 0:
            count = 1
            continue
        X = []
        b = float(line[1])
        X.append(b)
        c = float(line[2])
        X.append(c)
        d = str(line[3])
        X.append(d)
        f = str(line[5])
        X.append(f)
        g = str(line[6])
        X.append(g)
        h = float(line[7])
        X.append(h)
        i = str(line[8])
        X.append(i)
        j = str(line[9])
        X.append(j)
        k = float(line[10])
        X.append(k)
        l = str(line[11])
        X.append(l)
        m = str(line[12])
        X.append(m)
        n = float(line[13])
        X.append(n)
        o = str(line[14])
        X.append(o)
        p = str(line[15])
        X.append(p)
        q = float(line[16])
        X.append(q)
       

        n = str(line[17])
      #  if (n != 0 and n!= 1):
     #       continue
        target.append(n)
        #print(X)
        training_data.append(X)
#print(target)
print("Total data:")
print(len(target))

clf.fit(training_data, target)
print("Testing the data")
for i in range(601, 743):
    filename = testingFolder+str(i)+".csv"
    file = open(filename, "r")
    reader = csv.reader(file)
    #print(filename)
    count = 0

    for line in reader:
        if count == 0:
            count = 1
            continue
        X = []
        b = float(line[1])
        X.append(b)
        c = float(line[2])
        X.append(c)
        d = str(line[3])
        X.append(d)
        f = str(line[5])
        X.append(f)
        g = str(line[6])
        X.append(g)
        h = float(line[7])
        X.append(h)
        i = str(line[8])
        X.append(i)
        j = str(line[9])
        X.append(j)
        k = float(line[10])
        X.append(k)
        l = str(line[11])
        X.append(l)
        m = str(line[12])
        X.append(m)
        n = float(line[13])
        X.append(n)
        o = str(line[14])
        X.append(o)
        p = str(line[15])
        X.append(p)
        q = float(line[16])
        X.append(q)
       

        n = str(line[17])
        #if (n != 0 and n!= 1):
            #continue
        actual.append(n)
        #print(X)
        testing_data.append(X)

#print(actual)
total = len(actual)
print(total)

output = clf.predict(testing_data)
correct = 0

print(output)
accuracy = accuracy_score(actual, output) 
for i in range(0, total):
    if (actual[i] == output[i]):
        correct += 1

error = total - correct
print(error)



#print("Complete for Feature :" + str(feature_number));
#print("Train Score : " + str(clf.score(training_data, target)));
#print("Precision : " + str(precision_score(actual, output, average='weighted') * 100.0))
#print("F1 Score : " + str(f1_score(actual, output, average='weighted') * 100.0))
#print("Error Rate : " + str(error / total * 100.0));
#print("---------------------------------------\n");

print("Total test set size : " + str(total));
print("Correct prediction : " + str(correct));
print("Incorrect Prediction : " + str(error));
print("Accuracy : " + str(accuracy * 100.0))

print('DONE')
