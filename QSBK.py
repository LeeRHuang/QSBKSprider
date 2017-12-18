from bs4 import BeautifulSoup
import requests
import string


def genderCompare(gener):
    man = '男'
    woman = '女'
    if 'womenIcon' in gener:
        return woman
    else:
        return man

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
url = 'https://www.qiushibaike.com/'

print('开始爬取--------')
wb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')

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
    print('头像：', 'http:' + img, '昵称：', title, '年龄：', ageCount, '性别：', genderName, '\n', '内容：', contentValue,
              voteValue, commentValue)
