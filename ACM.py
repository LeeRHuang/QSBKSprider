import xlwt, json, urllib.request

def getDate():
    page = urllib.request.urlopen("http://contests.acmicpc.info/contests.json")
    return page.read().decode()

def getJson(s):
    j = json.loads(s)
    return j

def writeExcel(header, v):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet1')
    for c in range(len(header)):
        print(c,header[c])
        ws.write(0, c, header[c])
        for r in range(len(v)):
            print(r+1,c, v[r][header[c]])
            ws.write(r+1, c, v[r][header[c]])
    wb.save('Recent contests.xls')

header = ['oj', 'name', 'link', 'start_time', 'week', 'access']
writeExcel(header, getJson(getDate()))