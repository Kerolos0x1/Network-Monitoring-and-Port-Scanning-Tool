# Modules
import os

# Variables
index = """
 __   _   _____   _____   _          __  _____   _____    _   _   
|  \ | | | ____| |_   _| | |        / / /  _  \ |  _  \  | | / /  
|   \| | | |__     | |   | |  __   / /  | | | | | |_| |  | |/ /   
| |\   | |  __|    | |   | | /  | / /   | | | | |  _  /  | |\ \   
| | \  | | |___    | |   | |/   |/ /    | |_| | | | \ \  | | \ \  
|_|  \_| |_____|   |_|   |___/|___/     \_____/ |_|  \_\ |_|  \_\ v1.0
"""
line = "========================================================================"

# Index
os.system('clear')
print(index)
print(line)

print("1.Port Scanner")
print("2.DHCP Listen")

# User-Input
user_input = int(input("Choose : "))

# Conditions
if user_input == 1:
    os.system('clear')
    os.system('python3 Scanner.py')
    
elif user_input == 2:
    os.system('clear')
    os.system('sudo python3 DHCP.py')