import pandas as pd
# 1. Using list of dictionary
lst = [{"C1": 1, "C2": 2},
        {"C1": 5, "C2": 10, "C3": 20}]
# Observe NaN       
print(pd.DataFrame(lst, index = ["R1", "R2"]))
#     C1  C2    C3
# R1   1   2   NaN
# R2   5  10  20.0
# 2. Using dictionary
dc = {"C1": ["1", "3"],
        "C2": ["2","4"]}
print( pd.DataFrame(dc, index = ["R1", "R2"]) )
#    C1 C2
# R1  1  2
# R2  3  4
# 3. Using list
lst = [[52,32],[45,85]]
print(pd.DataFrame(lst, index = list('pq'), columns = list('ab')))
#     a   b
# p  52  32
# q  45  85


df = pd.DataFrame({'A': [10., 20.],
                    'B': "text",
                    'C': [2,60],
                    'D': 3+9j})
print(df)
#       A     B   C       D
# 0  10.0  text   2  (3+9j)
# 1  20.0  text  60  (3+9j)
print(df.dtypes)
# A       float64
# B        object
# C         int64
# D    complex128
# dtype: object 
              
  
print(df.info())


print((df.index))   #index of rows
# RangeIndex(start=0, stop=2, step=1)
print(df.columns)   # index of columns
# Index(['A', 'B', 'C', 'D'], dtype='object')
print(df.values)    # display values of df
# [[10.0 'text' 2 (3+9j)]
#  [20.0 'text' 60 (3+9j)]]
              
