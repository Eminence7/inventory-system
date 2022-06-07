from PyQt6 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMessageBox
from Ardino import Ardino
from robotArm import RobotArm
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


    #   #self.model.appendColumn(self.dataAccess.getData().columns)
    #   self.label.setText("Hello World!")
    #   self.tableView.setModel(self.model)

    #   self.textEdit.setPlainText ("Thi is a test")
    #   self.btnHello.clicked.connect(self.btnClick)
    #   self.textEdit.textChanged.connect(self.onTextChanged)
    #   self.btnRetrieve.clicked.connect(self.onRetrieveItemClicked)
        self.btnScanNow.clicked.connect(self.scanNowClicked)
        self.shelveBtn.clicked.connect(self.shelveClicked)
        self.Sy_searchBtn.clicked.connect(self.search_script_clicked)
        self.Verify_Btn.clicked.connect(self.verify_scan_clicked)
        self.btnReshelve.clicked.connect(self.reshelveClicked)
        #self.excel_loadbtntn.clicked.connect(self.)
    
    def scanNowClicked(self):
        rfid = self.scanner.ScanRFID()
        boxid = self.leBoxId.text()
        Location = self.leLocation.text()
        userName = self.leUserName.text()
        subject = self.leSubject.text()

        self.dataAccess.SaveRecord(boxid, Location, userName, rfid, subject)
        self.textB_append(rfid) 
    def shelveClicked(self):
        location = self.leLocation_se.toPlainText()
        self.robotArm.PlaceBox(location)
       
    def  reshelveClicked(self):  
        ret_RFID = self.rfid_te.toPlainText.split(',',5)
        for idcode in ret_RFID:
            rfid_ret = idcode        
        ret_User=self.leRequester.toPlainText
        ret_Box=self.leBox_ref.toPlainText
        course= self.leCourse.toPlainText
        self.dataAccess.Record_adjust(ret_Box, ret_User, rfid_ret, subject)
    
    def verify_scan_clicked(self, ret_rfid):
        return
        
    def search_script_clicked(self):
        try:
            self.dataAccess.search_send()
        except BaseException as error:
            self.show_Dialog()

           

    def show_Dialog():
        msg= QMessageBox(Warning, "Error", "Item/s not in database")
        x= msg.exec()
    
    def onRetrieveItemClicked(self):
        rfid = self.textEdit.toPlainText()
        self.master.RetrieveItem(rfid) 

    def textB_append(self, rfid):
        self.ScannedDfBrowser.moveCursor(QtTextCursor.Start)
        self.ScannedDfBrowser.append(rfid)
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