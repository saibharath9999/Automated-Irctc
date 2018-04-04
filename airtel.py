from selenium import webdriver
import time
def webPage():
    global dr
    cd="C:\\Users\\saibh_000\\Downloads\\chromedriver"
    dr = webdriver.Chrome(cd)
    dr.get("https://www.airtel.in/postpaid-bill-pay/")
    details()
def details():
    Num=dr.find_element_by_name('phone_number_field')
    Num.send_keys('9704615559')
    time.sleep(1)
    Amnt=dr.find_element_by_id('amount_input')
    time.sleep(2)
    Amnt.send_keys('150')
    dr.find_element_by_xpath('//*[@id="scroll"]/div/section/div[2]/button').click()
    time.sleep(3)
    paySelect()
def paySelect():
    dr.find_element_by_xpath('//*[@id="payments_tab"]/payment-options/div/div/div/ul/li[2]/a').click()
    cardname=dr.find_element_by_id('card_holder_name')
    cardname.send_keys("saibharath")
    cardnum=dr.find_element_by_id('card_number')
    cardnum.send_keys("5596010000718849")
    mnth=dr.find_element_by_id('expiry_month')
    mnth.send_keys("11")
    year=dr.find_element_by_name('expiry_year')
    year.send_keys("22")
    cvv=dr.find_element_by_id('cvv')
    cvv.send_keys("443")
    #dr.find_element_by_xpath('//*[@id="payments_tab"]/payment-options/div/div/div/div/div[2]/cards-tab/div/page-buttons/div/div/div/div/div/button[1]').click()
webPage()
dr.quit()