import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
banner = """
██████  ██   ██     ████████  ██████   ██████  ██     
██   ██ ██   ██        ██    ██    ██ ██    ██ ██     
██████  ███████        ██    ██    ██ ██    ██ ██   
██      ██   ██        ██    ██    ██ ██    ██ ██     
██      ██   ██        ██     ██████   ██████  ███████
Ai cần mua KEYVIP thì IB Tele
\n
Tool By: PHAM HUY                         Phiên Bản: V2     
\033════════════════════════════════════════════════  
           Telegram\033 : https://t.me/phtool
\033════════════════════════════════════════════════          
"""
os.system("cls" if os.name == "nt" else "clear")

for x in banner:
  print(x,end = "")
  sleep(0.001)
print(f" \033[1;33mOFF \033[1;33mTOOL \033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mCảm Ơn Bạn Dùng Tool....!")
