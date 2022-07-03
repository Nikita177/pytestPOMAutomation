import logging
from datetime import datetime

class BrowserLog:
    @staticmethod
    def get_browser_log_entries(driver):
     print("++++++++++++Broswe Log Entries++++++++++++++++++")
    #get browser logs
     slurped_logs = driver.get_log('browser')
     for entry in slurped_logs:
      print(entry)

      #print((datetime.datetime.fromtimestamp(entry['timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))
      # print("Level :",entry['level'],"Message :",entry['message'],"Timestamp :",datetime.fromtimestamp(entry['timestamp']))

       #if entry['level']=="INFO":
        #print("entry['message']",entry['message'])

