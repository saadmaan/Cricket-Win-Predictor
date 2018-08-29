import csv
import pandas as pd

input_file = 'NeuralNetwork.csv'
output_file = open("training.csv",'w',newline="\r\n")
file1 = open(input_file, "r")

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[], []]
count = 0

reader1 = csv.reader(file1)

for line1 in reader1:
    #print(line1[0])
    if count == 0:
        count = 1
        continue

    index = line1[0]
    count += 1
    #print(index)

    if int(index) > 328:
        break

    team1Count = int(line1[16])
    team2Count = int(line1[18])

    print(count)
    print(str(team1Count)+" "+str(team2Count))
    #print(team2Count)
    if team1Count > 3 and team2Count > 3:
        print('yes')
        col1.append(line1[1])
        col2.append(line1[2])
        col3.append(line1[3])
        col4.append(line1[4])
        col5.append(line1[5])
        col6.append(line1[6])
        col7.append(line1[7])
        col8.append(line1[8])
        col9.append(line1[9])
        col10.append(line1[10])
        col11.append(line1[11])
        col12.append(line1[12])
        col13.append(line1[13])
        col14.append(line1[14])
        col15.append(line1[19])
        col16.append(line1[20])

data_set = pd.DataFrame({
    'Batting Avg All': pd.Series(col1),
    'Batting Avg Rec': pd.Series(col2),
    'Batting Ball By Wicket All': pd.Series(col3),
    'Batting Ball By Wicket Rec': pd.Series(col4),
    'Batting Strike Rate All': pd.Series(col5),
    'Batting Strike Rate Rec': pd.Series(col6),
    'Bowling Avg All': pd.Series(col7),
    'Bowling Avg Rec': pd.Series(col8),
    'Bowling Eco All': pd.Series(col9),
    'Bowling Eco Rec': pd.Series(col10),
    'Bowling Strike Rate All': pd.Series(col11),
    'Bowling Strike Rate Rec': pd.Series(col12),
    'Current Winner': pd.Series(col13),
    'Face To Face Win Diff': pd.Series(col14),
    'Win Percentage All': pd.Series(col15),
    'Win Percentage Rec': pd.Series(col16),

})

data_set.to_csv(output_file,encoding='utf-8')


