import urllib.request
import re
import xlwt


yzdata ={}
yzdata['校长'] = ['国泰君安证券股份有限公司成都北一环路证券营业部','华泰证券股份有限公司成都南一环路第二证券营业部']
yzdata['金田路'] = ['光大证券股份有限公司深圳金田路证券营业部']
yzdata['赵老哥'] = ['中国银河证券股份有限公司绍兴证券营业部','浙商证券股份有限公司绍兴解放北路证券营业部','华泰证券股份有限公司浙江分公司','中信证券股份有限公司上海古北路证券营业部','中国银河证券股份有限公司北京阜成路证券营业部']
yzdata['佛山系'] = ['光大证券股份有限公司佛山季华六路证券营业部','光大证券股份有限公司佛山绿景路证券营业部','海通证券股份有限公司广州珠江西路证券营业部']
yzdata['炒股养家'] = ['华鑫证券有限责任公司上海淞滨路证券营业部','	华鑫证券有限责任公司上海宛平南路证券营业部','华鑫证券有限责任公司宁波沧海路证券营业部']
yzdata['荣超'] = ['华泰证券股份有限公司深圳益田路荣超商务中心证券营业部']
yzdata['机构'] = ['机构专用']
yzdata['欢乐海岸'] = ['中泰证券股份有限公司深圳欢乐海岸证券营业部']
yzdata['章建平'] = ['中信证券股份有限公司杭州四季路证券营业部','东方证券股份有限公司杭州龙井路证券营业部','国泰君安证券股份有限公司上海江苏路证券营业部','方正证券股份有限公司杭州保俶路证券营业部']
yzdata['孙哥'] = ['中信证券股份有限公司上海溧阳路证券营业部','光大证券股份有限公司杭州庆春路证券营业部']
yzdata['玉米'] = ['招商证券股份有限公司深圳蛇口工业七路证券营业部']
yzdata['小鳄鱼'] = ['中国中投证券有限责任公司南京太平南路证券营业部']
yzdata['著名刺客'] = ['海通证券股份有限公司北京阜外大街证券营业部']
yzdata['作手新一'] = ['国泰君安证券股份有限公司南京太平南路证券营业部']
yzdata['秘书长'] = ['中信建投证券股份有限公司重庆涪陵广场路证券营业部']
yzdata['财通绍兴'] = ['财通证券股份有限公司绍兴人民中路证券营业部']
yzdata['泥爷'] = ['大同证券有限责任公司晋中迎宾西街证券营业部']
yzdata['秘书长'] = ['中信建投证券股份有限公司重庆涪陵广场路证券营业部']
yzdata['研报席位'] = ['申万宏源证券有限公司上海闵行区东川路证券营业部','东方证券股份有限公司上海浦东新区银城中路证券营业部','海通证券股份有限公司上海共和新路证券营业部']
yzdata['进化论'] = ['华鑫证券有限责任公司常州晋陵中路证券营业部','国泰君安证券股份有限公司深圳蔡屋围金华街证券营业部']
yzdata['泥爷'] = ['大同证券有限责任公司晋中迎宾西街证券营业部']
yzdata['泥爷'] = ['大同证券有限责任公司晋中迎宾西街证券营业部']








style = xlwt.XFStyle()
fnt = xlwt.Font()
fnt.name = u'微软雅黑'
fnt.colour_index = 2
fnt.bold = False
style.font = fnt  


data = urllib.request.urlopen('http://data.eastmoney.com/stock/lhb.html').read().decode('utf-8','ignore')
yybdata = xlwt.Workbook()
table = yybdata.add_sheet('1.5',cell_overwrite_ok=True)
pat = 'data_code="(.*?)"'

allurl = re.compile(pat).findall(data)  #股票代码
for i in range(0,len(allurl)):
    try:
        print('第'+str(i+1)+'次爬取') 
        stockurl = 'http://data.eastmoney.com/stock/lhb/'+allurl[i]+'.html'  #成交明细url
        data = urllib.request.urlopen(stockurl).read().decode('gb2312','ignore')
        namepat = 'title="(.*?)" class="tit-a"'
        stockname = re.compile(namepat,re.S).findall(data)
        table.write(i,10,stockname[0])  #写入股票代码
        for j in range(5):
            yybpat = '买入金额最大的前5名.*?<td>'+str(j+1)+'</td>.*?.html">(.*?)</a></a>.*?卖出金额最大的前5名'
            yyblist = re.compile(yybpat,re.S).findall(data)
            if yyblist != []:                
                for key in yzdata:
                    if yyblist[0] in yzdata[key]:     
                        table.write(i,j,key,style) #写入营业部
#                    else:
#                        table.write(i,j,yyblist[0]) #写入营业部
#            else:
#                table.write(i,j,'no data') #写入营业部

                
            yybpat = '卖出金额最大的前5名.*?<td>'+str(j+1)+'</td>.*?.html">(.*?)</a></a>'
            yyblist = re.compile(yybpat,re.S).findall(data)
            if yyblist != []:                
                for key in yzdata:
                    if yyblist[0] in yzdata[key]: 
                        table.write(i,j+5,key,style) #写入营业部                        
#                    else:
#                        table.write(i,j+5,yyblist[0]) #写入营业部
#            else:
#                table.write(i,j+5,'no data') #写入营业部
                        


    except urllib.error.URLError as e:
        if hasattr(e,'code'):   
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason) 
yybdata.save('E:\yybdata.xls')
