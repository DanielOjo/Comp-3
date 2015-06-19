#Daniel Ogunlana
#16/06/2015
#name_widget

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NameWidget(QWidget):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()

        

        #Create Components
        self.label = QLabel("Please enter your name: ")
        self.name = QLineEdit()
        self.submit = QPushButton("Submit")

        #create layout
        self.layout = QVBoxLayout()

        #add componetes to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.submit)

        #add layout to widget
        self.setLayout(self.layout)

        #connections
        self.submit.clicked.connect(self.display_name)

    def display_name(self):
        name = self.name.text()
        print(name)
        self.NameEntered.emit()
