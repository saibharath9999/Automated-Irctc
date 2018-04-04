from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#### LOGIN
User_Name = "Marellasai"
Password = "Saimarella"
#### TRAVEL_DETAILS
Source = "CHENNAI CENTRAL - MAS"
Dest = "THRISUR - TCR"
Date = "12-01-2018"
#### PASSENGER_DETAILS
Name = ["saibharath","Yogambareesha","Heamamalini"]
Age = ['24','49','43']
Gender = ["Male","Male","Female"]

def webPage():
    global dr
    cd="C:\\Python34\\chromedriver"
    dr = webdriver.Chrome(cd)
    dr.maximize_window()
    dr.get("https://www.irctc.co.in/eticketing/loginHome.jsf")
    login()
def login():
    Name = dr.find_element_by_name('j_username')
    Name.send_keys(User_Name)
    Pass=dr.find_element_by_name('j_password')
    Pass.send_keys(Password)
    #WebDriverWait(dr,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="nlpAnswer"]')))
    WebDriverWait(dr,100).until(EC.visibility_of(dr.find_element_by_name('j_captcha')))
    time.sleep(5)
    dr.find_element_by_id("loginbutton").click()
    print("LOGIN SUCCESS")
    travel_Details()
def travel_Details():
    src=dr.find_element_by_xpath('//*[@id="jpform:fromStation"]')
    src.send_keys(Source)
    dest=dr.find_element_by_xpath('//*[@id="jpform:toStation"]')
    dest.send_keys(Dest)
    date=dr.find_element_by_xpath('//*[@id="jpform:journeyDateInputDate"]')
    date.send_keys(Date)
    dr.find_element_by_xpath('//*[@id="jpform:jpsubmit"]').click()
    train_Select()
def train_Select():
    dr.find_element_by_xpath('//*[@id="qcbd"]/table/tbody/tr/td[6]/input').click()  ##TATKAL
    dr.find_element_by_xpath('//*[@id="cllink-12623-SL-3"]').click()
    WebDriverWait(dr, 100).until(EC.visibility_of(dr.find_element_by_link_text('Book Now')))
    dr.find_element_by_link_text('Book Now').click()
    passenger_Details()
def passenger_Details():
    dr.find_element_by_xpath('//td[2]/input').send_keys(Name[0])
    dr.find_element_by_xpath('//tr[2]/td[2]/input').send_keys(Name[1])
    dr.find_element_by_xpath('//tr[3]/td[2]/input').send_keys(Name[2])
    dr.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:0:psgnAge"]').send_keys(Age[0])
    dr.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:1:psgnAge"]').send_keys(Age[1])
    dr.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:2:psgnAge"]').send_keys(Age[2])
    dr.find_element_by_xpath('//*[@id="addPassengerForm:onlyConfirmBerths"]').click()
    #dr.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:0:psgnGender"]').send_keys(Gender[0])
    #dr.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:1:psgnGender"]').send_keys(Gender[1])
    #dr.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:2:psgnGender"]').send_keys(Gender[2])
    dr.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(15)
    dr.find_element_by_xpath('//*[@id="validate"]').click()
    time.sleep(2)
    payment_Select()
def payment_Select():
    #time.sleep(20)
    dr.execute_script("window.scrollTo(1,document.body.scrollHeight);")
    WebDriverWait(dr,200).until(EC.presence_of_element_located((By.XPATH,'//*[@id="DEBIT_CARD"]')))
    #dr.find_element_by_xpath('//*[@id="DEBIT_CARD"]').click()
    dr.find_element_by_xpath('//*[@id="NETBANKING"]').click()
    dr.find_element_by_xpath('//div[4]/table/tbody/tr/td/table/tbody/tr/td[1]/input').click()
    #dr.find_element_by_xpath('//div[6]/table/tbody/tr/td/table/tbody/tr/td[1]/input').click()
    dr.find_element_by_xpath('//*[@id="validate"]').click()
    net()
    #pay()
def pay():
    card_num=dr.find_element_by_name('debitCardNumber')
    card_num.send_keys('1123456699625587')
    mnth=dr.find_element_by_id('debiMonth')
    mnth.send_keys('06')
    year=dr.find_element_by_id('debiYear')
    year.send_keys('2019')
    name=dr.find_element_by_id('debitCardholderName')
    name.send_keys('saibharath')
    pin=dr.find_element_by_id('cardPin')
    pin.send_keys('1589')
    time.sleep(5)
    #dr.find_element_by_name('proceed').click()
def net():
    dr.find_element_by_xpath('//*[@id="username"]').send_keys('saibharath9999')
    dr.find_element_by_xpath('//*[@id="label2"]').send_keys('9S@ibharath')
    dr.find_element_by_xpath('//*[@id="login_block"]/div[2]/div[1]/div[2]/div/input[1]').click()
    dr.find_element_by_xpath('//*[@id="Go"]').click()
    dr.find_element_by_xpath('//*[@id="confirmButton"]').click()
webPage()
time.sleep(5)
#dr.find_element_by_xpath('//*[@id="topnav"]/li[8]/ul/li[5]/a').click()
#dr.quit()

