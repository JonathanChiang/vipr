'''
# https://stackoverflow.com/questions/14988480/pandas-version-of-rbind

df1 = pd.DataFrame({'col1': [1,2], 'col2':[3,4]})
df2 = pd.DataFrame({'col1': [5,6], 'col2':[7,8]})
print(df1)
print(df2)
print(pd.concat([df1, df2]))

only binds two dataframes for now: 
should be able to bind multiple at once

pd.concat([df1, df2]) == rbind(df1, df2) 

'''

import pandas as pd
def rbind(df1, df2):
  return pd.concat([df1,df2])
 
