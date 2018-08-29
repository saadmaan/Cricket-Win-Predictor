from  sklearn.neural_network import MLPClassifier
import csv
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

clf = MLPClassifier(hidden_layer_sizes=(2, ), activation='tanh', solver='sgd', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=200, shuffle=True, random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
 
training_data = []
target = []
count = 0
testing_data = []
actual = []

trainingFolder = 'C:\Project 300\espncricinfoDatasets'
testingFolder = 'C:\Project 300\espncricinfoDatasets'


filename = trainingFolder+"NeuralNetworkPreviousDatas.csv"
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
    d = float(line[3])
    X.append(d)
    e = float(line[4])
    X.append(e)
    f = float(line[5])
    X.append(f)
    g = float(line[6])
    X.append(g)
    h = float(line[7])
    X.append(h)
    i = float(line[8])
    X.append(i)
    j = float(line[9])
    X.append(j)
    k = float(line[10])
    X.append(k)
    l = float(line[11])
    X.append(l)
    m = float(line[12])
    X.append(m)
    o = float(line[13])
    X.append(o)
    p = float(line[15])
    X.append(p)
    #q = float(line[16])
    #X.append(q)
    r = float(line[17])
    X.append(r)
    #s = float(line[18])
    #X.append(s)
    t = float(line[19])
    X.append(t)
    u = float(line[20])
    X.append(u)
   

    n = float(line[14])
    if (n != 0 and n!= 1):
        continue
    target.append(n)
    #print(X)
    training_data.append(X)
print(target)
print(len(target))

clf.fit(training_data, target)

for i in range(401, 486):
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
    d = float(line[3])
    X.append(d)
    e = float(line[4])
    X.append(e)
    f = float(line[5])
    X.append(f)
    g = float(line[6])
    X.append(g)
    h = float(line[7])
    X.append(h)
    i = float(line[8])
    X.append(i)
    j = float(line[9])
    X.append(j)
    k = float(line[10])
    X.append(k)
    l = float(line[11])
    X.append(l)
    m = float(line[12])
    X.append(m)
    o = float(line[14])
    X.append(o)
    p = float(line[15])
    X.append(p)
    #q = float(line[16])
    #X.append(q)
    r = float(line[17])
    X.append(r)
    s = float(line[18])
    X.append(s)
    t = float(line[19])
    X.append(t)
    u = float(line[20])
    X.append(u)
    v = float(line[21])
    X.append(v)
    w = float(line[22])
    X.append(w)
    x = float(line[23])
    X.append(x)
    #y = float(line[24])
    #X.append(y)
    z = float(line[25])
    X.append(z)
    aa = float(line[26])
    X.append(aa)
    ab = float(line[27])
    X.append(ab)
    ac = float(line[28])
    X.append(ac)
    ad = float(line[29])
    X.append(ad)

    n = float(line[13])
    #if (n != 0 and n!= 1):
        #continue
    actual.append(n)
    #print(X)
    testing_data.append(X)

#print(actual)
total = len(actual)
#print(total)

output = clf.predict(testing_data)
correct = 0

#print(output)
accuracy = accuracy_score(actual, output)
for i in range(0, total):
    if (actual[i] == output[i]):
        correct += 1

error = total - correct
#print(error)



#print("Complete for Feature :" + str(feature_number));
#print("Train Score : " + str(clf.score(training_data, target)));
#print("Precision : " + str(precision_score(actual, output, average='weighted') * 100.0))
#print("F1 Score : " + str(f1_score(actual, output, average='weighted') * 100.0))
#print("Error Rate : " + str(error / total * 100.0));
print("---------------------------------------\n");

print("Total test set size : " + str(total));
print("Correct prediction : " + str(correct));
print("Incorrect Prediction : " + str(error));
print("Accuracy : " + str(accuracy * 100.0))

print('DONE')