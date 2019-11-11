# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 03:03:39 2018

@author: Chandrima D

This is the working code of Question No. 4 - Part(ii) (visualizing the effects of change 
in population_size, p_crossover, p_mutation_initial, threshold parameters for Genetic Algorithm 
and comparing them against Random Search and NEH makespan results through BoxPlots)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data(filename):   
    with open(filename, "r") as f:
        n1 = int(f.readline())
        m1 = int(f.readline())
        p1_ij = np.zeros((n1, m1))
        for i in range(n1):
            p1_i = f.readline().split()
            for j in range(m1):
                p1_ij[i][j] = int(p1_i[j])
    return n1, m1, p1_ij
    
# Comparison of performance of each car matrix for 3 different algorithms
def visualize_popsize_effect(filename, car_name):
    path = ""
    file_name = filename
    n, m, p_ij = get_data(path+file_name) 
    arr = np.array(p_ij)
    np_arr = np.transpose(arr)
    df = pd.DataFrame(np_arr, columns=['Random Search', 'NEH', 'GA_popsize5', 'GA_popsize10', 'GA_popsize20', 'GA_popsize30', 'GA_popsize50', 'GA_popsize100'])
    df.boxplot(return_type='axes', figsize=(12,6), showmeans = True, meanline = True)
    plt.title('Comparison of Performance and Effect of Change in population_size for '+car_name, fontsize = 16, color = 'green', weight = 'semibold')
    plt.xlabel('Car Matrices', fontsize = 12)
    plt.ylabel('Makespan Values', fontsize = 12)
    plt.show()
    return

def visualize_p_crossover_effect(filename, car_name):
    path = ""
    file_name = filename
    n, m, p_ij = get_data(path+file_name) 
    arr = np.array(p_ij)
    np_arr = np.transpose(arr)
    df1 = pd.DataFrame(np_arr, columns=['Random Search', 'NEH', 'GA_p_crossover0.5', 'GA_p_crossover0.7', 'GA_p_crossover0.9', 'GA_p_crossover1'])
    df1.boxplot(return_type='axes', figsize=(12,6), showmeans = True, meanline = True)
    plt.title('Comparison of Performance and Effect of Change in p_crossover for car1', fontsize = 16, color = 'green', weight = 'semibold')
    plt.xlabel('Car Matrices', fontsize = 12)
    plt.ylabel('Makespan Values', fontsize = 12)
    plt.show()
    return

def visualize_p_mutation_effect(filename, car_name):
    path = ""
    file_name = filename
    n, m, p_ij = get_data(path+file_name) 
    arr = np.array(p_ij)
    np_arr = np.transpose(arr)
    df2 = pd.DataFrame(np_arr, columns=['Random Search', 'NEH', 'GA_p_mutation0.2', 'GA_p_mutation0.4', 'GA_p_mutation0.6', 'GA_p_mutation0.8', 'GA_p_mutation1'])
    df2.boxplot(return_type='axes', figsize=(12,6), showmeans = True, meanline = True)
    plt.title('Comparison of Performance and Effect of Change in p_mutation for '+car_name, fontsize = 16, color = 'green', weight = 'semibold')
    plt.xlabel('Car Matrices', fontsize = 12)
    plt.ylabel('Makespan Values', fontsize = 12)
    plt.show()
    return

def visualize_threshold_effect(filename, car_name):
    path = ""
    file_name = filename
    n, m, p_ij = get_data(path+file_name) 
    arr = np.array(p_ij)
    np_arr = np.transpose(arr)
    df3 = pd.DataFrame(np_arr, columns=['Random Search', 'NEH', 'GA_threshold0', 'GA_threshold0.5', 'GA_threshold0.95', 'GA_threshold1'])
    df3.boxplot(return_type='axes', figsize=(12,6), showmeans = True, meanline = True)
    plt.title('Comparison of Performance and Effect of Change in threshold for '+car_name, fontsize = 16, color = 'green', weight = 'semibold')
    plt.xlabel('Car Matrices', fontsize = 12)
    plt.ylabel('Makespan Values', fontsize = 12)
    plt.show()   
    return

visualize_popsize_effect('All_results_car1_for_popsize.txt', "car1")
visualize_p_crossover_effect('All_results_car1_for_p_crossover.txt', "car1")
visualize_p_mutation_effect('All_results_car1_for_p_mutation.txt', "car1")
visualize_threshold_effect('All_results_car1_for_threshold.txt', "car1")

visualize_popsize_effect('All_results_car6_for_popsize.txt', "car6")
visualize_p_crossover_effect('All_results_car6_for_p_crossover.txt', "car6")
visualize_p_mutation_effect('All_results_car6_for_p_mutation.txt', "car6")
visualize_threshold_effect('All_results_car6_for_threshold.txt', "car6")

visualize_popsize_effect('All_results_reC05_for_popsize.txt', "reC05")
visualize_p_crossover_effect('All_results_reC05_for_p_crossover.txt', "reC05")
visualize_p_mutation_effect('All_results_reC05_for_p_mutation.txt', "reC05")
visualize_threshold_effect('All_results_reC05_for_threshold.txt', "reC05")

visualize_popsize_effect('All_results_reC07_for_popsize.txt', "reC07")
visualize_p_crossover_effect('All_results_reC07_for_p_crossover.txt', "reC07")
visualize_p_mutation_effect('All_results_reC07_for_p_mutation.txt', "reC07")
visualize_threshold_effect('All_results_reC07_for_threshold.txt', "reC07")

visualize_popsize_effect('All_results_reC19_for_popsize.txt', "reC19")
visualize_p_crossover_effect('All_results_reC19_for_p_crossover.txt', "reC19")
visualize_p_mutation_effect('All_results_reC19_for_p_mutation.txt', "reC19")
visualize_threshold_effect('All_results_reC19_for_threshold.txt', "reC19")



