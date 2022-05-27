import pandas as pd

class DataAccess(object):

    def __init__(self):
        dfdata=pd.read_excel(r'C:\Users\jorda\OneDrive\Desktop\FINAL YEAR RFID LITERATURE\inventory system arduino code id12\inventory Main database.xlsx')
        self.dfdata =pd.DataFrame(dfdata)

    def getData(self):
        return self.dfdata
    
    def SaveRecord(self, boxId, location, username, rfid):
        dfadd = pd.DataFrame(
        {"Box": [boxId],
        "RFID": [rfid],
        "Location": [Location],
        "User": [username]})
        self.dfdata
         
       
        dfdata= pd.concat(frame)


