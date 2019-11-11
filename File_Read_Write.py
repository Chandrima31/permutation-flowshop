# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 06:09:35 2018

@author: Chandrima D

This is a common module for file reading and writing 
We kept the given text file 'flowshop_bman73701.txt' intact and extracted car data from it
This module is invoked by both Random_Search.py and NEH.py while execution

"""
import numpy as np
import csv

def get_data(): 
    lines = []
    with open('flowshop_bman73701.txt', 'r') as f:
        for _ in range(34):
        # ignore the first 34 lines as content starts on line 35
            next(f)
        for line in f:
            if '+' in line:
                line = line.replace('+', '')
            elif 'instance' in line:
                line = line.replace('instance', '')
            elif 'END OF DATA' in line:
                line = line.replace('END OF DATA', '')
            lines.append(line.strip())
    return [line for line in lines if line !=''][:-1]

def clean_data(data):
    clean_data = []
    for i in data:
        try:
            x = list(map(int, i.split()))
            clean_data.append(x)
        except:
            clean_data.append(i)
    return clean_data

def get_matrix(product_data):
    n1 = product_data[2][0]
    m1 = product_data[2][1]
    machines, time = get_work(product_data[3:])
    p1_ij = np.zeros((n1, m1))
    p1_i = time 
    for i in range(n1):
        for j in range(m1):
            num = i * m1 + j
            p1_ij[i][j] = p1_i[num]
    return n1, m1, p1_ij

def get_work(work):
    machines = []
    time = []
    for i in  range(0, len(work)):
        for j in range(0, len(work[i])):
            if ((j==0) and (j%2==0)):        #this will produce the machine number
                machines.append(work[i][j])
            if ((j!=0) and (j%2==1)):
                time.append(work[i][j])      #this will produce the time for job processed
    return(machines, time)

def write_file(n, m, p_ij, rec):
    with open('Results_RS.txt', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(("No. of Jobs:", n))
        writer.writerow(("No. of Machines:", m))
        writer.writerow(("Processing time matrix: \n Rows-> Jobs, Columns-> Machines \n", p_ij))
        writer.writerow(("Makespan Values: ", rec))
    writeFile.close() 


def write_file_with_sequence(n,m,p_ij,seq, bestspan):
    with open('Results_NEH.txt', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(("No. of Jobs:", n))
        writer.writerow(("No. of Machines:", m))
        writer.writerow(("Processing time matrix: \n Rows-> Jobs, Columns-> Machines \n", p_ij))
        writer.writerow(("Best Sequence: ", seq))
        writer.writerow(("Best Makespan: ", bestspan))
    writeFile.close()

def write_file_for_GA(n, m, p_ij, rec):
    with open('Results_GA.txt', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(("No. of Jobs:", n))
        writer.writerow(("No. of Machines:", m))
        writer.writerow(("Processing time matrix: \n Rows-> Jobs, \
                          Columns-> Machines \n", p_ij))
        writer.writerow(("Makespan Values: ", rec))
    writeFile.close()

def writefile_for_GAparam_change_effects(recs, filename):
    with open(filename, 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(recs)
    writeFile.close() 

def store_statistics(rec, filename):
    with open(filename, 'a') as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=['Min', 'Max', 'Mean', 'Std Dev'])
        writer = csv.writer(writeFile)
        writer.writerow(rec)
    writeFile.close() 

# this needs to get executed first for loading Car Data Matrices
data = get_data() 
clean_data = clean_data(data) 

car1_data =  clean_data[:14]
car6_data = clean_data[14:25]
reC05_data = clean_data[25:48]
reC07_data = clean_data[48:71]
reC19_data = clean_data[71:105]

all_data = [car1_data, car6_data, reC05_data, reC07_data, reC19_data]
