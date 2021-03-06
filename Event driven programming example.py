#Daniel Ogunlana
#16/06/2015
#Event driven programming example

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from name_widget import *
from back_widget import *

import sys

class ExampleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.stack = QStackedLayout()

        #create ui widgets
        self.name = NameWidget()
        self.back = BackWidget()

        #add widgets to stack
        self.stack.addWidget(self.name)
        self.stack.addWidget(self.back)

        #wrap stack in a widget
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        #set central widget
        self.setCentralWidget(self.widget)

        #connections
        self.name.NameEntered.connect(self.name_entered)

    def name_entered(self):
        print("A name was entered")
        self.stack.setCurrentIndex(1)
        name = self.name.name.text()
        self.back.label.setText(name)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleWindow()
    window.show()
    window.raise_()
    app.exec_()
