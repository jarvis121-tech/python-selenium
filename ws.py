from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bs
from multiprocessing import Process

os.environ['reset'] = 'Nrrs4247@'
RESET_PSWD = os.environ['reset']
cnumber = '4336620200292136'
expMonth = '02'
expYear = '25'
cvc = '014'
def account_reset(userId,number):

    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('--headless')
    while True:
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            # driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chromeOptions)
            # driver.minimize_window()
            driver.get('https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__EVENT_ID__=LOAD&__CALL_MODE__=91&LOGIN_FLAG=1&BANK_ID=ICI')

            # try:
            #     later = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/div[1]')
            #     later.click()
            # except:
            #     pass
            # soup = bs(driver.page_source,'html.parser')
            # print(soup.prettify())
            # login_btn = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/ul/li[9]/a')
            # login_btn.click()
            # dummy_userid = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, '/html/body/form[1]/div[3]/div[1]/div[2]/p[3]/span/span/input'))
            # )
            # dummy_userid.click()
            # input_userid = driver.find_element_by_xpath('/html/body/form[1]/div[3]/div[2]/div[2]/p[3]/span/span/input')
            # input_userid.click()
            # get_pswd = driver.find_element_by_xpath('/html/body/form[1]/div[3]/div[2]/div[2]/p[7]/span/a')
            # get_pswd.click()
            # driver.switch_to.window(driver.window_handles[1])
            proceed = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'CONTINUE_MODE'))
                )
            # proceed = driver.find_element_by_id('CONTINUE_MODE')
            # soup = bs(driver.page_source, 'html.parser')
            # print(soup.prettify())
            proceed.click()
            reset_userId = driver.find_element_by_xpath('/html/body/form/div[2]/div[3]/div/p[1]/span[3]/span/input')
            reset_userId.send_keys(userId)
            reset_number = driver.find_element_by_xpath('/html/body/form/div[2]/div[3]/div/p[2]/span[8]/span/input')
            reset_number.send_keys(number)
            go_btn = driver.find_element_by_xpath('/html/body/form/div[2]/div[3]/div/p[3]/span/input[2]')
            go_btn.click()
            #Input otp for reset pswd
            reset_otp = WebDriverWait(driver,20).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/form/div[2]/div/div/p[6]/span[3]/input'))
            )
            reset_otp_input = input('Enter otp for reset password')
            reset_otp.send_keys(reset_otp_input)
            go_reset = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/form/div[2]/div/div/p[8]/span/input'))
            )
            go_reset.click()
            """
                Reset password
        
            """
            reset_pswd = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div/p[2]/span[3]/input'))
            )
            reset_pswd.send_keys(RESET_PSWD)
            cnfrm_pswd = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div/p[3]/span[3]/input'))
            )
            cnfrm_pswd.send_keys(RESET_PSWD)
            pswd_reset_go = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div/p[4]/span/input'))
            )
            pswd_reset_go.click()
            driver.quit()
            break
        except Exception as e:
            print(f"Exception Occured {e}")
            driver.quit()



