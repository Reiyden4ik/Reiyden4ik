#It would be interesting to see if there is any evidence of a link between vaccine effectiveness
#and sex of the child. Calculate the ratio of the number of children who contracted chickenpox
#but were vaccinated against it (at least one varicella dose) versus 
#those who were vaccinated but did not contract chicken pox. Return results by sex.

import pandas as pd
def chickenpox_by_sex():
    df = pd.read_csv('your_dataset.csv')  
    filtered_df = df[(df['HAD_CPOX'] == 1) & (df['P_NUMVRC'] >= 1)]
    male_count = len(filtered_df[filtered_df['SEX'] == 1])  
    female_count = len(filtered_df[filtered_df['SEX'] == 2])  
    male_ratio = male_count / (len(filtered_df) - male_count)
    female_ratio = female_count / (len(filtered_df) - female_count)
    result = {
        "male": round(male_ratio, 1),  
        "female": round(female_ratio, 1)
    }
    return result
print(chickenpox_by_sex())
'''
A correlation is a statistical relationship between two variables. 
If we wanted to know if vaccines work, we might look at the correlation between
the use of the vaccine and whether it results in prevention of the infection or disease [1]. 
In this question, you are to see if there is a correlation between having had the chicken pox
and the number of chickenpox vaccine doses given (varicella).
Some notes on interpreting the answer. The had_chickenpox_column
is either 1 (for yes) or 2 (for no), and the num_chickenpox_vaccine_column 
is the number of doses a child has been given of the varicella vaccine. 
A positive correlation (e.g., corr > 0) means that an increase in had_chickenpox_column
(which means more no’s) would also increase the values of num_chickenpox_vaccine_column
(which means more doses of vaccine). If there is a negative correlation (e.g., corr < 0), 
it indicates that having had chickenpox is related to an increase in the number of vaccine doses.
Also, pval is the probability that we observe a correlation between had_chickenpox_column 
and num_chickenpox_vaccine_column which is greater than or equal to a particular value 
occurred by chance. A small pval means that the observed correlation is highly unlikely 
to occur by chance. In this case, pval should be very small 
(will end in e-18 indicating a very small number).
[1] This isn’t really the full picture, since we are not looking at when the dose was given.
It’s possible that children had chickenpox and then their parents went to get them the vaccine.
Does this dataset have the data we would need to investigate the timing of the dose?
'''
import scipy.stats as stats
import numpy as np
import pandas as pd

def corr_chickenpox():
    df = pd.DataFrame({
        "had_chickenpox_column": np.random.randint(1, 3, size=(100)),
        "num_chickenpox_vaccine_column": np.random.randint(0, 6, size=(100))
    })
    corr, pval = stats.pearsonr(df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"])
    return corr, pval
corr, pval = corr_chickenpox()
print("Correlation:", corr)
print("P-value:", pval)
