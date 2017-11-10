#coding=utf-8
import re
import os,os.path
import shutil
import random
import string

BOUNDARY = u"==========\n" #分隔符
intab = "\/:*?\"<>|"
outtab = "  ： ？“《》 "     #用于替换特殊字符
#trantab = maketrans(intab, outtab)

HTML_HEAD = '''<!DOCTYPE html>
<html><meta charset="UTF-8">
<link rel="stylesheet" href="../style/semantic.css">
<script src="http://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.2.min.js"></script>
<script src="../style/semantic.js"></script>
<script src="../style/cyang.js"></script>
<head>
    <title>kindle note</title>
    <style>
        .bannerbox {
            width:100%;
            position:relative;
            overflow:hidden;
            height:1080px;
        }
        .banner {
            width:1960px; /*图片宽度*/
            position:absolute;
            left:50%;
            margin-left:-980px; /*图片宽度的一半*/
        }
    </style>
</head>
'''

HEAD_ELSE = '''
<body>
    <div class="ui fixed inverted menu">
        <a href="../index.html" class="item">Home</a>
        <a href="#" class="item">About</a>
        <a href="http://cyang.tech" target="_blank" class="item">blog</a>
    </div>

    <div class="ui inverted vertical  segment">
        <div class="ui image">
            <!--<img src="images/banner.jpg" alt="" />--> 
        </div>
    </div>

    <!--<div class="ui  vertical basic segment">-->               
'''

END_ELSE = '''
            
        <!--</div>-->
    </body>   
'''

FOOTER_CONTENT = '''
    <footer>
        <div class="ui center aligned inverted segment">                 
            <div class="ui huge labels">
                <a class="ui label" href="http://cyang.tech/aboutme" target="_blank"><i class="user icon"></i>cyang</a>
                <a class="ui label" href="https://github.com/cyang812/kindleNote" target="_blank"><i class="marker icon"></i>kindle note</a>
                <a class="ui label" href="" target="_blank"><i class="mail icon"></i>cy950812@gmail.com</a>
                <a class="ui label" href="http://cyang.tech" target="_blank"><i class="linkify icon"></i>cyang.tech</a>
            </div>
        </div>
    </footer>
</html>
'''

CYANG_KINDLE = '''
<div class="ui cards">
  <div class="card">
    <div class="content">
      <div class="header">kindle note @cyang</div>
      <div class="description">这是一个使用 python 写的 kindle 笔记导出工具。</div>
    </div>
    <div class="ui bottom attached button"><i class="add icon"></i> View GitHub </div>
  </div>
</div>
'''

BOOK_NAME = '''
<div class="ui segment">
    <h1><h1/>
    <h1 class="ui center teal aligned header">BookName</h1>
    <h1><h1/>
</div>

'''

SENTENCE_CONTENT = '''
<div class="ui raised container segment">
   <h1 class="ui header">SENTENCE_TXT</h1>
    <div class="ui horizontal divider">
    </div>
    <a class="ui tag label">SENTENCE_TIME</a>
    <a class="ui tag label">SENTENCE_ADDR</a>
</div>

'''

ABOUT_PAGE = '''
<div class="bannerbox">
    <div class="banner">
        <img src="images/PIC_NAME.png">
    </div>
</div>

<div class="ui divider"></div>
    <h1 class="ui center teal aligned header">共 BOOKS_SUM 本书，SENTENCE_SUM 条笔记</h1>

'''

GRID_BEGIN = '''
    <div class="ui grid">
        <div class="four wide column">
            <div class="ui left image">
                <img src="images/2.png" alt="" />
            </div>
        </div>

        <div class="twelve wide column">
            <div class="ui relaxed divided list">
'''

GRID_END = '''
            </div>
        </div>
    </div>
'''

ITEM_CONTENT = '''
<div class="item">
    <i class="huge book middle aligned grey icon"></i>
    <div class="content">
      <a class="header" href="HTML_URL">HTML_FILE_NAME</a>
      <div class="ui pointing basic orange label"><i class="bookmark icon"></i>SENTENCE_COUNT 条标注</div>
    </div>
</div>
'''

# 替换不能用作文件名的字符
def changechar(s):
    return s.translate(str.maketrans(intab,outtab))

# 处理sentence列表的方法函数
def getAddr(s):  #获取标注位置
    g = s.split(" | ")[0]
    return g
def getTime(s):  #获取添加时间
    g = s.split(" | ")[1]
    return g.split("\n\n")[0]
def getMark(s):  #获取标注内容
    g = s.split(" | ")[1]
    try:
        return g.split("\n\n")[1]
    except IndexError:
        #print("list index out of range due to empty content")
        return "empty content"

# 分割函数实现利用关键词进行简单的分割成列表
# 结果为每一条单独的笔记，包含书名，时间，位置和内容
f = open("source.txt", "r", encoding='utf-8')
content = f.read()  # 读取全部内容
content = content.replace(u'\ufeff', u'') #替换书名前的空格
clips = content.split(BOUNDARY)
print("列表个数：",clips.__len__()) # 获取列表的个数
#for i in range(0,4):  #打印出4条标注
    #print(clips[i])
    #print('---------')
sum = clips.__len__()

