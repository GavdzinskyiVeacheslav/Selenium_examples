from selenium import webdriver
import time

driver = webdriver.Chrome(r"path\to\chromedriver.exe")
driver.get('https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A9b15b0994c6df9fc%2C10%3A1591711286%2C16%3A66b338ce162d6599%2Ca78a0c663f0beb12c0559379b61a9f5d62868c4fbd2f00e46a86ac26796507a1%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22921f8f04441041069683cc2377152422%22%7D&response_type=code&o2v=1&as=NCQvtBXI4prkLLDbn4Re0w&flowName=GeneralOAuthFlow')
time.sleep(3)
email = driver.find_element_by_id('identifierId')
email.send_keys('LOGIN')

nextBtn = driver.find_element_by_id('identifierNext')
nextBtn.click()

time.sleep(2)
passwd = driver.find_element_by_name('password')
passwd.send_keys('PASSWORD')


nextBtn = driver.find_element_by_id('passwordNext')
nextBtn.click()

print("Login completed!")

# https://ru.stackoverflow.com/questions/1157453/%D0%9A%D0%B0%D0%BA-%D0%B7%D0%B0%D0%B9%D1%82%D0%B8-%D0%B2-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82-google-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-selenium
