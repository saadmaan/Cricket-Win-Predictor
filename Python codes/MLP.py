from  sklearn.neural_network import MLPClassifier
import csv
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

training_data = []
target = []
count = 0
testing_data = []
actual = []

filename1 = 'training1.csv'
file1 = open(filename1, "r")
filename2 = 'testing.csv'
file2 = open(filename2, "r")
filename3 = 'training2.csv'
file3 = open(filename3, "r")

reader1 = csv.reader(file1)
reader2 = csv.reader(file2)
reader3 = csv.reader(file3)

count = 0
for line1 in reader1:
    if count == 0:
        count = 1
        continue

    x = []
    a = float(line1[1])
    x.append(a)
    b = float(line1[2])
    x.append(b)
    c = float(line1[3])
    x.append(c)
    d = float(line1[4])
    x.append(d)
    e = float(line1[5])
    x.append(e)
    f = float(line1[6])
    x.append(f)
    g = float(line1[7])
    x.append(g)
    h = float(line1[8])
    x.append(h)
    i = float(line1[9])
    x.append(i)
    j = float(line1[10])
    x.append(j)
    k = float(line1[11])
    x.append(k)
    l = float(line1[12])
    x.append(l)
    m = float(line1[13])
    x.append(m)
    n = float(line1[14])
    x.append(n)
    o = float(line1[15])
    x.append(o)
    p = float(line1[16])
    target.append(p)
    #print(x)
    training_data.append(x)


#print(training_data)
#print("###############")
print(target)
#print("###############")

count = 0
for line2 in reader2:
    if count == 0:
        count = 1
        continue

    x = []
    a = float(line2[1])
    x.append(a)
    b = float(line2[2])
    x.append(b)
    c = float(line2[3])
    x.append(c)
    d = float(line2[4])
    x.append(d)
    e = float(line2[5])
    x.append(e)
    f = float(line2[6])
    x.append(f)
    g = float(line2[7])
    x.append(g)
    h = float(line2[8])
    x.append(h)
    i = float(line2[9])
    x.append(i)
    j = float(line2[10])
    x.append(j)
    k = float(line2[11])
    x.append(k)
    l = float(line2[12])
    x.append(l)
    m = float(line2[13])
    x.append(m)
    n = float(line2[14])
    x.append(n)
    o = float(line2[15])
    x.append(o)
    p = float(line2[16])
    actual.append(p)
    #print(x)
    testing_data.append(x)

#print(testing_data)
#print("###############")
#print(actual)
#print("###############")

count = 0
for line3 in reader3:
    if count == 0:
        count = 1
        continue

    x = []
    a = float(line3[1])
    x.append(a)
    b = float(line3[2])
    x.append(b)
    c = float(line3[3])
    x.append(c)
    d = float(line3[4])
    x.append(d)
    e = float(line3[5])
    x.append(e)
    f = float(line3[6])
    x.append(f)
    g = float(line3[7])
    x.append(g)
    h = float(line3[8])
    x.append(h)
    i = float(line3[9])
    x.append(i)
    j = float(line3[10])
    x.append(j)
    k = float(line3[11])
    x.append(k)
    l = float(line3[12])
    x.append(l)
    m = float(line3[13])
    x.append(m)
    n = float(line3[14])
    x.append(n)
    o = float(line3[15])
    x.append(o)
    p = float(line3[16])
    target.append(p)
    #print(x)
    training_data.append(x)

#print(validation_data)
#print("###############")
#print(result)
#print("###############")


clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(12, ), random_state=1, activation='relu')

clf.fit(training_data, target)

output = clf.predict(testing_data)
correct = 0
total = len(actual)
for i in range(0, total):
    if (actual[i] == output[i]):
        correct += 1

error = total - correct
print(error)



#print("Complete for Feature :" + str(feature_number));
print("Train Score : " + str(clf.score(training_data, target)));
print("Total test set size : " + str(total));
print("Correct prediction : " + str(correct));
print("Incorrect Prediction : " + str(error));
print("Accuracy : " + str(accuracy_score(actual, output) * 100.0))
print("Precision : " + str(precision_score(actual, output, average='weighted') * 100.0))
print("F1 Score : " + str(f1_score(actual, output, average='weighted') * 100.0))
print("Error Rate : " + str(error / total * 100.0));
#print("---------------------------------------\n");