from PySide6.QtWidgets import QApplication, QMessageBox,QTextEdit
from PySide6.QtUiTools import QUiLoader
from threading import Thread
from collections import defaultdict
from PySide6.QtGui import QIcon
import sys
from pathlib import Path

class Statics:
    NameAndId = defaultdict(str)
    def __init__(self):
        self.initialize()
        self.ui = QUiLoader().load(self.resourse_path('查询模版.ui'))
        self.ui.setWindowIcon(QIcon(self.resourse_path('天津大学logo.jpg')))
        self.ui.search.clicked.connect(self.handle_search)
        self.ui.fuzzysearch.clicked.connect(self.handle_fuzzysearch)
    
    def resourse_path(self, filename):
        if hasattr(sys, '_MEIPASS'):
            return str(Path(sys._MEIPASS) / 'QT_UI' / filename)
        else:
            return str(Path(__file__).parent.resolve() / filename)
    def initialize(self):
        txt_path = self.resourse_path('天津大学2024级学号姓名.txt')
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
            QMessageBox.warning(self.ui,'提示','请输入内容')
            return
        for i in self.NameAndId.keys():  
            if info in i:  
                result.append(i)
    
        result_str = "\n".join(result)
        #QMessageBox.about(self.ui, '查询结果', f'查询结果：\n{result_str}')
        msg_box = QMessageBox(self.ui)
        msg_box.setWindowTitle('查询结果')
        msg_box.setText(f'找到 {len(result)} 条匹配结果：')
        msg_box.setDetailedText(result_str)
        msg_box.exec()



app = QApplication([])
statics = Statics()
statics.ui.show()
app.exec()
