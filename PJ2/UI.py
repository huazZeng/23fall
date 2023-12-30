import sys
import time
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QRadioButton,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QComboBox, QTextEdit,QButtonGroup
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from controller import controller
class MyWidget(QWidget):
    def __init__(self):
        
        app = QApplication(sys.argv)
        super().__init__()
        self.controll=controller()
        self.initUI()
        self.show()
        sys.exit(app.exec_())
    
    def initUI(self):
        pixmap = QPixmap("./data-1/tagged.png")  # 替换为实际图像的路径
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        # 创建右侧垂直布局
        right_layout = QVBoxLayout()
        # 创建两个输入框
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        right_layout.addWidget(QLabel('LocationA:', self))
        right_layout.addWidget(self.input1)
        right_layout.addWidget(QLabel('LocationB:', self))
        right_layout.addWidget(self.input2)
        label = QLabel('You can choose to search Online')
        self.radioButton1 = QRadioButton('Offline')
        self.radioButton2 = QRadioButton('Online')
        self.radioButton1.setChecked(True)
        self.radioButton1.toggled.connect(lambda: self.onRadioButtonToggle(self.radioButton1))
        self.radioButton2.toggled.connect(lambda: self.onRadioButtonToggle(self.radioButton2))
        

        
        # 创建四个按钮
        button1 = QPushButton("oparation 1")
        button1.clicked.connect(self.oparation_1_button)
        button2 = QPushButton("oparation 2")
        button2.clicked.connect(self.oparation_2_button)
        button3 = QPushButton("oparation 3")
        button3.clicked.connect(self.oparation_3_button)
        button4 = QPushButton("oparation 4")
        button4.clicked.connect(self.oparation_4_button)

        # 创建一个输出框
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        # 将部件添加到右侧布局
        right_layout.addWidget(label)
        right_layout.addWidget(self.radioButton1)
        right_layout.addWidget(self.radioButton2)
        right_layout.addWidget(button1)
        right_layout.addWidget(button2)
        right_layout.addWidget(button3)
        right_layout.addWidget(button4)
        
        right_layout.addWidget(self.output_text)

        # 创建水平布局并将左侧大图和右侧布局添加到其中
        main_layout = QHBoxLayout()
        main_layout.addWidget(image_label)
        main_layout.addLayout(right_layout)
        # 设置主布局
        self.setLayout(main_layout)
        image_label.setMinimumSize(600, 600)

        # 设置主布局
        self.setLayout(main_layout)

        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('Mapping')

    def oparation_1_button(self):
        self.output_text.append("Searching...")
        self.output_text.append(self.controll.operation_1(self.input1.text(),self.input2.text()))
        self.output_text.append("---------Finished!--------\n\n\n")

    def oparation_2_button(self):
        self.output_text.append("Searching...")
        self.output_text.append(self.controll.operation_2(self.input1.text()))
        self.output_text.append("---------Finished!--------\n\n\n")


    def oparation_3_button(self):
        self.output_text.append("Searching...")
        self.output_text.append(self.controll.operation_3())
        self.output_text.append("---------Finished!--------\n\n\n")

    def oparation_4_button(self):
        self.output_text.append("Searching...")
        self.output_text.append(self.controll.operation_4(self.input1.text()))
        self.output_text.append("---------Finished!--------\n\n\n")
    def onRadioButtonToggle(self, radio_button):
        if radio_button.isChecked() and radio_button.text()=='Online':
            self.controll.isOnline=True
            self.output_text.append("Online Searching now...\n")
        if radio_button.isChecked() and radio_button.text()=='Offline':
            self.controll.isOnline=False
            self.output_text.append("Offline Searching now...\n")



if __name__ == '__main__':
    app=MyWidget()
