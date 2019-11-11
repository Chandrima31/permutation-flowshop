# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 06:09:35 2018

@author: Chandrima D

This is the working code of Question No. 4 - Part(i) (effects of change in population_size, 
p_crossover, p_mutation_initial, threshold parameters for Genetic Algorithm)
"""

from File_Read_Write import *
from Genetic_Algorithm import genetic_algorithm


pop_size = [5, 10, 20, 50, 100]
p_crossover = [0.5, 0.7, 0.9]
p_mutation_initial = [0.2, 0.4, 0.6, 1.0]
threshold = [0.0, 0.5, 1.0]


#to observe the effect of change in pop_size keeping other parameters intact
def run_effect_of_change_in_pop_size(all_data):
    for data in all_data:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        n, m, p_ij = get_matrix(data) 
        for i in range(5):
            rec = genetic_algorithm(n,m,p_ij,2,pop_size[i],1,0.8,0.95)
            print("Makespan Values for pop-size ", pop_size[i], "is: ", rec)
        print('++++++++++++++++++++  End of product',data[0],'++++++++++++++++++++++')
        recs = []
        recs.append(data[0])
        recs.append(rec)
        writefile_for_GAparam_change_effects(recs, 'Effect_of_change_in_PopSize.csv') 
 
    return
       
# to observe the effect of change in p_crossover keeping other parameters intact
# program does not run if p_crossover = 0.0
def run_effect_of_change_in_p_crossover(all_data):
    for data in all_data:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        n, m, p_ij = get_matrix(data) 
        for i in range(3):
            rec = genetic_algorithm(n,m,p_ij,2,30,p_crossover[i],0.8,0.95)
            print("Makespan Values for p_crossover ", p_crossover[i], "is: ", rec)
        print('++++++++++++++++++++  End of product',data[0],'++++++++++++++++++++++')
        recs = []
        recs.append(data[0])
        recs.append(rec)
        writefile_for_GAparam_change_effects(recs, 'Effect_of_change_in_p_crossover.csv') 
 
    return
    
# to observe the effect of change in p_mutation_initial keeping other parameters intact
# program does not run if p_mutation_initial = 0.0    
def run_effect_of_change_in_p_mutation_init(all_data):
    for data in all_data:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        n, m, p_ij = get_matrix(data) 
        for i in range(4):
            rec = genetic_algorithm(n,m,p_ij,2,30,1,p_mutation_initial[i],0.95)
            print("Makespan Values for p_mutation ", p_mutation_initial[i], "is: ", rec)
        print('++++++++++++++++++++  End of product',data[0],'++++++++++++++++++++++')
        recs = []
        recs.append(data[0])
        recs.append(rec)
        writefile_for_GAparam_change_effects(recs, 'Effect_of_change_in_p_mutation_init.csv') 
 
    return
    
# to observe the effect of change in threshold_parameter keeping other parameters intact   
def run_effect_of_change_in_threshold(all_data):
    for data in all_data:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        n, m, p_ij = get_matrix(data) 
        for i in range(3):
            rec = genetic_algorithm(n,m,p_ij,2,30,1,0.8,threshold[i])
            print("Makespan Values for threshold ", threshold[i], "is: ", rec)
        print('++++++++++++++++++++  End of product',data[0],'++++++++++++++++++++++')
        recs = []
        recs.append(data[0])
        recs.append(rec)
        writefile_for_GAparam_change_effects(recs, 'Effect_of_change_in_threshold.csv') 
 
    return

#main program
run_effect_of_change_in_pop_size(all_data)   
run_effect_of_change_in_p_crossover(all_data) 
run_effect_of_change_in_p_mutation_init(all_data)
run_effect_of_change_in_threshold(all_data)





































