import sys
import time
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QRadioButton,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QComboBox, QTextEdit,QButtonGroup
from controller import controller
class MyWidget(QWidget):
    def __init__(self):
        self.controll=controller()
        app = QApplication(sys.argv)
        super().__init__()
        self.initUI()
        self.show()
        sys.exit(app.exec_())

    def initUI(self):
        layout = QVBoxLayout()

        Treelayout = QHBoxLayout()
        self.button_group = QButtonGroup()
        radio_button1 = QRadioButton('B-Tree', self)
        radio_button1.setChecked(True)
        self.button_group.addButton(radio_button1)
        Treelayout.addWidget(radio_button1)
        radio_button2 = QRadioButton('BRTree', self)
        self.button_group.addButton(radio_button2)
        Treelayout.addWidget(radio_button2)
        self.button_group.buttonClicked.connect(self.onButtonClicked)
        layout.addLayout(Treelayout)

        file_layout = QHBoxLayout()
        self.filepath_input = QLineEdit(self)
        file_layout.addWidget(self.filepath_input)
        file_dialog_button = QPushButton('Browse', self)
        file_dialog_button.clicked.connect(self.showDialog)
        file_layout.addWidget(file_dialog_button)
        import_button = QPushButton('Import', self)
        import_button.clicked.connect(self.importclicked)
        file_layout.addWidget(import_button)
        layout.addLayout(file_layout)
        

        add_delete_layout = QHBoxLayout()
        add_delete_layout.addWidget(QLabel('English:', self))
        self.input_English = QLineEdit(self)
        add_delete_layout.addWidget(self.input_English)
        add_delete_layout.addWidget(QLabel('Chinese:', self))
        self.input_Chinese = QLineEdit(self)
        add_delete_layout.addWidget(self.input_Chinese)
        add_button = QPushButton('Add', self)
        add_delete_layout.addWidget(add_button)
        add_button.clicked.connect(self.addclicked)
        delete_button = QPushButton('Delete', self)
        add_delete_layout.addWidget(delete_button)
        delete_button.clicked.connect(self.deleteclicked)
        layout.addLayout(add_delete_layout)

        translate_layout = QHBoxLayout()
        self.input_translatedword = QLineEdit(self)
        translate_layout.addWidget(self.input_translatedword)
        translate_button = QPushButton('Translate', self)
        translate_layout.addWidget(translate_button)
        translate_button.clicked.connect(self.translateclicked)

        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel('Search Range From', self))
        self.from_text = QLineEdit(self)
        search_layout.addWidget(self.from_text)
        search_layout.addWidget(QLabel('To', self))
        self.to_text = QLineEdit(self)
        search_layout.addWidget(self.to_text)
        submit_button = QPushButton('Submit', self)
        submit_button.clicked.connect(self.submitclicked)
        search_layout.addWidget(submit_button)
        layout.addLayout(translate_layout)
        layout.addLayout(search_layout)

        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)
        self.setWindowTitle('Translator')

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')
        self.filepath_input.setText(fname[0])
    #导入按钮事件
    def importclicked(self):
        self.output_text.append("Importing...")
       
        self.output_text.append(self.controll.importfrom(self.filepath_input.text()))
        self.output_text.append("Finished!")
    #
    def addclicked(self):
        self.output_text.append("Adding...\nmassage:"+self.input_English.text() +'  '+self.input_Chinese.text())
        self.controll.add(self.input_English.text(),self.input_Chinese.text())
        self.output_text.append("Finished!")
    
    def deleteclicked(self):
        self.output_text.append("Deleting...")
        self.controll.delete(self.input_English.text())
        self.output_text.append("Finished!")

    def translateclicked(self):
        self.output_text.append("Translating...")
        self.output_text.append(self.controll.search(self.input_translatedword.text()))
        self.output_text.append("Finished!")
    
    def submitclicked(self):
        self.output_text.append("Submitting...")
        self.output_text.append(self.controll.searchByRange(self.from_text.text(),self.to_text.text()))
        self.output_text.append("Finished!")
    def onButtonClicked(self, button):
        # 检查哪个按钮被选中，并执行相应的操作
        if button.text() == 'B-Tree':
            self.output_text.append("B-Tree now!Please import again!")
            self.controll.changetype(0)

        elif button.text() == 'BRTree':
            self.output_text.append("BRTree now!Please import again!")
            self.controll.changetype(1)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
    