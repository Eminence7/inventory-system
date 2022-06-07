import pandas as pd
import time
from datetime import datetime
class DataAccess(object):

    def __init__(self):
        self.dfdata=pd.read_excel(r'C:\Users\jorda\OneDrive\Desktop\FINAL YEAR RFID LITERATURE\inventory system arduino code id12\inventory Main database.xlsx')
        self.df_main =pd.DataFrame(self.dfdata)

    def getData(self):
        return self.dfdata
    #save to MS Excel sheet and create Closed loop/feedback into Main MS Excell sheet
    def SaveRecord(self, boxId, Location, username, rfid,subject):
        dfadd = pd.DataFrame(
        {"Box": [boxId],
        "RFID": [rfid],
        "Location": [Location],
        "User": [username],"Subject":[subject],"Time in":[dt] })
        self.df_main
         
        frame= [dfadd,self.df_main]
        self.df_main= pd.concat(frame)
        self.df_main.to_excel("inventory Main database.xlsx") 

    def Record_adjust(self, ret_RFID,ret_User,ret_Box):
        if ret_RFID or ret_Box ==df_main[RFID or Box]:  
            df_main.where(df_main['RFID' or 'Box'] == ret_RFID or ret_Box)
            df_main["Availability"].replace({"unavailable": "available"}, inplace=True)
            #df_main[]
            df_main["Time in"]
    #############################################################
   
    def search_send(self, ret_Box, ret_rfid,):
        self.time_delay= time.sleep(10)
       
        if df_main['RFID'].where(df_main[course] == ret_rfid):
            ser.write(df_main['Location'].where(df_main['RFID'] == ret_RFID))
            time_delay
        if df_main.where(df_main['Box']==ret_Box):
            ser.write(df_main[Location].where(df_main['Box']==ret_Box))
            time_delay
      
    
