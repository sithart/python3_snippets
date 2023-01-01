import pandas as pd
import warnings
# from natsort import index_natsorted, order_by_index
warnings.simplefilter("ignore")

df = pd.read_excel(r"C:\Users\sitha\Projects\refactoring\python3_snippets\data\Aug - 2021 Master Data (1).xlsx")
# print(df.columns)
num_vars = df.columns[df.dtypes != object]
print("num_vars", num_vars[:15])


df_1 = df['TestSampleNo'].isnull().sum().sort()
print("ans", df_1)

"""num_vars = df.columns[df.dtypes != object]
print("num_vars", num_vars)

cat_vars = df.columns[df.dtypes == object]
print("cat_vars", cat_vars)

hai = num_vars.isnull().sum()
hoi = cat_vars['TestSampleNo'].isnull().sum()
print("hai", hoi)
"""

#df = df.reindex(index=order_by_index(df.index, index_natsorted(df['TestSampleNo'], reverse=False)))
"""df = df['TestSampleNo'].isnull().sum().sort()
print("ans", df)"""
# datafra = df['TestSampleNo']#.fillna(0).str.strip()
# df_ = list(datafra)
# for val in df_:
#     #val = val
#     print("val", val)
"""df1=df['TestSampleNo'].sort_values(by='TestSampleNo')
ans = list(df1)
print("df1", ans)

"""



"""    need = val.split("CVD")[1]

    df1 = need.reindex(index=order_by_index(need.index, index_natsorted(need[, reverse=True)))
print (df)


    #nee = int(need)
    #order = nee.sort_values( by = "TestSampleNo", ascending=True)
    #conv = val.astype("str")
#for x in datafra.str.split("CVD", 0)[1]:
#need = df['TestSampleNo'].astype("str")
#for i in need:
    #if "CVD" in need:
    print("need", type(need))"""
