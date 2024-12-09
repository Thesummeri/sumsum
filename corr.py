import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
salary_df=pd.read_csv("/Salary_Data.csv")
x=salary_df["YearsExperience"].values
y=salary_df["Salary"].values
plt.scatter(x,y)
pred_sal=[]
x2=[]
y_intercept=23000
co_ef=10000
for i in range(0,30):
    x2.append(x[i])
    d=co_ef*x[i]
    pred_sal.append(d+y_intercept)
print(x.shape)
print(len(pred_sal))
plt.plot(x,pred_sal)
plt.show()
for i in range(0,30):
    print("actual salary="+str(y[i])+"predicted sal="+str(pred_sal[i])+"diff="+str(y[i]-pred_sal[i]))