def account_details(userId):
    # global driver
    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('--headless')
    # driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chromeOptions)
    # driver.get('https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get('https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI')
    # try:
    #     later = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/div[1]')
    #     later.click()
    # except:
    #     pass
    # login_btn = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/ul/li[9]/a')
    # login_btn.click()
    dummy_userid = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/form[1]/div[3]/div[1]/div[2]/p[3]/span/span/input'))
    )
    dummy_userid.click()
    optionValue = 2
    while True:
        input_userid = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/form[1]/div[3]/div[2]/div[2]/p[3]/span/span/input')))
        input_userid.click()
        input_userid.send_keys(userId)
        input_pswd = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form[1]/div[3]/div[2]/div[2]/p[6]/input[2]')))
        input_pswd.send_keys(RESET_PSWD)
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form[1]/div[3]/div[2]/div[2]/p[9]/span/span/span/div')))
        options.click()
        option_choose = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form[1]/div[3]/div[2]/div[2]/p[9]/span/span/span/div/div[2]/ul/li['+str(optionValue)+']/a')))
        option_choose.click()
        time.sleep(2)
        login =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form[1]/div[3]/div[2]/div[2]/p[11]/span[1]/input[1]')))
        login.click()
        if optionValue ==2:
            try:
                print("inside try")
                # my_accounts = WebDriverWait(driver,10).until(
                #     EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[2]/div/div/div/div/ul/li[2]'))
                # )
                with open("jquery-3.4.1.min.js", errors='ignore') as f:
                    driver.execute_script(f.read())
                    driver.execute_script('$( document).ready(function() {console.log("Document Ready");});')
                break
            except:
                    print("inside exception")
                    optionValue = 1
    # time.sleep(5)
    # if optionValue == 2:
    #     my_accounts.click()
    #     pockets_acnt = WebDriverWait(driver,10).until(
    #         EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[2]/div/div/div/div/ul/li[2]/ul/li[8]/a'))
    #     )
    #     pockets_acnt.click()
    # elif optionValue == 1:
    #     try:
    #
    #         # showMeAround = WebDriverWait(driver, 10).until(
    #         #     EC.presence_of_element_located(
    #         #         (By.XPATH, '/html/body/form/div[1]/div[5]/div/div[4]/div[3]/div/div[1]/a'))
    #         # ).click()
    #         # exitButton = WebDriverWait(driver, 10).until(
    #         #     EC.presence_of_element_located(
    #         #         (By.XPATH, ('/html/body/form/div[1]/div[5]/div/div[4]/div[3]/div/div[3]/div/a[1]')))
    #         # ).click()
    #     except Exception as e:
    #         print(e)
    #         pass
    #         # my_accounts = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located(
            #         (By.XPATH, '/html/body/form/div[1]/div[4]/div/div/div[3]/div[1]/div/div/div/ul/li[2]/a/div[1]/p'))
            # ).click()
            # pocketsClick = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located(
            #         (By.XPATH, '/html/body/form/div[1]/div[4]/div/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div/a[8]'))
            # ).click()
    with open("jquery-3.4.1.min.js",errors='ignore') as f:
        driver.execute_script(f.read())
    # while True:
    #     try:
    #         print("inside second try")
    #         driver.execute_script("document.getElementById('Pockets').click()")
    #     except:
    #         pass
    #     else:
    #         break
        driver.execute_script('$( document ).ready(function() {document.getElementById("Pockets").click();});')
    cardNumber_element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[3]/div[1]/div[6]/div[2]/div/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr[3]/td[2]/a'))
    )
    cardNumber =cardNumber_element.text
    # view_card_details = WebDriverWait(driver,10).until(
    #     EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[3]/div[1]/div[6]/div[1]/div[2]/div[16]/a[3]'))
    # )
    # view_card_details.click()
    driver.execute_script('document.getElementById("Pockets_View-Card-Details").click()')
    exp_date = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[3]/div[1]/div[6]/div[2]/div/div/div[3]/div/div[2]/p[5]/span[2]/span'))
    )
    expiryDate = exp_date.text
    cvv_text = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[3]/div[1]/div[6]/div[2]/div/div/div[3]/div/div[2]/p[6]/span[2]/span'))
    )
    cvv = cvv_text.text
    print(cardNumber)
    print(expiryDate)
    print(cvv)
    global cnumber
    global expMonth
    global expYear
    global cvc
    cnumber = cardNumber
    expMonth = expiryDate.split('/')[0]
    expYear = expiryDate.split('/')[1]
    cvc = cvv
    # return {
    #     'ccnumber':cardNumber,
    #     'expMonth':expMonth,
    #     'expYear':expYear,
    #     'cvc':cvv
    # }



