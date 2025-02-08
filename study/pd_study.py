import pandas as pd
import numpy as np
csv_path=r"D:\aguo\数据集\临时\archive\Titanic-Dataset.csv"
df=pd.read_csv(csv_path)


result=df.groupby('Pclass').agg({'Fare':'mean','Survived':'mean'}).reset_index()
print(result)



# survived_cl=df['Survived']
# total=len(survived_cl)
# # print(total)
# counts=survived_cl.value_counts()
# # print(counts)
# n_0=counts.get(0)
# n_1=counts.get(1)
# # print(n_1)
# # print(n_0)
# survival_rate=n_1/total
# # print(survival_rate)
# p_0="{:.2f}".format(n_0/total)
# # print(p_0)
#
#
# sex_counts=df['Sex'].value_counts()
# male=sex_counts.get('male')
# female=sex_counts.get('female')
# sex_total=len(df['Sex'])
# # print(f"{sex_total} {male} {female} {sex_counts}")
# # print(type(df))
#
# data = {'Category': ['A', 'B', 'A', 'B', 'A'],'Value': [10, 20, 15, 25, 30]}
# df1=pd.DataFrame(data)
# grouped=df1.groupby(by='Category')
# print(grouped)
# res1 = grouped.mean()
# print(res1)
# data = {'First Score': [100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score': [np.nan, 40, 80, 98]}
#
# df = pd.DataFrame(data)
# missing_values = df.isnull()
# print(missing_values)