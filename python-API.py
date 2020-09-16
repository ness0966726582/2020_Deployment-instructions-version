#處理進度條pip install progressbar2 

######關閉DHCP SERVER(避免不斷發送IP)###
sudo apt install -y isc-dhcp-server
sudo isc-dhcp-server stop

######定时 cron 任务###
安裝 > pip3 install APScheduler 

######Google套件######
更新 >python -m pip install --upgrade pip
安裝 >pip3 install gspread
安裝 >pip3 install gspread oauth2client

######溫濕度計-DHT11######
pip3 install Adafruit_DHT

######I2C-LCD############
設定 >sudo raspi-config------->Advance Option內啟用i2c
安裝 >sudo apt-get install i2c-tools
安裝 >sudo apt-get install python-smbus
CMD >i2cdetect -y 1   #確認I2C使用的位址0X27

打開I2C_LCD_driver修改內容:
I2C bus (I2CBUS = 0)----->改成1 #Raspberry PI3 的型號 use port 1
I2C address (ADDRESS = 0x27).

###### ARDUINIO 串接 RASPBERRY ############
[查詢USB位置]pi@nesspi:~$ls -i /dev/tty*
[內容修改]serial.Serial('/dev/ttyUSB1', 9600)