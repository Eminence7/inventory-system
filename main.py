from PyQt6 import QtWidgets, uic, QtCore
from Ardino import Ardino
from RobotArm import RobotArm
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
        self.scanner = Ardino()
        self.robotArm = RobotArm("MyRobot")


    #     #self.model.appendColumn(self.dataAccess.getData().columns)
    #     self.label.setText("Hello World!")
    #     self.tableView.setModel(self.model)

    #     self.textEdit.setPlainText ("Thi is a test")
    #     self.btnHello.clicked.connect(self.btnClick)
    #     self.textEdit.textChanged.connect(self.onTextChanged)
    #     self.btnRetrieve.clicked.connect(self.onRetrieveItemClicked)
    self.btnScanNow.clicked.connect(self.scanNowClicked)
    self.btnReshelve.clicked.connect(self.reshelveClicked)

    def scanNowClicked(self):
        rfid = self.scanner.ScanRFID()
        boxid = self.leBoxId.toPlainText()
        location = self.leLocation.toPlainText()
        userName = self.leUserName.toPlainText()

        self.dataAccess.SaveRecord(boxId, location, userName, rfid)

    def reshelveClicked(self):
        location = self.leLocation_se.toPlainText()
        self.robotArm.PlaceBox(location)
        
    # def onRetrieveItemClicked(self):
    #     rfid = self.textEdit.toPlainText()
    #     #self.master.RetrieveItem(rfid)   

    # def onTextChanged(self):
    #     name = self.textEdit.toPlainText()
    #     self.label.setText("Hello " + name)

    # def btnClick(self):
    #     name = self.textEdit.toPlainText()
    #     self.label.setText("Hello " + name)

app = QtWidgets.QApplication(sys.argv)
window = DemoWidget()
app.exec()

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()

sys.exit(app.exec_())
window