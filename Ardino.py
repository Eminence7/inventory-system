import pandas as pd
import serial
import time
import sys
import glob


class Ardino(object):
    BAUD_RATE = 9600
    RFID_BYTES = 12
    START_CHAR = 'b'#'\x02'
    COM_PORT = 'COM2'
    def __init__(self):
        print("hello")
        self.ser = serial.Serial(self.COM_PORT, self.BAUD_RATE)

    def ScanRFID(self ):
        # Wait until a tag is read
        rfid = self.ser.read(self.RFID_BYTES)
        rfid = str(rfid).strip(self.START_CHAR)
        return rfid;

    def verify_scan(self, ret_RFID, ret_Box):
        vrfid= self.ScanRFID()
        if ret_RFID==vrfid:
           self.dataAccess.Record_adjust()
        if ret_Box:
            self.dataAccess.Record_adjust()

    


        
        
