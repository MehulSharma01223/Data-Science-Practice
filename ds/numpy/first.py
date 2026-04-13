import numpy as  np
import pandas as  pd 

dict1 ={
    "name" : ["mehul sharma","rohan","Raju","deepak"],
    "Marks" : [45,34,23, 23],
    "city" : ['Rampur','delhi','rajasthan','jaipur']
    }

df = pd.DataFrame(dict1)
print(df)
df.to_csv('freinds.csv')
