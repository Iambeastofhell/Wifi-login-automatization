from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import socket


import subprocess
try:
    def checkssid():
        try:
            # For Windows: "netsh wlan show interfaces"
            # For Linux/macOS: "nmcli -t -f active,ssid dev wifi"
            result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], universal_newlines=True)
            for line in result.split('\n'):
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()
                    return ssid
        except subprocess.CalledProcessError:
            return None


    counter=False
    if (checkssid()=="Hostel" or checkssid()=="IITPKD" or checkssid()=="IIT-PALAKKAD"):
        counter=True
    else:
        pass

    def is_connected():
        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            return True
        except socket.error:
            return False


    if (counter==True and not is_connected()):
        print("inside")
        driverpath = r"C:\Users\Vishesh\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
        
        service = Service(executable_path=driverpath)
        driver = webdriver.Chrome(service=service)
        driver.get("http://8.8.8.8/")
        sleep(2)
        current_url = driver.current_url
        driver.get(current_url)
        username = driver.find_element(By.ID, "ft_un")
        username.send_keys("username")
        passwd = driver.find_element(By.ID, "ft_pd")
        passwd.send_keys("password" +Keys.RETURN)
        sleep(1)
        driver.quit()
    else:
        print("other")
except:
    exit(1)
