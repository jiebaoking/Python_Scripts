import tushare as ts
import xlrd

#策略：每日开盘买入银华日利，收盘前卖出，如果逆回购利率高，选择一日逆回购，否则进入天天宝

#一日逆回购GC001，手续费0.001% 当逆回购利率大于4.745时选择逆回购
#券商货基使用每万元1.2，约年化4.4% 无手续费
#国金比较好

file='D:\\PythonStudy\\gc001.xls'
data=ts.get_hist_data('511880')


workbook=xlrd.open_workbook(file)
#sheet_names=workbook.sheet_names()

sheet0 = workbook.sheet_by_name('Sheet0')
cols = sheet0.col_values(1)[4:254]
#date = sheet0.col_values(0)
cols2=cols.copy()

for i in range(250):
    if cols[i]<=4.745:
        cols2.remove(cols[i])

#银华日利部分
rate=data.apply(lambda x:x[2]/x[0],axis=1)
r=1
for i in range(250):
    r*=rate[i]
    

#逆回购部分
for i in range(len(cols2)):
    r*=cols2[i]/36500-0.00001+1
    
#券商天天宝部分
r*=1.00012**(365-len(cols2))
print(r)