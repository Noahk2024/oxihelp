import estimateBP
import pandas as pd
import random
from math import sqrt
data_list = []

dataframe = pd.read_excel('PPG-BP-dataset.xlsx')

bmi_col = dataframe["Unnamed: 9"].values.tolist()
systolic_blood_pressure_col = dataframe["Unnamed: 6"].values.tolist()
bp_col = dataframe["Unnamed: 8"].values.tolist()
names = dataframe['Hospital Electronic Medical Record'].values.tolist()

def build_tuples():
    for i in range(1, len(bmi_col)):
        data_list.append((bmi_col[i], systolic_blood_pressure_col[i], bp_col[i], names[i]))
#print(estimateBP.find_bp.get_bp(107, 21.6))#bp and bmi

def stable(old, new):
    for key in old:
        if key not in new:
            return False
    return True
        

#K=5
K = 13
build_tuples()

means_list = random.sample(data_list, K)
means = {}
for me in means_list:
    means[me] = []
old_means = {0:{}}
new_means = {1:{}}
while not stable(old_means, new_means):
    for vector in data_list:
        min_dist = 10**10
        min_mean = 0
        for me in means:
            dist = sqrt(sum([(vector[i] - me[i])**2 for i in range(3)]))
            if dist < min_dist:
                min_dist = dist
                min_me = me
        means[min_me].append(vector)
    
    new_means = {}
    for me in means:
        avg, avg1, avg2= 0, 0, 0
        for vector in means[me]:
            #print(vector)
            avg += vector[0]
            avg1 += vector[1]
            avg2 += vector[2]
            
            
        l = len(means[me])
       
        #print(l)
        average = (float(avg/l), float(avg1/l), float(avg2/l))
        new_means[average] = []
    old_means = means
    means = new_means
#for key in old_means:
#    print(f"Mean: {key}")
#    print(old_means[key])
#    print()

classification = {'Prehypertension': 0, 'Hypertension': 0 , 'Normal':0, 'Stage 1 hypertension':0, 'Stage 2 hypertension':0}
medial_class_list = {}


for key in old_means:
    curr_mean = classification.copy()
    for vector in old_means[key]:
        curr_mean[vector[3]] += 1
    curr_max = 0
    curr_max_key = ''
    second_max = 0
    second_max_key = ''
    for key1 in curr_mean:
        if curr_mean[key1] > curr_max:
            second_max = curr_max
            second_max_key = curr_max_key
            curr_max = curr_mean[key1]
            curr_max_key = key1
        elif curr_mean[key1] > second_max:
            second_max = curr_mean[key1]
            second_max_key = key1
    if curr_max/4 < second_max:
        medial_class_list[curr_max_key + "," + second_max_key] = key
    else:
        medial_class_list[curr_max_key] = key

print(medial_class_list)
    


#Classification Groups are: 
#class_list = set(dataframe['Hospital Electronic Medical Record'].values.tolist())
#
#print(class_list)

