import numpy
#a=numpy.zeros((3,4))
#b=[3,6,7,4,8,3,7,3,7]
#a = [(1,3,4,5),(2,6,8,5),(4,8,6,9)] 

import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt


x=[]
y=[]
for year in range(2013,2019):
    for m in range(1,13):
        mstr=str(m).zfill(2)
        ymstr=str(year)+'-'+str(mstr)
        if ymstr == '2018-02':
            break
            
    
        df= ts.month_boxoffice(ymstr)
        sum = 0
        for i in range(11):
            sum+=int(df['boxoffice'][i])
        x.append(ymstr)
        y.append(sum)

x2=range(len(x))        
plt.plot(x2,y)  #plot(x轴数据，y轴数据，展现形式)   
plt.xticks(x2,x,rotation = 45)
#plt.figure(figsize=(40,5)) 
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.show()

