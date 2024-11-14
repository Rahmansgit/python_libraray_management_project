import sys
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
   QTableWidget, QTableWidgetItem, QVBoxLayout, QMessageBox, QGridLayout)

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("PyQt5 Testing")

        self.setupUI()

    def setupUI(self):
        self.text = QLabel(self)
        self.text.setText("Library Management System")
        self.text.move(50,50)

        self.btn1 = QWidget.QPushButton(self)
        self.btn1.setText('Click on me')
        self.btn1.clicked.connect(self.on_clicked)
        
    def on_clicked(self):
        self.text.setText("This test has been changed")

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.show()
    sys.exit(app.exec_())
    
main()
