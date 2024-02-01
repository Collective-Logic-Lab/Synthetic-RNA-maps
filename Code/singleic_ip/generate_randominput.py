"""
Ayomide Laguda 11/16/23
We created a python script that generates an input file for BoolODE.
"""
import pandas as pd
import random
import numpy as np
import sys

def label_to_state (label, digits):
    return np.array(list(map(int,list(format(label,'0'+str(digits)+'b')))))

def generate_randomicfile(filename): 
    """
    This function reads the gene names from the given network file, 
    creates random initial conditions for those genes, 
    and produces an IC file called rand_ICS.txt.
    
    To do: Check what BoolODE does in all zeros and all ones cases.
    """
    df = pd.read_csv(filename, sep='\t')
    
    Gene_names = list(df.Gene)
    n = len(Gene_names)
    x = random.randint(0,(2^n)-1)
    
    s = label_to_state(x,n)
    
    # Input Convention of BoolODE(we think):
    #
    # EXAMPLE 1
    # ['g1','g3']  [1,1]
    # g1 and g3 start as on and all other genes start as off
    #
    # EXAMPLE 2
    # ['g1','g3']  [0,1]
    # g1 is pinned to zero forever, g3 starts at one, and all other genes start as off
    
    p1 = str([ Gene_names[i] for i in range(n) if s[i] == 1 ])
    p2 = str( [1 for i in range(np.sum(s))] )
    
    f = open("rand_ICS.txt", "w")
    f.writelines([
    "Genes"+"\t"+"Values"+"\n",
    p1+"\t"+p2
    ])
    f.close()
    
if __name__== "__main__":
    if len(sys.argv) == 2:
        generate_randomicfile(sys.argv[1])
    else:
        print("ERROR: The desired usage is python generate_randominput.py input_file !!!")
