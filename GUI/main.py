# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("myApp.ui",self)
       # self.searchButton.clicked.connnect(self.searchFunction)

  #  def searchFunction(self):
      # searchText=self.search.text()
      #  print("Successfully retrieved stat for opening : ",  searchText)




app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(1100)
widget.setFixedWidth(1100)
widget.show()
app.exec_()
