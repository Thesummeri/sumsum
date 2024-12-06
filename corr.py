import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
salary_df=pd.read_csv("(C:/Users/Kethan V/Downloads/Salary_Data.csv)/salary_data.csv")
x=salary_df["years experience"].values
y=salary_df["salary"].values
plt.scatter(x,y)
pred_sal=[]
x=[]
y_intercept=23000
co_ef=1000
x=x.reshape(-1,1)
y=y.reshape(-1,1)
for i in range(1,30):
    x.append(x[i])
    d=co_ef * x[i]
    pred_sal.append(d+y_intercept)
print(x.shape)
print(len(pred_sal))
plt.plot(x,pred_sal)
plt.show()
for i in range(1,30):
    print("actual salary="+str(y[i])+"predicted sal="+str(pred_sal[i])+"diff="+str(y[i]-pred_sal[i]))
