#Daniel Ogunlana
#19/06/2015
#back_widget

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class BackWidget(QWidget):
    BackButton = pyqtSignal()
    def __init__(self):
        super().__init__()

        #Create Components
        self.label = QLabel()
        self.back = QPushButton("Back")

        #create layout
        self.layout = QVBoxLayout()

        #add componetes to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.back)

        #add layout to widget
        self.setLayout(self.layout)

        #connections
        self.back.clicked.connect(self.return_menu)

    def return_menu(self):
        
        self.BackButton.emit()
