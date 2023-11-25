import pandas as pd
import numpy as np

def proportion_of_education():
    
    df = pd.read_csv("assets/NISPUF17.csv", index_col = 0)
    
    EDUS = df['EDUC1']
    edus = np.sort(EDUS.values)
    
    poe = {"less than high school": 0,
        "high school": 0,
        "more than high school but not college": 0,
        "college": 0}
    n = len(edus)
    
    poe["less than high school"] = np.sum(edus == 1)/n
    poe["high school"] = np.sum(edus == 2)/n
    poe["more than high school but not college"] = np.sum(edus == 3)/n
    poe["college"] = np.sum(edus == 4)/n
    
    return poe
    raise NotImplementedError()
