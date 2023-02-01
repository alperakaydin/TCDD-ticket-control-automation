from email import message
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from Telegram import sendMessage
import requests
import re

regex = r"\(+\d+\)$"


class Control:
    def __init__(self,nereden,nereye,tarih):
        self.nereden = nereden
        self.nereye = nereye
        self.tarih = tarih

    def isEmpty(self):
        try:
            driver = webdriver.Chrome("/Users/alper/Desktop/Projeler/bilet_auto/chromedriver")
            driver.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")
            #elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mainTabView:gidisSeferTablosu:1:j_idt109:0:somVagonTipiGidis1_label']")))
            time.sleep(1)
            
            _nereden = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/form/div[1]/p[4]/input')
            
            _nereye = driver.find_element_by_xpath('//*[@id="nereye"]')
            _tarih = driver.find_element_by_xpath('//*[@id="trCalGid_input"]')
            ara = driver.find_element_by_xpath('//*[@id="btnSeferSorgula"]/span')
            
            
            _nereden.send_keys(self.nereden)
            _nereye.send_keys(self.nereye)
            _tarih.clear()
            _tarih.send_keys(self.tarih)
            
            time.sleep(1)
            
            ara.click()
            
            time.sleep(3)
            
            seferTablosu = driver.find_elements_by_xpath('//*[@class="ui-selectonemenu-label ui-inputfield ui-corner-all"]')
            

            for sefer in seferTablosu:

                try:
                    if(sefer.text !=""):
                        print(sefer.text)
                        matches = re.search(regex, sefer.text)
                        s = int(matches.start())
                        e = int(matches.end())
                        emptyNumber = int(sefer.text[s+1 : e-1])
                        print(matches)
                        if(emptyNumber > 0):
                            
                            info = f" {self.nereden} -> {self.nereye} \n {self.tarih} \n {emptyNumber -2} adet yer var ..."
                            print(info)
                            sendUrl = "https://api.telegram.org/bot5329313401:AAEJvzBArLj3vfo7xvs7-xf0ioyv6vFPGVw/sendMessage"
                            requests.post(url=sendUrl, data={"chat_id":"1099086328","text":info})
                            

                except:
                    pass
        
            #lement.get_attribute("value")
            time.sleep(3)
            driver.close()

        except:
            print("Control error !!!!!!")
            time.sleep(2)
            driver.close()
            pass # Hata mesajı oluştur