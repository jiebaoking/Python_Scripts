#水木网际识别
import tushare as ts

text='''B 600398 11.94 11000 
B 603895 43.91 1200 
B 600789 10.71 5000 
B 002146 13.21 4000 
B 600426 18.47 2900 
S 603676 17.18 4900 
S 600188 18.89 4200 
S 603103 30.76 3200 '''

t=text.split('\n')

for i in range(len(t)):
    tprint=''
    t2=t[i].split(' ')
    t2.remove('')
    if len(t2)==4:
        tprint+='买入' if t2[0]== 'B' else '卖出'
        df = ts.get_realtime_quotes(t2[1])
        tprint+=df['name'][0]
        tprint+=str(int(float(t2[2])*float(t2[3])))
        tprint+='元 价格'+t2[2]
        print(tprint)
        
    if len(t2)==5:
        tprint+='买入' if t2[0]== 'B' else '卖出'
        tprint+=t2[2]
        tprint+=str(int(float(t2[3])*float(t2[4])))
        tprint+='元 价格'+t2[3]
        print(tprint)
        
        
        
        