import urllib.request
import re
import pymysql

testpat='详细仓位'
pat1='000983'#西山煤电
pat2='600970'
pat3='600050'
breakpat='验证码'

db = pymysql.connect(host='localhost', user='root', passwd='', db='myproject',charset='utf8')
cursor = db.cursor()

headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener) 


#程老师1266614
#威廉 973000,975000
for i in range(1266884,1,-1):
    print('第'+str(i)+'次尝试') 
    url = 'https://xueqiu.com/P/ZH'+str(i)   
    try:
        data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
        testdata=re.compile(testpat).findall(data)
        data1=re.compile(pat1).findall(data)
        data2=re.compile(pat2).findall(data)
        data3=re.compile(pat3).findall(data)
        breakdata=re.compile(breakpat).findall(data)
        if breakdata != []:
            print('ip被禁啦')
            break
        if testdata ==[]:
            print('未能爬取组合页面')
            break
#        if data1 != [] and data2 != [] and data3 != []:
        if data1 != [] :
            
            print('找到啦!')
#        if testdata != []:
            sql="insert into snowball values('"+str(i)+"')"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
    except Exception as e:
        print(e)
        
db.close()
    
