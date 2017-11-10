## 项目说明

这是一个使用 python 语言编写的项目，用于将 kindle 笔记导出为网页文件。

## 使用说明
- 1、从 kindle 中拷贝出标注文件，重命名为 source.txt。
- 2、下载本项目源码，使用你的 source.txt 进行替换。
- 3、在 Python3 环境下执行 `python demo.py` 指令，等待生成网页文件。

如下分别为 Linux 和 Windows 下的执行情况：

![Debian](https://github.com/cyang812/kindleNote/raw/master/Debian.png)

![Win7](https://github.com/cyang812/kindleNote/raw/master/Win7.png)

## 进度


### 2016.9.5
	V0.1 实现文件分割, 按照书名生成网页
### 2017.11.7
	V1.0 修复特殊字符无法创建文件名的问题
### 2017.11.8
	V1.1 增加 Semantic UI, 美化生成的网页
	V1.2 增加 index.html
### 2017.11.9
	V1.3 修复linux下文件名过长的问题


## 功能说明

- 1、按照书名导出一个个独立的网页文件，文件内容包含每本书的所有的书签内容

    V1.0
    ![V1.0](https://github.com/cyang812/kindleNote/raw/master/V1.0.png)

    V1.1
    ![V1.1](https://github.com/cyang812/kindleNote/raw/master/V1.1.png)

    V1.2
    ![V1.2](https://github.com/cyang812/kindleNote/raw/master/V1.2.png)
