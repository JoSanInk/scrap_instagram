from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import os
import requests
import time

class IGBot:
    def __init__(self, username, password, target):
        self.username = username
        self.password = password
        self.target = target
        self.service = Service()
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options) # objeto usado para manipular o navegador

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)

        userName = driver.find_element(By.XPATH, '//input[@name="username"]')
        userName.clear()
        userName.send_keys(self.username)

        passWord = driver.find_element(By.XPATH, '//input[@name="password"]')
        passWord.clear()
        passWord.send_keys(self.password)
        passWord.send_keys(Keys.RETURN)
        time.sleep(5)

        self.perfis(self.target)

    def perfis(self, url):
        driver = self.driver
        driver.get(f'https://www.instagram.com/{url}/')
        time.sleep(5)

        refs = []
        for _i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            localRefs = driver.find_elements(By.CLASS_NAME, "x5yr21d")
            for x in localRefs:
                if x.get_attribute('src') not in refs:
                    refs.append(x.get_attribute('src'))
        print(len(refs), ' images to be downloaded.')

        for idx,picRef in enumerate(refs):
            filename = url.replace('.','')+ ' ' + str(idx)

            try:
                img = requests.get(picRef)
                if img.status_code != 200:
                    print(f'IMAGE COUDNT BE DOWNLOADED, URL: {picRef}')
                else:
                    Path(f'{os.path.expanduser('~')}\\Desktop\\{url}\\').mkdir(parents=True, exist_ok=True)
                    with open(f'{os.path.expanduser('~')}\\Desktop\\{url}\\{filename}.jpg', 'wb') as f:
                        f.write(img.content)
                        print(f'saved {filename}')
            except:
                try:
                    if picRef == None:
                        print('INEXISTENT IMAGE')
                except:
                    print(f'(EXEPT) IMAGE COUDNT BE DOWNLOADED, URL: {picRef}')
                    print(f'{os.path.expanduser('~')}\\Desktop\\{url}\\{filename}.jpg')
