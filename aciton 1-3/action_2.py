# action2 统计考试成绩相关数据
from typing import List

import pandas as pd

data = {'语文': [68, 95, 98, 90, 80],
        '数学': [65, 76, 86, 88, 90],
        '英语': [30, 98, 88, 77, 90]}
df = pd.DataFrame(data, index=["张飞", "关羽", "刘备", "典韦", "许褚"])
#print("\n————————原始数据表为————————：\n\n{}".format(df))

# 各统计值。因describe()输出的类型较多，且有些不满足要求此处不采用
result=df.drop(index=["张飞", "关羽", "刘备", "典韦", "许褚"])
result.loc['均值'] = df.apply(lambda x: x.mean())
result.loc['最小'] = df.apply(lambda x: x.min())
result.loc['最大'] = df.apply(lambda x: x.max())
result.loc['方差'] = df.apply(lambda x: round(x.var(),1))
result.loc['标准差'] = df.apply(lambda x: round(x.std(),1))
print("\n————————各统计数据表为————————：\n\n{}".format(result))

# 按照总成绩排序
result1=df
result1["总成绩"] = result1.apply(lambda x: x.sum(), axis=1)
result1=result1.sort_values(["总成绩"],ascending=False)
result1["名次"] =[1,2,3,4,5]
print("\n————————排名后的数据表为————————：\n\n{}".format(result1))