# 获取书名存储为列表books，获取除书名外的内容为sentence
both = []  #完整内容。格式为[['',''],['','']……]
books = [] #书名列表
sentence = []  #标注内容
for i in range(0,sum):
    book = clips[i].split("\n-")
    both.append(book)
    #print(book)
    if (book != ['']): # 如果书名非空
        books.append(changechar(book[0])) #添加书名，替换特殊字符，以便创建文件
        sentence.append(book[1])          #添加笔记
#print("both:",both)
#print("books:",books)
#print("sentence:",sentence)
print('笔记总数：',sentence.__len__())

# 去除书名列表中的重复元素
nameOfBooks = list(set(books))
nameOfBooks.sort(key=books.index)
print('书籍总数：',nameOfBooks.__len__())
#print(nameOfBooks)

# 根据不同书名建立网页文件
stceOfBookCnt = {}   # 记录每本书有几条标注的字典
#print(os.listdir())
if os.path.exists('books'):
    shutil.rmtree('books')
    print('rm books dir succ')
os.mkdir('books') #创建一个books目录，用于存放书名网页文件
# print(os.listdir())
os.chdir('books') #更改工作目录
for j in range(0,nameOfBooks.__len__()):
    '''
    # 文件名中含有特殊字符则不成创建成功，包括\/*?<>|字符
    #if (nameOfBooks[j]!='Who Moved My Cheese? (Spencer Johnson)'):
        #if (nameOfBooks[j]!='Send to Kindle | 当读书失去动力，你该如何重燃阅读的激情？ (kindle@eub-inc.com)'):
    '''
    # 网页文件的字符长度不能太长，以免无法在linux下创建
    if nameOfBooks[j].__len__() > 80:
        #print(nameOfBooks[j],"_len:",nameOfBooks[j].__len__())
        #print(nameOfBooks[j][0:90]+".html")
        nameOfBooks[j] = nameOfBooks[j][0:80]  # 截取字符串

    f = open(nameOfBooks[j]+".html",'w',encoding='utf-8') # 创建网页文件
    f.write(HTML_HEAD)   # 写入html头文件
    f.write(HEAD_ELSE)
    #s = nameOfBooks[j]
    f.write(BOOK_NAME.replace('BookName',nameOfBooks[j])) #写入书名
    f.close()
    stceOfBookCnt.__setitem__(nameOfBooks[j],0)  # 清零每本书的标注数量

# 向文件添加标注内容
stce_succ_cnt = 0  # 向html文件添加笔记成功次数
stce_fail_cnt = 0  # 向html文件添加笔记失败次数
#print("html name:",os.listdir())
file_list = os.listdir(".") # 获取当前目录文件名，存放于file_list
for j in range(0,sentence.__len__()):
    temp = both[j]
    filename = changechar(temp[0][0:80])
    if (filename+".html" in file_list ): # 检索字典
        s1 = getAddr(temp[1])  # 获取标注位置
        s2 = getTime(temp[1])  # 获取标注时间
        s3 = getMark(temp[1])  # 获取标注内容
        f = open(filename+".html",'a',encoding='utf-8') # 打开对应的文件
        if (s3 != '\n'):       # 如果文本内容非空
            stce_succ_cnt += 1
            cnt_temp = stceOfBookCnt[filename]
            stceOfBookCnt[filename] = cnt_temp+1
            f.write(SENTENCE_CONTENT.replace("SENTENCE_TXT",s3)
                                    .replace("SENTENCE_TIME",s2)
                                    .replace("SENTENCE_ADDR",s1))
        else:
            stce_fail_cnt += 1
            print("empty txt",stce_fail_cnt,filename)
        f.close()
    else:
        print("can't find filename html :",temp[0]+".html")
print("sentence add succ cnt = ",stce_succ_cnt)
print("sentence add fail cnt = ",stce_fail_cnt)
#print(stceOfBookCnt)

#向文件添加脚标
#print("html name:",os.listdir())
file_list = os.listdir(".") #获取当前目录文件名，存放于file_list
html_count = file_list.__len__()
print("file_list_count",html_count)
for i in range(0,file_list.__len__()):
    '''
    检查文件名是否过长，验证上面的修改是否成功
    '''
    #print(i,file_list[i].__len__())
    #if file_list[i].__len__() > 80:
    #    print(file_list[i],"len:",file_list[i].__len__())

    f = open(file_list[i],'a',encoding='utf-8') #打开对应的文件
    f.write(END_ELSE)
    f.write(FOOTER_CONTENT)
    f.close()

#处理index.html
os.chdir("../")
print("ls dir",os.listdir())
f=open("index.html",'w',encoding='utf-8') #打开对应的文件
f.write(HTML_HEAD.replace("../",""))      #写入html头内容
f.write(HEAD_ELSE.replace("../index.html","#"))
f.write(ABOUT_PAGE.replace("PIC_NAME",random.randint(1,10).__str__())
                    .replace("BOOKS_SUM",str(nameOfBooks.__len__()))
                    .replace("SENTENCE_SUM",str(sentence.__len__())))    #介绍页
f.write(GRID_BEGIN)
for i in range(0,html_count):
    html_url = "books/"+file_list[i]
    html_name = file_list[i].replace(".html",'')
    f.write(ITEM_CONTENT.replace("HTML_URL",html_url)
                        .replace("HTML_FILE_NAME",html_name)
                        .replace("SENTENCE_COUNT",str(stceOfBookCnt[html_name]))) # 写入本书标注数量
f.write(GRID_END)
f.write(END_ELSE)
f.write(FOOTER_CONTENT)
f.close()


