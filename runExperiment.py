# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:50:57 2022

@author: ieav-asa
"""

import os
import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Force the Working Directory for the file directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%%%
N = 22
T = 1000

for K in range(22):
    #FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
    args = f'NKTest.exe -n {N} -t {T} -k {K}'
    #subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)
    subprocess.Popen(args, shell=False)
    
#%%%

N = 7
T = 10000
for K in range(6):
    
    #summaryDf = pd.DataFrame(summaryData, columns = ["N","K","peaks","max_values", "min_values"])
    runName = f'./N{N}_IT{T}/Results_N{N}_K{K}_Iterations_{T}'
    summaryDf = pd.read_csv(runName + ".csv", delimiter=';')
    # *** CALCULATING SUMMARY STATISTICS ****************************************
    
    # Let's print some summary statistics of our sample of NK landscapes
    print('\nSummary statistics for IMatrix: ' + ' K=' + str(K))
    print('average number of peaks: ' + str(np.mean(summaryDf.peaks)))
    print('maximum number of peaks: ' + str(np.max(summaryDf.peaks)))
    print('minimum number of peaks: ' + str(np.min(summaryDf.peaks)))
    print('average maximum value: ' + str(np.mean(summaryDf.maxValue)))
    print('average minimum value: ' + str(np.mean(summaryDf.minValue)))        
    
     
    #plot histogram of the number of local peaks in our sample
    plt.figure(1, facecolor='white', figsize=(8, 6), dpi=150)  # for screens with
    #higher resolution change dpi to 150 or 200. For normal use 75.
    plt.hist(summaryDf.peaks, bins=20, range=(1, 20), color='dodgerblue', edgecolor='black') # adjust if necessary
    plt.title(f'Distribution of the number of peaks - N={N} / K={K} / Runs={T}', size=12)
    plt.xlabel('number of peaks', size=10)
    plt.ylabel('frequency', size=10)    
    plt.savefig(runName + ".png")
    plt.show()
