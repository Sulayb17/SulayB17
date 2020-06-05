
#This script that advertises a bluetooth low energy beacon for 15 seconds


import time #<----1st party class module

from bluetooth.ble import BeaconService #<---3rd party module

#Create an instace of the object from the 3rd party class

service = BeaconService() #Creating BeaconService as a variable into service

service.start_advertising("11111111-2222-3333-4444-555555555555", 1, 1, 1, 200) #Parameters are how you recive the UUID
                                       #UUID                       #Parameters
time.sleep(15) #Sets amount of time the signal will last.

service.stop_advertising()#This stops advertising the signal

print("Done.") #Send message letting us know its done
