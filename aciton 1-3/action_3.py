# action3 统计车型投诉相关数据

import pandas as pd

# 读入csv文件，创建dataframe
df=pd.read_csv("car_complain.csv")

# 数据清洗，防止重复统计
def f(x):
    x=x.replace("一汽-大众","一汽大众")
    return x
df["brand"]=df["brand"].apply(f)

# 对某列使用某分隔符进行ont-hot转换，输出多列，使用：Series.str.get_dummies([sep])
df=df.drop(columns="problem").join(df['problem'].str.get_dummies(","))

# 按照brand分组，统计各个品牌的投诉总数。然后按照count降序排列，并重置索引。
result1 = df.groupby(["brand"])["id"].agg(["count"])
result1 = result1.sort_values("count",ascending=False).reset_index()
print("\n------第1问：品牌的投诉总数排名-------：\n{}".format(result1))

# 按照car_model分组，统计各个车型的投诉总数。然后按照count降序排列，并重置索引。
result2=df.groupby(["car_model"])["id"].agg(["count"])
result2 = result2.sort_values("count",ascending=False).reset_index()
print("\n-------第2问：车型的投诉总数排名-------：\n{}".format(result2))

# 按照(brand，carmodel)分组，统计各品牌下各车型的投诉总数。然后按照"brand"再分组，对count求平均，降序排列，并重置索引。
result3=df.groupby(["brand","car_model"])["id"].agg(["count"])
result3=result3.groupby(["brand"])["count"].agg(["mean"])
result3=result3.sort_values("mean",ascending=False).reset_index()
print("\n------第3问：各品牌下平均车型投诉数排名------：\n  平均投诉最多的品牌是：{}\n\n{}".format(result3["brand"][0],result3))