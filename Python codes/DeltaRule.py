from random import choice
from numpy import array, dot, random
import csv
import matplotlib.pyplot
import pylab

unit_step = lambda x: 0 if x < 0 else 1

training_data = []
validation_data = []
testing_data = []
count1 = 0
count2 = 0
count3 = 0

iterator_count = []
error_count = []

filename1 = 'training.csv'
file1 = open(filename1, "r")
filename2 = 'validation.csv'
file2 = open(filename2, "r")
filename3 = 'testing.csv'
file3 = open(filename3, "r")

reader1 = csv.reader(file1)
reader2 = csv.reader(file2)
reader3 = csv.reader(file3)

for line1 in reader1:
    if count1 == 0:
        count1 = 1
        continue

    a = float(line1[1])
    b = float(line1[2])
    c = float(line1[3])
    d = float(line1[4])
    e = float(line1[5])
    f = float(line1[6])
    g = float(line1[7])
    h = float(line1[8])
    i = float(line1[9])
    j = float(line1[10])
    k = float(line1[11])
    l = float(line1[12])
    m = float(line1[14])
    n = float(line1[15])
    o = float(line1[16])
    p = float(line1[13])

    training_data.append([array([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, -1]), p])

for line1 in reader2:
    if count2 == 0:
        count2 = 1
        continue

    a = float(line1[1])
    b = float(line1[2])
    c = float(line1[3])
    d = float(line1[4])
    e = float(line1[5])
    f = float(line1[6])
    g = float(line1[7])
    h = float(line1[8])
    i = float(line1[9])
    j = float(line1[10])
    k = float(line1[11])
    l = float(line1[12])
    m = float(line1[14])
    n = float(line1[15])
    o = float(line1[16])
    p = float(line1[13])

    validation_data.append([array([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, -1]), p])

for line1 in reader3:
    if count3 == 0:
        count3 = 1
        continue

    a = float(line1[1])
    b = float(line1[2])
    c = float(line1[3])
    d = float(line1[4])
    e = float(line1[5])
    f = float(line1[6])
    g = float(line1[7])
    h = float(line1[8])
    i = float(line1[9])
    j = float(line1[10])
    k = float(line1[11])
    l = float(line1[12])
    m = float(line1[14])
    n = float(line1[15])
    o = float(line1[16])
    p = float(line1[13])

    testing_data.append([array([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, -1]), p])


w = random.rand(16)
w_min = random.rand(16)
#print(w)

errors = []
eta = 0.2
n = 50001

minimum_error = 100001

for ii in range(n):
    for jj in range(1,302):
        x, expected = choice(training_data)  # one from data list
        result = dot(w, x)
        error = expected - result

        # print('weight')
        # print(w)
        # print('data')
        # print(x)

        #print('result')
        #print(result)
        #print('expected')
        #print(expected)
        #print('mapped result')
        #print(unit_step(result))

        #print('error')
        #print(error)

        errors.append(error)
        #print(errors)
        w += eta * error * x

    if ii % 1000 == 0:
        errorCount = 0
        for kk in range(1, 78):
            y, expected2 = choice(validation_data)
            validation_result = unit_step(dot(w, y))
            #print(validation_result)
            #print(str(expected2)+" "+str(validation_result))
            if expected2 != validation_result:
                errorCount += 1
        print(str(ii)+" "+str(errorCount))
        iterator_count.append(ii/1000)
        error_count.append(error_count)
        if(minimum_error > errorCount):
            w_min = w
            minimum_error = errorCount


#print('baicha asen')
#matplotlib.pyplot.scatter(iterator_count, error_count)

#matplotlib.pyplot.show()

errorCount = 0
for xx in range(1, 75):
    z, expected3 = choice(testing_data)
    final_result = unit_step(dot(w_min, z))
    # print(validation_result)
    # print(str(expected2)+" "+str(validation_result))
    if expected3 != final_result:
        errorCount += 1
print(str(errorCount))
print(str(100 - (errorCount/75)*100)+"%")
