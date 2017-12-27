# 介绍
使用 python3.6 爬取糗事百科数据，将爬取的数据解析、写入文件、导入 Excle 中

# 使用
1. 由于使用 python3.6 版本，而 Mac 系统自带版本目前是 2.x 版本，推荐使用 Homebrew 方式安装，第一次接触 python 童鞋可以 Goggle之 [python3.6安装](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000)
2. python3.6 环境自带了 *pip* 包管理工具，安装完环境后，可以在终端 cd 到项目目录下，执行 `pip3 install BeautifulSoup`  `pip3 install requests`  `pip3 install BeautifulSoup`  `pip3 install codecs`  `pip3 install xlwt`  安装这些依赖的第三方库
3. 安装完三方库之后，在当前项目目录下，执行 `python3 QSBKSprider.py`

# 目标
- 增强对 Excle 表格数据处理
- 提取计算出一些数据出现的频率，形成云图
- 多线程爬取，定时启动爬虫

