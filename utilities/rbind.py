'''
# https://stackoverflow.com/questions/14988480/pandas-version-of-rbind

Example 1
---------

df1 = pd.DataFrame({'col1': [1,2], 'col2':[3,4]})
df2 = pd.DataFrame({'col1': [5,6], 'col2':[7,8]})
print(df1)
print(df2)
print(pd.concat([df1, df2]))

only binds two dataframes for now: 
should be able to bind multiple at once

pd.concat([df1, df2]) == rbind(df1, df2) 

Example 2
---------

import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(iris.data[:, :], columns = ["f{}".format(i) for i in range(1,5)])  
dfs = [df for i in range(10)]

rbind(dfs)

'''

import numpy as pd
import pandas as pd

def rbind(*dfs):
    
    # Add assertion for all sets of columns being equal

    result = pd.concat(dfs[0], axis = 0, ignore_index = True)
    
    return result
 
