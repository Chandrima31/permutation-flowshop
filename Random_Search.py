# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 02:07:31 2018

@author: Chandrima D

This is the working code of Question No. 1 (Random Search)
"""

import numpy as np
import statistics
from File_Read_Write import *

def makespan(current_sequence, ptime_ij, no_of_machines):
        cum_ptime_ij = np.zeros((len(current_sequence), no_of_machines)) 

        for i in range(1, len(current_sequence)):
            cum_ptime_ij[i][0] = cum_ptime_ij[i-1][0] + ptime_ij[current_sequence[i-1]][0]
    
        #for j in range(1, no_of_machines):
            #cum_ptime_ij[0][j] = cum_ptime_ij[0][j-1] + ptime_ij[0][current_sequence[j-1]]
    
        for i in range(1, len(current_sequence)):
            for j in range(1, no_of_machines):
                cum_ptime_ij[i][j] = np.maximum(cum_ptime_ij[i - 1][j], \
                cum_ptime_ij[i][j - 1]) + ptime_ij[current_sequence[i-1]][j]

        return cum_ptime_ij[-1][-1]
    
#random search                
def RandomSearch(process_time_ij, n):
    number_of_jobs = process_time_ij.shape[0] 
    number_of_machines = process_time_ij.shape[1]     
    order = np.arange(number_of_jobs) 
    records = np.array([]) 
    
    for i in range(30):
        np.random.seed(i+1)
        random_order = np.random.permutation(order)
        best_span = makespan(random_order, process_time_ij, number_of_machines)
        for j in range(1000*n): 
            random_order = np.random.permutation(order)
            new_span = makespan(random_order, process_time_ij, number_of_machines)
            if(new_span < best_span):
                best_span = new_span
        records = np.append(records, best_span)
    return records 


#main program

def run_programme(all_data):
     for data in all_data:
         print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
         n, m, p_ij = get_matrix(data) #function defined in File_Read_Write
         rec = RandomSearch(p_ij, 2)
         print("No. of Jobs:", n)
         print("No. of Machines:", m)
         print("Processing time matrix: \n Rows-> Jobs, Columns-> Machines \n", p_ij)
         print("Makespan Values: ", rec)
         print('++++++++++++++++++++  End of product',data[0],'++++++++++++++++++++++')
         write_file(n,m,p_ij, rec) #function defined in File_Read_Write
         
         stats=[]
         stats.append(data[0])
         stats.append(min(rec))
         stats.append(max(rec))
         stats.append(statistics.mean(rec))
         stats.append(statistics.stdev(rec))
         store_statistics(stats, 'RS_statistics.csv') #function defined in File_Read_Write
     return
    
run_programme(all_data)






