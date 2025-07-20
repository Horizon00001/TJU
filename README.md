# 输入姓名查找学号，输入学号查找姓名

使用方法：


1.如果你安装了pyinstaller，源码下载后在vs终端输入以下内容可自行打包为exe文件

    pyinstaller --onefile --windowed --add-data "天津大学2024级学号姓名.txt;Qt_ui" --add-data "天津大学logo.jpg;Qt_ui" --add-data "查询模版.ui;Qt_ui" --hidden-import PySide6.QtXml --icon="D:\Qt_ui\天津大学logo.ico" 查询.py

2.或者可以下载两个压缩包解压成exe文件



使用效果：


<img width="210" height="170" alt="image" src="https://github.com/user-attachments/assets/9e34a76f-0a97-47a6-ad40-1680fcdc0174" />    <img width="210" height="170" alt="image" src="https://github.com/user-attachments/assets/95df46cf-b3bf-4b39-9cf0-5df6082c529f" />



