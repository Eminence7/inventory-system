from PyQt6 import QtWidgets, uic, QtCore
from Ardino import Ardino
from dataAccess import DataAccess
import sys

class DemoWidget(QtWidgets.QWidget):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(DemoWidget, self).__init__()
        # Load the .ui file
        uic.loadUi('main.ui', self)
        # Show the widget
        self.dataAccess = DataAccess()
        self.show()
        self.model = QtCore.QStringListModel()
        self.master = Ardino()


        #self.model.appendColumn(self.dataAccess.getData().columns)
        self.label.setText("Hello World!")
        self.tableView.setModel(self.model)

        self.textEdit.setPlainText ("Thi is a test")
        self.btnHello.clicked.connect(self.btnClick)
        self.textEdit.textChanged.connect(self.onTextChanged)
        self.btnRetrieve.clicked.connect(self.onRetrieveItemClicked)


    def onRetrieveItemClicked(self):
        rfid = self.textEdit.toPlainText()
        self.master.RetrieveItem(rfid)   

    def onTextChanged(self):
        name = self.textEdit.toPlainText()
        self.label.setText("Hello " + name)

    def btnClick(self):
        name = self.textEdit.toPlainText()
        self.label.setText("Hello " + name)

app = QtWidgets.QApplication(sys.argv)
window = DemoWidget()
app.exec()

# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()