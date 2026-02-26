import pandas as pd
li = [1, 4, 7, 8, 3 ,9]
df = pd.Series(li)       #Use Series() to create a series of data
print(df)
dict = {
  "name": ["akshay", "Vivek", "aish"],
  "age": [55, 48, 45]
}
df = pd.DataFrame(dict)
print(df)
