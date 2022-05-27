import pandas as pd
import serial
import time
import sys
import glob


class Ardino(object):
    BAUD_RATE = 9600
    RFID_BYTES = 12
    START_CHAR = '\x02'
    COM_PORT = 'COM2'
    def __init__(self):
        print("hello")
        self.ser = serial.Serial(COM_PORT, BAUD_RATE)

    def ScanRFID(self ):
        # Wait until a tag is read
        rfid = ser.read(RFID_BYTES)
        rfid = str(rfid).strip(START_CHAR)
        return rfid;
        
        
