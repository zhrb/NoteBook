def readFileAndCreateDict(filename):
    areaDict = {}
    with open(filename, 'r') as f: #'r'以只读方式打开文件，f代表打开文件后的对象
        f.readline()                #第一行是标题直接跳过
        for line in f:              #对文件中的每一行
            xlist = line.strip().split(",")
            areaDict[xlist[0]] = xlist[1:]
    return areaDict

def showInfo(x):#x为一个列表里面包含行政区划其他信息
    t = ["简称", "等级", "区号", "邮编", "全称", "精度", "纬度", "拼音" ]
    info = "{}:{}\n{}:{}\n{}:{}\n{}:{}\n{}:{}\n{}:{}\n{}:{}".\
        format(t[0],x[0],t[1],x[1],t[2],x[2],t[3],x[3],t[4],x[4],t[5],x[5],t[6],x[6],t[7],x[7])
    print(info)
    
def menu():
    return input("1. 查询\n2. 退出\n请输入:")

if __name__ == "__main__":
    fileName = "行政区划数据库.csv"
    areaDict = readFileAndCreateDict(fileName)
    print("读取数据库完毕")
    while True:
        choice = menu()
        if choice == "1": #输入1查询，其他退出
            name = input("请输入要查询的区域:")
            result = areaDict.get(name)
            if result == None:
                print("查无此区域")
            else:
                showInfo(result)
        else:
            break        