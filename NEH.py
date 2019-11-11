# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 04:08:25 2018

@author: Chandrima D

This is the working code of Question No. 2 (NEH)
"""


import numpy as np
import math
import statistics
from File_Read_Write import *


def cumulative_process_time(machine_index, matrix, m_machines): 
    cumulative_p_time = 0
    for j in range(m_machines):
        cumulative_p_time = cumulative_p_time + matrix[machine_index][j]
    return cumulative_p_time  #returns total process time for one row i.e. for one job

def get_sequence(matrix, no_of_jobs, no_of_machines): 
    sequence_store = []
    for i in range(no_of_jobs):
        sequence_store.append(i)
    return sorted(sequence_store, key=lambda index: cumulative_process_time(index, matrix, no_of_machines), \
                  reverse=True) 

def insertion_in_sequence(sequence, position_to_insert, new_value):
    new_sequence = sequence[:]
    new_sequence.insert(position_to_insert, new_value)
    return new_sequence

def makespan_for_neh(current_sequence, ptime_ij, no_of_machines):
    cum_ptime_ij = np.zeros((len(current_sequence) + 1, no_of_machines)) 

    for i in range(1, len(current_sequence) + 1):
        cum_ptime_ij[i][0] = cum_ptime_ij[i-1][0] + ptime_ij[current_sequence[i-1]][0]
   
    for i in range(1, len(current_sequence) + 1):
        for j in range(1, no_of_machines):
            cum_ptime_ij[i][j] = max(cum_ptime_ij[i - 1][j], cum_ptime_ij[i][j - 1]) + \
            ptime_ij[current_sequence[i-1]][j]
    return cum_ptime_ij

def neh_algo(process_time, jobs, machines):
    ordered_sequence = get_sequence(process_time, jobs, machines) 
    #print(ordered_sequence)
    current_sequence = [ordered_sequence[0]]
    for i in range(1, jobs):
        min_col_max = math.inf #initiate with a very big value
        for j in range(0, i + 1):
            temp_sequence = insertion_in_sequence(current_sequence, j, ordered_sequence[i])
            col_max_temp = makespan_for_neh(temp_sequence, process_time, machines)\
            [len(temp_sequence)][machines - 1]
            #print("Path :",temp_sequence, "Makespan :",col_max_temp) 
            if min_col_max > col_max_temp:
                chosen_sequence = temp_sequence #chosen seq. corr. to path with min. makespan
                min_col_max = col_max_temp
        current_sequence = chosen_sequence
    return current_sequence, makespan_for_neh(current_sequence, process_time, machines)[jobs][machines - 1]


#main program

if __name__ == '__main__':
    def run_programme(all_data):
        for data in all_data:
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            n, m, p_ij = get_matrix(data) 
            seq, bestspan = neh_algo(p_ij, n, m)
            print("No. of Jobs:", n)
            print("No. of Machines:", m)
            print("Processing time matrix: \n Rows-> Jobs, Columns-> Machines \n", p_ij)
            print("Best Sequence: ", seq)
            print("Best Makespan: ", bestspan)
            print('++++++++++++++++++++  End of product ', data[0], '++++++++++++++++++++++')
            write_file_with_sequence(n,m,p_ij,seq, bestspan)
            
            stats=[] #min = max = mean = bestspan; std dev = 0
            stats.append(data[0])
            stats.append(bestspan)
            stats.append(bestspan)
            stats.append(bestspan)
            stats.append(bestspan)
            store_statistics(stats, 'NEH_statistics.csv') 
        return
 
    
    run_programme(all_data)
