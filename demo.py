#coding=utf-8
import re
import os,os.path
import shutil
BOUNDARY = u"==========\n"

#分割函数实现利用关键词进行简单的分割成列表，结果为每一条标注
f = open("source.txt", "r", encoding='utf-8')
content = f.read()  # 读取全部内容
content = content.replace(u'\ufeff', u'') #替换书名前的空格
clips = content.split(BOUNDARY)
print("列表个数：",clips.__len__()) # 获取列表的个数
for i in range(0,4):  #打印出4条标注
    print(clips[i])
sum = clips.__len__()
#print(sum)

# 获取书名存储为列表books，获取除书名外的内容为sentence
both = []  #完整内容。格式为[['',''],['','']……]
books = [] #书名列表
sentence = []
for i in range(0,sum):
    book = clips[i].split("\n-")
    both.append(book)
    print(book)
    if (book!=['']): # 如果书名为空
        books.append(book[0].replace(":","："))
        sentence.append(book[1])
print("both:",both)
print("books:",books)
print("sentence:",sentence)
print('书籍总数：',books.__len__())
print('笔记总数：',sentence.__len__())

# 处理sentence列表的方法函数
def getAddr(s):  #获取标注位置
    return s.split(" | ")[0]
def getTime(s):  #获取添加时间
    g = s.split(" | ")[1]
    return g.split("\n\n")[0]
def getMark(s):  #获取标注内容
    g = s.split(" | ")[1]
    try:
        return g.split("\n\n")[1]
    except IndexError:
        print("list index out of range")

# 去除书名列表中的重复元素
nameOfBooks = list(set(books))
nameOfBooks.sort(key=books.index)
print(nameOfBooks)
print(nameOfBooks.__len__()) # 总共具有的书的种类

# 根据不同书名建立网页文件
print(os.listdir())
if os.path.exists('books'):
    shutil.rmtree('books')
    print('rm books dir succ')
os.mkdir('books') #创建一个books目录，用于存放书名
# print(os.listdir())
os.chdir('books') #更改工作目录
for j in range(0,nameOfBooks.__len__()):
    if (nameOfBooks[j]!='Who Moved My Cheese? (Spencer Johnson)'):
        if (nameOfBooks[j]!='Send to Kindle | 当读书失去动力，你该如何重燃阅读的激情？ (kindle@eub-inc.com)'):
            f=open(nameOfBooks[j]+".html",'w',encoding='utf-8')
            f.write('<!DOCTYPE html>'
                    '<html>'
                    '<meta charset="UTF-8">\n')
            f.write(u"cyang\编码\n")
            s=nameOfBooks[j]
            f.write("<h1>"+s+"</h1>")
            f.close()

# 向文件添加标注内容
print(os.listdir())
file_list = os.listdir(".") #获取当前目录文件名，存放于file_list
for j in range(0,sentence.__len__()):
    temp = both[j]
    if (temp[0]+".html" in file_list ): # 检索字典
        #print("true")
        s1 = getAddr(temp[1])
        s2 = getTime(temp[1])
        s3 = getMark(temp[1]) #获取标注数据
        f=open(temp[0]+".html",'a',encoding='utf-8') #打开对应的文件
        f.write(u'\n')
        f.write("<h3>"+s1+"</h3>")
        f.write("<h3>"+s2+"</h3>")
        # f.write("<h3>" + s3 + "</h3>")  # 写入新的标注数据
        try:
            f.write("<h3>"+s3+"</h3>") #写入新的标注数据
        except:
            f.write("<h3>"+'null'+"</h3>")
        f.write(u'========\n')
        f.write('</html>')
        f.close()
