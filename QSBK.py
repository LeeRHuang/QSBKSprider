from bs4 import BeautifulSoup
import requests
import string
import time

'''格式化取从page 1到13的地址，为分页准备，{}是格式化需要填充的字符串值，format()是字符串格式化,str(i)将整形转成字符型,range(1,14,1)三个参数意义:第一个1是指定开始的索引
第二个14是截止到的索引位置，不包含该索引值，第三个1表示间隔的值，综合表达意思是取1-13，间隔值为1
'''
urls = ['https://www.qiushibaike.com/8hr/page/{}/'.format(str(i)) for i in range(1,14,1)]

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
    contents = soup.select('a > div > span')
    voteValue = soup.select('div.stats > span.stats-vote')[0].get_text()
    votes = soup.select('div.stats > span.stats-vote > i.number')
    comments = soup.select('div.stats > span.stats-comments > a')

    for user, age, content, vote, comment in zip(users, ages, contents, votes, comments):
        img = user.get('src')  # 获取img下src属性的值
        title = user.get('alt')
        ageCount = age.get_text()
        gender = age.get('class')
        genderName = genderCompare(gender)
        contentValue = content.get_text()  # 获取标签中的文本
        commentValue = comment.get_text()
        print('头像：','http:' + img,'\n','昵称：',title,'\n','年龄：',ageCount,'\n','性别：',genderName,'\n','内容：',contentValue,
              voteValue,'\n',commentValue)



if __name__ == '__main__':

    ''''主程序入口'''
    for url in urls:
        time.sleep(2)
        soup = loadData(url)
        handleSoupData(soup)
