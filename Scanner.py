# Modules
import nmap
import os
import time

# Variables
scanner = nmap.PortScanner()

index = """
 _____   _____       ___   __   _   __   _   _____   _____   
/  ___/ /  ___|     /   | |  \ | | |  \ | | | ____| |  _  \  
| |___  | |        / /| | |   \| | |   \| | | |__   | |_| |  
\___  \ | |       / / | | | |\   | | |\   | |  __|  |  _  /  
 ___| | | |___   / /  | | | | \  | | | \  | | |___  | | \ \  
/_____/ \_____| /_/   |_| |_|  \_| |_|  \_| |_____| |_|  \_\  v1.0
"""
line = "============================================================="

# Index
os.system('clear')
print(index)
print(line)

# User-Input
Port_Num_Begin = int(input("Port Range Begin : "))
print(line)
Port_Num_End = int(input("Port Range End : "))
print(line)
Target_Ip_Address = input("Ip Address : ")
print(line)

# Function
for i in range(Port_Num_Begin , Port_Num_End):
    i = i+1
    result = scanner.scan(Target_Ip_Address,str(i))
    
    try:
        result = result['scan'][Target_Ip_Address]['tcp'][i]['state']
    except KeyError:
        print("Please Type An Correct IP...!")
        time.sleep(1)
        exit()
        
    time.sleep(2)
    print("Port", i ,"Is", result)
