#library import 
import pandas as pd
import time 
from rest_sms_gateway import SMSGatewayClient 

#cvs file load here
df = pd.read_csv('dataset/numbers.csv')
# Device Initialize 
no_Devices = 5
device_no1 = ""
device_no2 = ""
device_no3 = ""
device_no4 = ""
device_no5 = ""
# delay Define 
delay = 4
# Massege 
massege = "Hello This is Ahmed Hassan Here!!!!"
# create list 
number_list = [] 
#counter auto update value
counter =  no_Devices - 1

# loop for sending massege 
for key , number in enumerate(df['Number']):
    #add number in list
    number_list.insert(key,number)  
    
    #send Massege
    if(key == counter):
        if(no_Devices == 1):
            print(number_list[0])
        elif(no_Devices == 2):
            print(number_list[0] , number_list[1])
        elif(no_Devices == 3):
           print(number_list[0] , number_list[1], number_list[2])
        elif(no_Devices == 4):
            print(number_list[0] , number_list[1], number_list[2], number_list[3])
        elif(no_Devices == 5):
            print(number_list[0] , number_list[1], number_list[2], number_list[3], number_list[4])        
        
        time.sleep(delay)
    
    print(key)

      
    


