import pandas as pd
import numpy as np
from datetime import datetime
from persiantools.jdatetime import JalaliDate
import matplotlib.pyplot as plt
from collections import Counter


#read data
dataset = pd.read_csv("tarikhche kharid.csv",usecols=["id","selling_price","created_at"])
dataset["date"] = dataset["created_at"]
dataset.drop(["created_at"],axis=1,inplace=True)
def date(a):
    dt = datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
    dt = dt.date()
    return dt
#remove hour from date column
dataset["date"] = dataset["date"].apply(date)
#get first data day of week
firstdate = dataset["date"].iloc[0]
firstdate = firstdate.weekday()


print("لطفا رقم مطلوب برای خرید را وارد کنید")
a= input()
a = int(a)

print("لطفا تاریخ مطلوب برای خرید را وارد کنید")
b = input()
b = datetime.strptime(b, '%Y-%m-%d')
b = b.weekday()
#getting id of product,witch are having same pricevalues as inputed
id = []
for row in dataset.index :
    x = int(dataset["selling_price"].iloc[row] )
    if (x <= (a+500))   and  (x >= (a-500)):
        if (dataset["date"].iloc[row]).weekday() == b:
            id.append(dataset["id"].iloc[row])


print(id)


def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


print(most_frequent(id))


plt.hist(id)
plt.show()

