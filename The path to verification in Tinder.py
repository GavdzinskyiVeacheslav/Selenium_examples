import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options, )  

                                  
        driver.get('https://accounts.google.com/o/oauth2/auth/identifier?redirect_uri=storagerelay%3A%2F%2Fhttps%2Ftinder.com%3Fid%3Dauth548378&response_type=permission%20id_token&scope=email%20profile%20openid&openid.realm&include_granted_scopes=true&client_id=230402993429-g4nobau40t3v3j0tvqto4j8f35kil4hf.apps.googleusercontent.com&ss_domain=https%3A%2F%2Ftinder.com&fetch_basic_profile=true&gsiwebsdk=2&flowName=GeneralOAuthFlow')
        time.sleep(7)
        email_form = driver.find_element_by_id('identifierId')
        email_form.send_keys('Olyatimoshevskaya777@gmail.com')
        time.sleep(7)
        driver.find_element_by_xpath("//span[text()='Далее']").click()
        time.sleep(5)
        passwd = driver.find_element_by_name('password')
        passwd.send_keys('Nub4ek114455')
        driver.find_element_by_xpath("//span[text()='Далее']").click()
        time.sleep(17)
        driver.get(url=url)
        time.sleep(25)
        driver.find_element_by_xpath("//span[text()='Принимаю']").click()
        time.sleep(17)
        driver.find_element_by_xpath("//span[text()='Войдите']").click()
        time.sleep(17)
        driver.find_element_by_xpath("//span[text()='Войти через Google']").click()
        time.sleep(25)
        # driver.find_element_by_xpath("//span[text()='Разрешить']").click()
        # time.sleep(17)
        # driver.find_element_by_xpath("//span[text()='Включить']").click()
        # time.sleep(17)
        driver.find_element_by_xpath("//span[text()='Продолжить']").click()
        time.sleep(25)
        driver.find_element_by_xpath("//span[text()='Далее']").click()
        time.sleep(17)
        driver.find_element_by_xpath("//span[text()='1-я поза']").click()
        time.sleep(17)
        a = driver.find_element_by_xpath("//button[@type='button']")
        a.send_keys("D:/Desktop/SCRIPT/IP-proxy/1.jpg")
        time.sleep(17)

        time.sleep(500000)
    except Exception as ex:
        print(ex)

def main():
    get_data_with_selenium('https://tinder.com')


if __name__ == '__main__':
    main()
