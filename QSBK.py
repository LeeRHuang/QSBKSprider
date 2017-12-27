# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import codecs
import xlwt
import time

'''格式化取从page 1到13的地址，为分页准备，{}是格式化需要填充的字符串值，format()是字符串格式化,str(i)将整形转成字符型,range(1,14,1)三个参数意义:第一个1是指定开始的索引
第二个14是截止到的索引位置，不包含该索引值，第三个1表示间隔的值，综合表达意思是取1-13，间隔值为1
'''
urls = ['https://www.qiushibaike.com/8hr/page/{}/'.format(str(i)) for i in range(1,14,1)]

'''
声明一个接受数据数组
'''
dataArr = []

'''配置请求头'''
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

'''判断性别'''
def genderCompare(gener):
    man = '男'
    woman = '女'
    if 'womenIcon' in gener:
        return woman
    else:
        return man


def loadData(url):
    '''
    请求数据
    :return: soup对象
    '''
    print('开始爬取: ',url)
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    return soup


def handleSoupData(soup):
    '''
    处理返回数据
    :param soup:
    :return:
    '''
    # users = soup.select('div.author.clearfix > a > img') #获取div 标签，class为author clearfix下所有 a 标签下的 img 标签
    users = soup.select('div.author.clearfix img')  # 获取div 标签，class为author clearfix下所有img的标签和上面效果一样
    ages = soup.select('div.author.clearfix > div')
    contents = soup.select('a.contentHerf > div > span')
    votes = soup.select('div.stats > span.stats-vote > i.number')
    comments = soup.select('div.stats > span.stats-comments > a')

    for user, age, content, vote, comment in zip(users, ages, contents, votes, comments):
        img = user.get('src')  # 获取img下src属性的值
        title = user.get('alt')
        ageCount = age.get_text()
        gender = age.get('class')
        genderName = genderCompare(gender)
        voteValue = vote.get_text()
        contentValue = content.get_text()  # 获取标签中的文本
        commentValue = comment.get_text()
        print('头像：','http:' + img,'\n','昵称：',title,'\n','年龄：',ageCount,'\n','性别：',genderName,'\n','内容：',contentValue,'\n',
              voteValue,'好笑','\n',commentValue)
        text = '头像：'+format('https:' + img)+'\n'+'昵称：'+title+'\n'+'年龄：'+ageCount+'\n'+'性别：'+genderName+'\n'+\
               '内容：'+contentValue+'\n'+voteValue+'好笑'+'\n'+commentValue
        cacheData(text) #缓存到txt文件中

        #组装字典
        dic = {
            u'昵称': title,
            u'头像': format('https:' + img),
            u'年龄': ageCount,
            u'性别': genderName,
            u'内容': contentValue,
            u'好笑': voteValue,
            u'评论': commentValue
        }
        dataArr.append(dic)


def cacheData(text):
    '''
    1.使用 with 避免文件写入句柄还没有关闭又写入
    2.使用 codecs 帮助读取文件时候自动转码
    3.指定编码方式，ASCII(American standard Code Information Interchange)是英文和其他字符的编码方式；GBK 汉字编码方式；
    UTF-8 是 UniCode 编码方式的一种实现，好比英语是国际通用语言
    4.使用 a 这种 model 模式，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    :param text:
    :return:
    '''
    with codecs.open('data.txt','a',encoding='utf-8') as f:
        f.write(text+'-----------------------------------------------------------'+'\n')


def saveContent(arr):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('QSBK Sheet')
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style = xlwt.XFStyle()  # 居中
    style.alignment = alignment

    '''
    声明表头
    '''
    titles = [u'昵称', u'头像', u'年龄', u'性别', u'内容', u'好笑', u'评论']

    '''
    循环遍历
    '''
    for c in range(len(titles)):
        title = titles[c]
        worksheet.write(0, c, title, style)
        for r in range(len(arr)):
            worksheet.write(r+1,c,arr[r][titles[c]])

    workbook.save('QSBK.xls')



if __name__ == '__main__':

    ''''主程序入口'''
    # soup = loadData('https://www.qiushibaike.com/8hr/page/1/')
    # handleSoupData(soup)

    for url in urls:
        time.sleep(2)
        soup = loadData(url)
        handleSoupData(soup)

    saveContent(dataArr)
    print('爬完啦，打开 excle 看看吧')