def aws(firstName,emailId,number,proc):
    global driver
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chromeOptions)
    driver.get('https://portal.aws.amazon.com/billing/signup#/start')
    email_address = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'ccEmail'))
    )
    email_address.send_keys(emailId)
    pswd = driver.find_element_by_id('ccPassword')
    pswd.send_keys(RESET_PSWD)
    repswd = driver.find_element_by_id('ccRePassword')
    repswd.send_keys(RESET_PSWD)
    awsname = driver.find_element_by_id('ccUserName')
    awsname.send_keys(firstName)
    continue_btn = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[5]/button/span/input'))
    )
    continue_btn.click()
    personal = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'personal-account'))
    )
    personal.click()
    phoneNumber = driver.find_element_by_id('phone-number')
    phoneNumber.send_keys(number)
    country = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[4]/select')
    country.click()
    country_choose = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[4]/select/option[102]')
    country_choose.click()
    adress = driver.find_element_by_id('street-address-1')
    adress.send_keys('mulund')
    city = driver.find_element_by_id('city')
    city.send_keys('Mumbai')
    state = driver.find_element_by_id('state')
    state.send_keys('Maharashtra')
    postal_code = driver.find_element_by_id('postal-code')
    postal_code.send_keys('400080')
    agree = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/agreement/div/div[2]/input')
    agree.click()
    account_create = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/button/span/input')
    account_create.click()
    proc.join()
    ccnumber = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'addCreditCardNumber'))
    )
    ccnumber.send_keys(cnumber)
    select = Select(driver.find_element_by_id('expirationMonth'))
    select.select_by_value(str(int(expMonth) - 1))
    select_year = Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/sup-credit-card-input/div/div[2]/div/select[2]'))
    select_year.select_by_visible_text('20' +str(expYear))
    cvc_number = driver.find_element_by_id('cvc')
    cvc_number.send_keys(cvc)
    acntName = driver.find_element_by_id('accountHolderName')
    acntName.send_keys('Nilay')
    pan_no = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/span/span/div/div/label[2]/input')
    pan_no.click()
    verify = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/button/span/span[1]')
    verify.click()


def email_create(email):
    email = email.split("@")[0]

    options = Options()
    options.headless = True
    while True:
        try:
            driver = webdriver.Firefox(options=options)
            driver.get('https://m.kuku.lu/')
            WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,'link_loginform'))
            )
            driver.execute_script("""
                document.getElementById('link_loginform').click()
            """)
            time.sleep(1)
            driver.execute_script("""
                document.getElementById('user_number').value = 'nilayaws';
                document.getElementById('user_password').value = '162017';
            """)
            WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div[9]/div[3]/div/div/input'))
            ).click()
            # WebDriverWait(driver,10).until(
            #     EC.element_to_be_clickable((By.XPATH,'area-confirm-dialog-button-cancel'))
            # ).click()
            time.sleep(3)
            while True:
                driver.execute_script("document.getElementById('area-confirm-dialog-button-cancel').click()")
                try:
                    time.sleep(2)
                    alert = driver.switch_to.alert
                    if alert.text != "You are logged in. Your data will be reloaded." :
                        continue
            # time.sleep(2)
                    alert.accept()
                    break
                except:
                    pass
            WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,'area_mailaddr_54cd571141ff2d88389a8cbebdde0314'))
            )
            WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.ID,'link_addMailAddrByManual'))
            ).click()

            driver.execute_script(f"""
                document.getElementById('input_manualmailaddr').value = "{email}";
                document.getElementById('link_manualmailaddr_domainlist_more').click();
                document.getElementById('radio-choice-ruru.be').click()
        """)
            time.sleep(2)
            WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div[5]/div[1]/div[3]/div/div[6]/input'))
            ).click()
            time.sleep(3)
            print("Email id created")
            driver.quit()
            break
        except Exception as e:
            print(f"Exception occcured {e}")
            driver.quit()

    # time.sleep(5)
# account_reset('NILASH0482','7666090782')
# user_id = input('Enter user id: ')
# number = input('Enter number: ')
# email = input('Enter email: ')
# # account_reset(user_id,number)
# aws(email,number)

# if __name__ == '__main__':
#     p1 = Process(target=account_details,args=('Brian4037',))
#     p1.start()
#     aws('Brian40@ruru.be','7578061215',p1)
# email_create('tony124')