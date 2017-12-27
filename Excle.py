#coding=utf-8

import xlwt
import datetime

# workbook = xlwt.Workbook(encoding = 'ascii')
# worksheet = workbook.add_sheet('My Worksheet')
# # # style = xlwt.XFStyle() # 初始化样式
# # # font = xlwt.Font() # 为样式创建字体
# # # font.name = 'Times New Roman'
# # # font.bold = True # 黑体
# # # font.underline = True # 下划线
# # # font.italic = True # 斜体字
# # # style.font = font # 设定样式
# worksheet.write(0, 0, 'Unformatted value') # 不带样式的写入
#
# worksheet.write(1, 0, 'Formatted value', style) # 带样式的写入
#
# workbook.save('formatting.xls') # 保存文件

# 头像：http://pic.qiushibaike.com/system/avtnew/3009/30097823/thumb/20171208223138.JPEG?imageView2/1/w/90/h/90
# 昵称：敏儿卟哭
# 年龄：26
# 性别：女
# 内容：
#
#
# 今天上午快下班的时候，我们老大（男）说“小敏给你发个东西，给我打印出来。”我怀着快下班愉快的心情打开微信。尼玛，发了一张男厕所一坨屎没冲的照片给我让我打印。要宣导素质，（不过有些人真的没素质）。打完以后给我们办公室的人都看看，结果一个个都一副要吐的表情。我说“你们看的都是黑白版的。我看的还是彩色版的呢？”我们老大：“你看的彩色版算什么。我看的现场版的说什么了吗？”然后就在讨论怎么找嫌疑人。讨论了好久，都每个所以然，我都听不下去了。我说要不验DNA吧！[挖鼻孔][挖鼻孔][挖鼻孔]
#
#
# 479好笑
#
# 7 评论



def style():
    workbook = xlwt.Workbook(encoding='ascii')
    wokesheet = workbook.add_sheet('QSBK Worksheet')
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.bold = True
    font.underline = True
    style.font = font
    style.num_format_str = 'MM/DD/YYYY'
    wokesheet.col(0).width = 10000
    wokesheet.write(0,1,'今天上午快下班的时候，我们老大（男）说“小敏给你发个东西，给我打印出来。”我怀着快下班愉快的心情打开微信。尼玛，发了一张男厕所一坨屎没冲的照片给我让我打印。要宣导素质，（不过有些人真的没素质）。打完以后给我们办公室的人都看看，结果一个个都一副要吐的表情。我说“你们看的都是黑白版的。我看的还是彩色版的呢？”我们老大：“你看的彩色版算什么。我看的现场版的说什么了吗？”然后就在讨论怎么找嫌疑人。讨论了好久，都每个所以然，我都听不下去了。我说要不验DNA吧！[挖鼻孔][挖鼻孔][挖鼻孔]',style)
    wokesheet.write(0,0,datetime.datetime.now(),style)
    workbook.save('style.xls')


def caculate():
    workbook = xlwt.Workbook(encoding='ascii')
    wokesheet = workbook.add_sheet('QSBK Worksheet')
    wokesheet.write(0, 0, 5) # Outputs 5
    wokesheet.write(0, 1, 2) # Outputs 2
    wokesheet.write(1, 0, xlwt.Formula('A1*B1')) # Should output "10" (A1[5] * A2[2])
    wokesheet.write(1, 1, xlwt.Formula('SUM(A1,B1)')) # Should output "7" (A1[5] + A2[2])
    workbook.save('caculate.xls')


def link():
    workbook = xlwt.Workbook(encoding='ascii')
    wokeSheet = workbook.add_sheet('QSBK Worksheet')
    wokeSheet.write(1,1,xlwt.Formula('HYPERLINK("http://www.baidu.com";"Baidu")'))
    workbook.save('link.xls')

def merge():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Merge Sheet')
    worksheet.write_merge(0, 0, 0, 3, 'First Merge')
    font = xlwt.Font()
    font.bold = True
    style = xlwt.XFStyle()
    style.font = font
    worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style)
    workbook.save('Merge.xls')
    # workbook = xlwt.Workbook()
    # worksheet = workbook.add_sheet('QSBK Sheet')
    # worksheet.write_merge(0, 0, 0, 3, 'First Merge')  # Merges row 0's columns 0 through 3.
    # font = xlwt.Font()  # Create Font
    # font.bold = True  # Set font to Bold
    # style = xlwt.XFStyle()  # Create Style
    # style.font = font  # Add Bold Font to Style
    # worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style)  # Merges row 1 through 2's columns 0 through 3.
    # workbook.save('merge.xls')


def alignment():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('My Sheet')
    worksheet.col(0).width = 10000
    worksheet.col(0).height = 2000
    alignment = xlwt.Alignment()  # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER  # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    style = xlwt.XFStyle()  # Create Style
    style.alignment = alignment  # Add Alignment to Style
    worksheet.write(0, 0, 'Cell Contents', style)
    workbook.save('Excel_Workbook.xls')

def border():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('My Sheet')
    borders = xlwt.Borders()  # Create Borders
    borders.left = xlwt.Borders.DASHED
    # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
    borders.right = xlwt.Borders.DASHED
    borders.top = xlwt.Borders.DASHED
    borders.bottom = xlwt.Borders.DASHED
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40
    style = xlwt.XFStyle()  # Create Style
    style.borders = borders  # Add Borders to Style
    worksheet.write(0, 0, 'Cell Contents', style)
    workbook.save('Excel_Workbook.xls')


def background():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('My Sheet')
    pattern = xlwt.Pattern()  # Create the Pattern
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = 5  # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
    style = xlwt.XFStyle()  # Create the Pattern
    style.pattern = pattern  # Add Pattern to Style
    worksheet.write(0, 0, 'Cell Contents', style)
    workbook.save('Excel_Workbook.xls')


style()
caculate()
link()
merge()
alignment()
border()
background()