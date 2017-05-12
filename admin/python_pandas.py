# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
# matplotlib.use('Agg')
import matplotlib
from pylab import  *
from io import StringIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

datas = pd.read_csv('jobInfo.csv')
print(datas)
# datas = datas.drop('companyLogo',axis = 1)#删除无关项
# datas = datas.replace(['1-3','3-5'],['1-3年','3-5年'])##处理时间数据
# datas = datas[datas['jobNature']=='实习']#排除兼职和实习影响
#
# ###实习招聘 第一部分
# #全国实习招聘情况按城市排名
def practical_city():
    plt.figure(figsize=(5, 6))
    city = datas.groupby('city').size()
    city.sort(inplace=True)
    #city.ix[:10].plot(kind = 'bar')
    city.plot(kind='bar')
    plt.title('全国实习招聘情况按城市排名')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/practical_city.png')



#全国实习招聘情况按职位领域排名
def practical_poistion():
    plt.figure(figsize=(5, 6))
    kk = datas.groupby('positionType').size()
    kk.sort(ascending = False)
    #print(kk)
    k1 = kk/len(datas)
    for i in range(5):
        print(k1.ix[:5*i].sum())
    kk.plot(kind = 'bar')
    plt.title('全国实习招聘情况按职位领域排名')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/practical_poistion.png')


#
###全国招聘情况 第二部分
#全国招聘情况按工作经验排名
def global_experience():
    plt.figure(figsize=(5, 6))
    work_year = datas.groupby('workYear').size()##7项
    work_year.sort(ascending = False)
    work_year.plot(kind='bar')
    plt.title('全国招聘情况按工作经验排名')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/global_experience.png')


#全国招聘情况按学历要求排名
def global_education():
    plt.figure(figsize=(5, 6))
    education = datas.groupby('education').size()
    education.sort(ascending = False)
    education.plot(kind='bar')##如果是横的柱状图，则排序为True
    plt.title('全国招聘情况按学历要求排名')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/global_education.png')



#招聘公司类型统计
def company_size():
    plt.figure(figsize=(5, 6))
    kk = datas.groupby('companySize').size()
    kk.sort()
    kk.plot(kind = 'barh')
    plt.title('公司人数大小')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/company_size.png')



def company_financeStage():
    plt.figure(figsize=(5, 6))
    kk = datas.groupby('financeStage').size()
    kk.sort()
    kk.plot(kind = 'barh')
    plt.title('招聘公司上市类型')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/company_financeStage.png')


def company_positiontype():
    plt.figure(figsize=(5, 6))
    kk = datas.groupby('positionType').size()
    kk.sort()
    kk.plot(kind = 'barh')
    plt.title('招聘职位统计')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/company_positiontype.png')

#
#
# ###城市 第三部分
cities = datas[datas['city'].isin(['北京','上海','广州','深圳','杭州','成都','武汉','南京','郑州','长沙'])]
print(cities)
### 不同城市薪酬
def city_salary():
    plt.figure()
    city1 = cities.pivot_table(['salaryMin','salaryMax'],index='city')
    city1 = city1.sort_values(by='salaryMin')
    city1.plot(kind='bar',figsize=(5, 6))
    plt.title('工作需求最多的十大城市平均薪资')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/city_salary.png')

#
# ###城市对学历人数及薪酬
# #不同城市对不同学历要求招聘人数
xl = cities[cities['education'].isin(['本科','大专','学历不限','硕士'])]
def city_education_num():
    plt.figure()
    xl1 = xl.pivot_table('salaryMax',index='education',columns='city',aggfunc=len)
    xl1.T.plot(kind='bar',stacked = True,figsize=(5, 6))
    plt.title('不同城市对不同学历要求招聘人数')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/city_education_num.png')



#不同城市招聘针对不同学历平均薪酬
def city_education_salary():
    plt.figure()
    xl2 = xl.pivot_table('salaryMax',index='education',columns='city')
    xl2.T. plot(kind='bar',figsize=(5, 6))
    plt.title('不同城市招聘针对不同学历平均薪酬')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/city_education_salary.png')


#不同城市针对不同工作经验招聘人数
def city_experience_num():
    plt.figure()
    jy = cities[cities['workYear'].isin(['1-3年','3-5年','5-10年','不限','应届毕业生'])]
    jy1 = jy.pivot_table('salaryMin',index='workYear',columns='city',aggfunc=len)
    jy1.T.plot(kind='bar',stacked= True,figsize=(5, 6))
    plt.title('不同城市针对不同工作经验招聘人数')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/city_experience_num.png')
city_experience_num()
# #不同城市招聘针对不同工作经验平均薪酬
def city_experience_salary():
    plt.figure()
    jy = cities[cities['workYear'].isin(['1-3年','3-5年','5-10年','不限','应届毕业生'])]
    jy2 = jy.pivot_table('salaryMin',index='workYear',columns='city')
    jy2.T.plot(kind='bar',figsize=(5, 6))
    plt.title('不同城市招聘针对不同工作经验平均薪酬')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/city_experience_salary.png')

##前十职位薪酬，这里主要是按照薪酬来计算，调用的是全国数据，而非前十城市数据
###或者可以再加一段不同城市不同职位的薪酬

rec = datas.groupby('positionType').size()#只考虑全职
rec.sort(ascending=False)
#rec.sort_values(inplace=True)
rec=list(rec.index[:10])

def hotjob_salary():
    plt.figure()
    pt = datas[datas['positionType'].isin(rec)]
    pt1 = pt.pivot_table(['salaryMin','salaryMax'],index='positionType')
    pt1 = pt1.sort_values(by='salaryMin')
    pt1.plot(kind='bar',figsize=(5, 6))
    plt.title('热门职位领域薪资水平')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/hotjob_salary.png')


##
def hotjob_hotsalary_fivecity():
    pt = datas[datas['positionType'].isin(rec)]
    pt_city = pt[pt['city'].isin(['北京','深圳','广州','上海','杭州'])]
    plt.figure()
    pc1 = pt_city.pivot_table('salaryMin',index='positionType', columns='city')
    pc1.plot(kind='bar',figsize=(5, 6))
    plt.title('热门领域在五大城市薪酬水平')
    plt.savefig('C:/Users/xsh/PycharmProjects/web_app/static/img_pandas/hotjob_hotsalary_fivecity.png')


practical_city()
practical_poistion()
global_education()
global_experience()
company_financeStage()
company_positiontype()
company_size()
city_experience_salary()
city_education_num()
city_salary()
city_education_salary()
city_experience_num()
hotjob_hotsalary_fivecity()
hotjob_salary()
#



'''
education_ratio = education/len(datas)
education_ratio.to_csv('education_ratio.csv')
print(education_ratio)


companySize = datas.groupby('companySize').size()
companySize.sort()
companySize.plot(kind = 'barh')
plt.show()

companySize_ratio = companySize/len(datas)
companySize_ratio.to_csv('companySize_ratio.csv')
'''

# city_ratio = city/len(datas)
# print(city_ratio.ix[0])
# city5 = city_ratio.ix[:5].sum()
# city10 = city_ratio.ix[:10].sum()
# print(city5, city10)

'''
work_year_ratio = work_year/len(datas)
work_year_ratio.to_csv('work_year_ratio.csv')
print(work_year_ratio)
'''

