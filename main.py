from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from Control import Control 
if __name__ == "__main__":
    #first_location = input("Biniş yerinizi giriniz. Ör:Ankara Gar\n")
    #last_location = input("İniş yerinizi giriniz. Ör:İstanbul(Bostancı)\n")
    #date = input("Gideceğiniz günü giriniz. Ör:18.07.2021\n")
    #timee = input("Saati giriniz. Ör:15:00\n")


    Control("İstanbul(Bostancı)","Ankara Gar" , "2.02.2023").isEmpty()
    time.sleep(5)
    Control("İstanbul(Bostancı)","Ankara Gar" , "2.02.2023").isEmpty()
    time.sleep(2)
    """
    while(1):
        try:
            Control("Ankara Gar","İstanbul(Bostancı)" , "11.05.2022").isEmpty()
            time.sleep(10)
            Control("Ankara Gar","İstanbul(Bostancı)" , "08.05.2022").isEmpty()
            time.sleep(30)
        except:
            pass
    """