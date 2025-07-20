from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from threading import Thread
from collections import defaultdict
import sys
import os
from pathlib import Path
class Statics:
    NameAndId = defaultdict(str)
    def __init__(self):
        self.initialize()
        self.ui = QUiLoader().load(self.get_resource_path('查询模版.ui'))
        self.ui.search.clicked.connect(self.handle_search)
        self.ui.fuzzysearch.clicked.connect(self.handle_fuzzysearch)
    def get_resource_path(self,filename):
        if hasattr(sys, '_MEIPASS'):  # 检查是否是打包环境
            base_path = Path(sys._MEIPASS)  # 临时目录
            return str(base_path / "QT_UI" / filename)
        else:
            base_path = filename  # 开发环境
            return base_path
    
    def initialize(self):
        txt_path = self.get_resource_path("天津大学2024级学号姓名.txt")
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                l = line.split()
                if l[1] in self.NameAndId.keys():
                    self.NameAndId[l[1]] += ' ' + l[0]
                    continue
                self.NameAndId[l[1]] = l[0]
                self.NameAndId[l[0]] = l[1]

    def handle_search(self):
        info = self.ui.text.toPlainText()
        if len(info) == 0:
            QMessageBox.about(self.ui,'查询结果','请重新输入')
            return
        QMessageBox.about(self.ui,'查询结果', f'查询结果：{self.NameAndId[info]}')

    def handle_fuzzysearch(self):
        result = []
        info = self.ui.text.toPlainText()
        if len(info) == 0:
            QMessageBox.about(self.ui,'查询结果','请重新输入')
            return
        for i in self.NameAndId.keys():  
            if info in i:  
                result.append(i)
    
        result_str = "\n".join(result)
        QMessageBox.about(self.ui, '查询结果', f'查询结果：\n{result_str}')



app = QApplication()
statics = Statics()
statics.ui.show()
app.exec()