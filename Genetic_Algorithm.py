# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 06:09:35 2018

@author: Chandrima D

This is the working code of Question No. 3 (Genetic Algorithm)
"""

import numpy as np
import pandas as pd 
import random
import statistics
from NEH import neh_algo
from File_Read_Write import *
            
def makespan(sequence, processing_time, number_of_machines):
    number_of_jobs = len(sequence) - 1
    cp = [0] * number_of_jobs
    for machine_no in range(0, number_of_machines):
        for i in range(number_of_jobs):
            cp_span = cp[i]
            if i > 0:
               cp_span = max(cp[i - 1], cp[i])
               cp[i] = cp_span + processing_time[sequence[i]][machine_no]
    return cp[number_of_jobs - 1]
    
    
def initialize_population(population_size, number_of_jobs):
    population = []
    i = 0
    while i < population_size:
        individual = list(np.random.permutation(number_of_jobs))
        if individual not in population:
            population.append(individual)
            i += 1
    return population

def crossover(parents):
    #2-point crossover
    parent1 = parents[0]
    parent2 = parents[1]
    
    length_of_parent1 = len(parent1)
    first_point1 = random.randint(0,int((length_of_parent1 - 1)/2))
    second_point1 = int(length_of_parent1 - first_point1)
    left1 = parent1[0:first_point1] 
    intersect1 = parent1[first_point1:second_point1]
    right1 = parent1[second_point1:length_of_parent1]
    
    length_of_parent2 = len(parent2)
    first_point2 = first_point1 
    second_point2 = second_point1
    left2 = parent2[0:first_point2]
    intersect2 = parent2[first_point2:second_point2]
    right2 = parent2[second_point2:length_of_parent2] 
    
    intersect1_random = np.random.permutation(intersect1)
    intersect2_random = np.random.permutation(intersect2)
    
    global child1
    global child2
    child1 = np.append(left1,intersect1_random)
    child2 = np.append(left2,intersect2_random)
    child1_copy = np.copy(child1)
    child2_copy = np.copy(child2) 

    
    for i in range(len(right2)):
        if right2[i] in child1_copy:
           child1 = np.append(child1,right1[i])
        else:
           child1 = np.append(child1,right2[i])
    
    for j in range(len(right1)):
       if right1[j] in child2_copy:
          child2 = np.append(child2,right2[j])
       else:
          child2 = np.append(child2,right1[j])
    
    child1 = child1.astype("int") 
    child2 = child2.astype("int")
    return child1, child2


def mutate(child):
    #exchange mutation
    len_child = len(child)
    i = np.random.randint(0,len_child-1)
    j = np.random.randint(0,len_child-1)
    while(j == i):
        j = np.random.randint(0,len_child-1)
    global mutated_child
    mutated_child = list(child)
    x = mutated_child[i]  
    y = mutated_child[j]
    mutated_child[i] = y 
    mutated_child[j] = x
    return mutated_child 

def genetic_algorithm(n, m, p_ij, n1, pop_size, p_crossover, p_mutation_initial, threshold):
    neh_seq, bestspan = neh_algo(p_ij, n, m) #first sequence is NEH
    theta = 0.99 
    d = threshold
    global df5 
    # Initialize population
    population = initialize_population(pop_size,n)
    population.append(neh_seq) 

    store_span = [] 
    store_seq = [] 
    for i in range(pop_size):
        current_span = makespan(population[i],p_ij,m)
        seq = population[i]
        store_span.append(current_span)
        store_seq.append(seq) 

    df = pd.DataFrame(np.zeros((pop_size,2)))  
    df = df.astype("object")
    df = pd.DataFrame(list(zip(store_seq,store_span)),columns=["Sequence","Makespan"]) 
    df1 = df.sort_values(by ="Makespan",ascending= True)     
    df1["Rank"] = range(1,pop_size+1)    
    min_makespan = np.min(df1["Makespan"])  
    mean_makespan = np.mean(df1["Makespan"]) 
    med_rank = np.median(df1["Rank"]) 
    fit_population = df1[0:int(med_rank)]
    unfit_population = df1[int(med_rank):pop_size] 
    p_mutation = p_mutation_initial 

    results = [] 
    for run in range(pop_size):
        for k in range(1000*n1):
            random.seed(run) 
            r1 = np.random.random()
            if r1 < p_crossover:
                random_rank_p1 = np.random.randint(1,int(med_rank))
                index1 = fit_population.index[random_rank_p1 - 1]
                parent1 = fit_population.loc[index1][0] 
                random_rank_p2 = np.random.randint(2,pop_size)
                index2 = df1.index[random_rank_p2 -1]
                parent2 = df1.loc[index2][0]
                global parents 
                parents = [parent1,parent2] 
                child1, child2 = crossover(parents)
        
        
            r2 = np.random.random() 
            if r2 < p_mutation:
                child = [child1,child2] 
                child_rand = np.random.randint(0,1) 
                mutate(child[child_rand])
                makespan(mutated_child,p_ij,m) 
                random_rank_p3 = np.random.randint(int(med_rank)+1,pop_size)
                index3 = unfit_population.index[random_rank_p3 - int(med_rank) - 1] 
                #old_sequence = unfit_population.loc[index3][0]
                df2 = df1.drop(index3)
                df3 = df2.drop("Rank",axis=1) 
                new_sequence = mutated_child
                new_sequence_makespan = makespan(mutated_child,p_ij,m) 
                df4 = df3.append({"Sequence":new_sequence, "Makespan":new_sequence_makespan},ignore_index=True)
                global df5 
                df5 = df4.sort_values(by ="Makespan",ascending= True)     
                df5["Rank"] = range(1,pop_size+1)
        
                min_makespan = np.min(df5["Makespan"]) 
                mean_makespan = np.mean(df5["Makespan"])         
                fit_population = df5[0:int(med_rank)]
                unfit_population = df5[int(med_rank):pop_size]
                del df1
                df1 = fit_population.append(unfit_population)
                med_rank = np.median(df1["Rank"])
        
                p_mutation = theta * p_mutation
                ratio = min_makespan/mean_makespan
                if ratio > d:
                    p_mutation = p_mutation_initial
                # = df1.loc[df1.index[0]][0]  
                best_makespan = df1.loc[df1.index[0]][1]    
        results.append(best_makespan) 
    return results 



#main program
if __name__ == '__main__':    
    def run_programme(all_data):
        for data in all_data:
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            n, m, p_ij = get_matrix(data) #function defined in File_Read_Write
            rec = genetic_algorithm(n,m,p_ij,1,30,1,0.8,0.95)
            print("No. of Jobs:", n)
            print("No. of Machines:", m)
            print("Processing time matrix: \n Rows-> Jobs, Columns-> Machines \n", p_ij)
            print("Makespan Values for Genetic Algorithm: ", rec)
            print('++++++++++++++++++++  End of product',data[0],'++++++++++++++++++++++')
            write_file_for_GA(n,m,p_ij, rec) #function defined in File_Read_Write
         
            stats=[]
            stats.append(data[0])
            stats.append(min(rec))
            stats.append(max(rec))
            stats.append(statistics.mean(rec))
            stats.append(statistics.stdev(rec))
            store_statistics(stats, 'GA_statistics.csv') 
        return
    
    run_programme(all_data)













