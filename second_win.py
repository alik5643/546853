from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication , QWidget,
    QHBoxLayout , QVBoxLayout , 
    QGroupBox , QRadioButton , 
    QPushButton ,  QLabel , QListWidget , QLineEdit
)

from instr import * 



class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(wwin_x,win_y)
    def initUI(self):
        self.name = QLineEdit(txt_name,self)
        self.age = QLineEdit(txt_hintage,self)
        self.test1 = QLabel(txt_test1)
        self.start1test = QPushButton(txt_starttest1)
        self.test1results = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.start2test = QPushButton(txt_starttest2)
        self.test2results = QLineEdit(txt_hinttest2)
        self.test3 = QLabel(txt_test3)
        self.start3test = QPushButton(txt_starttest3)
        self.test3results = QLineEdit(txt_hinttest3)
        
    def next_click(self):
        self.tw = TestWin()
        self.hide()