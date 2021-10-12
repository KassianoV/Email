import win32com.client

#other libraries to be used in this script 
import os 
from datetime import datetime, timedelta

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
""" outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace('MAPI')
 """

""" for account in mapi.Accounts: 
    print(account.DeliveryStore.DisplayName)
"""

""" for idx, folder in enumerate(mapi.Folders):
    #index starts from 1
    print(idx+1, folder) """

for idx, folder in enumerate(outlook.Folders(1).Folders): 
    print(idx+1, folder)
