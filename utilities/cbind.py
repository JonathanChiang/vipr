'''
[stackoverflow](https://stackoverflow.com/questions/28595701/pandas-equivalent-of-rs-cbind-concatenate-stack-vectors-vertically)
import pandas

test1 = pandas.DataFrame([1,2,3,4,5])
test2 = pandas.DataFrame([4,2,1,3,7])

Should end up like this: 
cbindR(test1,test2)
   v0  v1
0   1   5
1   2   4
2   3   3
3   4   2
4   5   1

'''

def cbindR(df1, df2):
  df3 = pd.concat([df1, df2], axis=1)
  df3.columns = ['v0','v1'] 
  return df3
