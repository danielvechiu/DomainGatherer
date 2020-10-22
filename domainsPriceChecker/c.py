import whois
from time import sleep
from selenium import webdriver
domains = []  # creating the empty variable
driver = webdriver.Chrome(r"C:\Users\PC\Desktop\domainsPriceChecker\chromedriver.exe") #change path to chromedriver.exe
pricedDomains = []

class Domain:
    def __init__(self, url, price):
        self.url = url
        self.price = price

def Login():
    driver.get("https://sso.godaddy.com/?realm=idp&path=%2fproducts&app=account")
    sleep(2)
    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    username.send_keys('danielspop')
    password.send_keys('passwordHere')
    loginBtn = driver.find_element_by_xpath('//*[@id="submitBtn"]')
    loginBtn.click()
    sleep(2)

def Check(dom):
    textfield = driver.find_element_by_xpath('//*[@id="inputSearch"]')
    textfield.send_keys(dom)
    button = driver.find_element_by_xpath('//*[@id="btnSearch"]') 
    button.click()
    sleep(2)
    returnedText = driver.find_element_by_xpath('//*[@id="domainvaluation"]/div[1]/div/div/div/div[1]/div[1]/h3/span[3]/strong').text
    price = int(''.join(c for c in returnedText if c.isdigit()))
    domain1 = Domain(dom, price)
    pricedDomains.append(domain1)
    textfield = driver.find_element_by_xpath('//*[@id="inputSearch"]')
    textfield.clear()

with open('./availabledomains.txt') as f:
    domains = f.read().splitlines()

# domains = Sorting(domains)
Login()
driver.get("https://uk.godaddy.com/domain-value-appraisal/appraisal/")
for dom in domains:
    Check(dom)
pricedDomains = sorted(pricedDomains, key=lambda domain: domain.price, reverse=True)
for pd in pricedDomains:
    li = open('./pricedDomains.txt', 'a')
    li.write(pd.url + ' - $' + str(pd.price) + '\n')
    li.close()
