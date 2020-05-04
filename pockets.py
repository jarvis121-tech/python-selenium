import requests
import json
import names
import random
from ws import account_reset,email_create
from multiprocessing import Process,Value,Array,Manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.firefox.options import Options
import warnings
warnings.filterwarnings("ignore")
from python3_anticaptcha import ImageToTextTask
from faker import Faker
from bs4 import BeautifulSoup as bs


ANTICAPTCHA_KEY = "84134679af5a11cf217094d30105e186"



firstName = 'Harish'
email_id = 'sharmaharish1928@gmail.com'
phone_number = '8723993584'
cnumber = '4336620200424762'
expMonth = '03'
expYear = '25'
cvc = '414'
user_id = 'Lenniel5896'
os.environ['reset'] = 'Nrrs4247@'
RESET_PSWD = os.environ['reset']


def runtime_script(driver,script):
    driver.execute_script(script)


def generate_address():
    page =requests.get("https://www.fakeaddressgenerator.com/World_more/India_address_generator")
    soup = bs(page.content,'html.parser')
    inputs = soup.find_all('input',class_="no-style")
    return {'street': str(inputs[5].get("value")),
            'city': str(inputs[6].get("value")),
            'state':str(inputs[7].get("value")),
            'pincode':str(inputs[8].get("value")), }


def main():
    global email_id
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'x-wl-app-version': '1.0',
        'Accept-Language': 'en_IN',
        'x-wl-platform-version': '6.2.0.00.20140915-1601',
         'x-wl-analytics-tracking-id': 'f0ebc733-df51-4663-a0d0-e40a6b684435',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'digitalbank.icicibank.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'WLNativeAPI(shamu; greatlteks-user 5.1.1 NMF26X 500200323 release-keys; SM-N950N; SDK 22; Android 5.1.1)',
    }

    data = {
        'action':'test',
        'AjaxRequest':'true',
        'x': '0.28853674565953004'
    }

    r = requests.post('https://digitalbank.icicibank.com/wlsdigi62/apps/services/api/wlsdigi62/android/init',headers=headers,data=data,verify=False)
    if r.status_code != 401:
        print(r.status_code)
        print("Response unsucessfull")
        print(r.content)
        exit()
    # print(r.status_code)
    # print(r.content)

    jsonString = str(r.content).split('\\n')[1].split('*')[0]
    responseDict = json.loads(jsonString)

    instance_id = responseDict['challenges']['wl_antiXSRFRealm']['WL-Instance-Id']
    token = responseDict['challenges']['wl_deviceNoProvisioningRealm']['token']

    # print(instance_id)
    # print(token)
    # print(r.headers)

    session_id = r.headers['Set-Cookie'].split(';')[0].split('=')[1]
    persistent = r.headers['Set-Cookie'].split(';')[2].split('=')[1]

    # print(session_id)
    # print(persistent)
    Cookie = 'WL_PERSISTENT_COOKIE=' + str(persistent) + ';WLJSESSIONID=' + str(session_id) + ';'
    # print(Cookie)

    headers['Cookie'] = Cookie
    headers['WL-Instance-Id'] = str(instance_id)
    formHeaders = headers.copy()
    headers['Authorization'] = '{"wl_deviceNoProvisioningRealm":{"ID":{"app":{"id":"wlsdigi62","version":"1.0"},"device":{"id":"5fd4d342-567e-3c0e-9cfb-1cf0ad071292","os":"5.1.1","model":"SM-N950N","environment":"Android"},"token":\"' +str(token) +'\"}}}'
    # print(headers['Authorization'])

    headers['Cookie2'] = '$Version=1'

    data['x'] = '0.7972757092102044'
    # headers['Content-Length'] = '51'
    r = requests.post('https://digitalbank.icicibank.com/wlsdigi62/apps/services/api/wlsdigi62/android/init',headers=headers,data=data,verify=False)

    # print(r.status_code)
    # print(r.content)
    if r.status_code != 200:
        print("Response unsucessfull")
        print(r.content)
        exit()

    formHeaders['x-wl-app-version'] =  '1.0'
    formHeaders['x-wl-app-details'] = '{"applicationDetails":{"platformVersion":"6.2.0.00.20140825-1637","nativeVersion":"3340478406","skinName":"","skinChecksum":1088150931}}'
    formHeaders['x-wl-device-id'] = '5fd4d342-567e-3c0e-9cfb-1cf0ad071292'
    formHeaders['User-Agent'] = 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N950N Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36/Worklight/6.2.0.00.20140915-1601'

    global phone_number
    phone_number = str(input("Please enter number: "))
    email_id = 'rjsharma07@ruru.be'

    formData = {
        'adapter': 'Registration',
        'procedure' : 'POCRIBMOB01',
        'parameters' : '[{"OPERATIONID":"POCRIBMOB01","MOBILENO":"' +str(phone_number)+ '","EMAIL":"' + str(email_id) +'","DEVICEID":"a4c3f09ed6bc8343","MACADDRESS":"A4:C3:F0:9E:D6:BC","DEVICETYPE":"android","IMEI":"351564840821417"}]',
        '__wl_deviceCtx' : 'AYtn1wl41-ykuBAA',
        'isAjaxRequest' : 'true',
        'x' : '0.7262695812595399',
        'compressResponse' : '',
    }

    nameForm_request = requests.post('https://digitalbank.icicibank.com/wlsdigi62/apps/services/api/wlsdigi62/android/query',data=formData,headers=formHeaders,verify=False)

    #
    # # print(nameForm_request.status_code)
    # print(nameForm_request.content)
    namFormDict = json.loads(str(str(nameForm_request.content).split("\\n")[1].split("*")[0]))
    mobileStatusCode = int(namFormDict.get('MB').get('RS').get('STATUSCODE'))
    if mobileStatusCode == 10:
        print("Mobile Already Registered,Sorry Try again")
        print("Exiting Program")
        exit()
    # if nameForm_request.status_code != 200:
    #     print("Response unsucessfull")
    #     print(nameForm_request.content)
    #     exit()
    #
    # formData['procedure'] = 'POCREGUR01'
    # formData['parameters'] = '[{"OPERATIONID":"POCURSTLST01","CITY":"","PINCODE":"400080"}]'
    #
    #
    # cityForm_request = requests.post('https://digitalbank.icicibank.com/wlsdigi62/apps/services/api/wlsdigi62/android/query',data=formData,headers=formHeaders,verify=False)
    # # print(cityForm_request.status_code)
    # print(cityForm_request.content)
    # if cityForm_request.status_code != 200:
    #     print("Response unsucessfull")
    #     print(cityForm_request.content)
    #     exit()
    # formData['procedure'] = 'POCRIBOTP01'
    # formData['parameters'] = '[{"OPERATIONID":"POCRIBOTP01","MOBILENO":"'+ str(phone_number) + '"}]'
    #
    # otpForm_request = requests.post('https://digitalbank.icicibank.com/wlsdigi62/apps/services/api/wlsdigi62/android/query',data=formData,headers=formHeaders,verify=False)
    #
    # # print(otpForm_request.status_code)
    # print(otpForm_request.content)
    # if otpForm_request.status_code != 200:
    #     print("Response unsucessfull")
    #     print(r.content)
    #     exit()
    # while True:
    #     otp=str(input("Please enter otp: "))
    #     formData['procedure'] = 'POCRIBOTP02'
    #     formData['parameters'] = '[{"OPERATIONID":"POCRIBOTP01","MOBILENO":"'+ str(phone_number) + '"' + ',"OTP":"' + str(otp) + '"}]'
    #
    #     otpsent_request = requests.post('https://digitalbank.icicibank.com/wlsdigi62/apps/services/api/wlsdigi62/android/query',data=formData,headers=formHeaders,verify=False)
    #     if otpsent_request.status_code != 200:
    #         print("Response unsucessfull")
    #         print(r.content)
    #         exit()
    #     # print(otpsent_request.status_code)
    #     print(otpsent_request.content)
    #
    #     otpDict = json.loads(str(str(otpsent_request.content).split("\\n")[1].split("*")[0]))
    #     otpStatusCode = int(otpDict.get('MB').get('RS').get('STATUSCODE'))
    #     if otpStatusCode == 0:
    #         print("Correct Otp")
    #         break
    #     elif otpStatusCode == 1:
    #         print("Wrong Otp")
    global firstName



    while True:
        firstName = names.get_first_name()
        randnumber = random.randint(1000,9999)
        customerId = str(firstName) + str(firstName[0].lower())+str(randnumber)
        formData['procedure'] = 'POCREGUN01'
        formData['parameters'] = '[{"OPERATIONID":"POCREGUN01","CUSTOMER_USERNAME":"' + str(customerId) + '","CUSTOMER_PASSWORD":"nrrs4247","CUSTOMER_REPASSWORD":"nrrs4247","CUSTOMER_NAME":"' + str(firstName) +'","CUSTOMER_LASTNAME":"Sharma","CUSTOMER_DOB":"01/04/1985","CUSTOMER_MOBILE":"' + str(phone_number)+'","CUSTOMER_EMAIL":"' + str(Faker().email()) +'","CUSTOMER_GENDER":"m","CUSTOMER_ADDRESS1":"Mulund","CUSTOMER_ADDRESS2":"","CUSTOMER_CITY":"MUMBAI","CITYCODE":"2847","CUSTOMER_STATE":"MAHARASHTRA","STATECODE":"23","CUSTOMER_PINCODE":"400080","CUSTOMER_NATIONALITY":"IND","DEVICEID":"a4c3f09ed6bc8343","MACADDRESS":"A4:C3:F0:9E:D6:BC","DEVICETYPE":"android","IMEI":"351564840821417"}]'
        # print(formData['parameters'])
        regsent_request = requests.post('https://digitalbank.icicibank.com/wlsdigi62/apps/services/api/wlsdigi62/android/query',data=formData, headers=formHeaders, verify=False)
        if regsent_request.status_code != 200:
            print("Response unsucessfull")
            print(r.content)
            exit()
        # print(regsent_request.status_code)
        print(str(regsent_request.content))
        with open("regDict.txt","w") as outfile:
            outfile.write(str(regsent_request.content))
        regDict = json.loads(str(str(regsent_request.content).split("\\n")[1].split("*")[0]))
        print(regDict)
        regStatusCode = int(regDict.get('MB').get('RS').get('STATUSCODE'))
        print(regStatusCode)
        if regStatusCode == 0:
            print("Registration Completed")
            print("First Name " + firstName)
            print("Customer Id: " + customerId)
            email_id = customerId + "@ruru.be"
            with open("pocketsaccount.txt","a") as outfile:
                outfile.write(str(customerId) + ":" + str(phone_number) + "\n")
            break
        else:

            print("Registration unsuccesful")
            print(regDict.get('MB').get('RS').get('MESSAGE'))
            print("Trying again")
            time.sleep(5)

    final_user_id = regDict['MB']['RQ']['CUSTOMER_USERNAME']
    final_mobile_number = regDict['MB']['RQ']['CUSTOMER_MOBILE']
    print("Reset Password Process Begin")
    account_reset(final_user_id,final_mobile_number)
    print("Password reset Completed")
    global user_id
    user_id = final_user_id

def account_details(userId,return_dict):
    # global driver
    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('--headless')
    # driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chromeOptions)
    # driver.get('https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI')
    while True:
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            # driver = webdriver.Chrome()
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
            optionValue = 1
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
                if optionValue ==1:
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
                            optionValue = 2
            # time.sleep(5)
            # # if optionValue == 2:
            # #     my_accounts.click()
            # #     pockets_acnt = WebDriverWait(driver,10).until(
            # #         EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[2]/div/div/div/div/ul/li[2]/ul/li[8]/a'))
            # #     )
            # #     pockets_acnt.click()
            # # elif optionValue == 1:
            # #     try:
            # #
            # #         # showMeAround = WebDriverWait(driver, 10).until(
            # #         #     EC.presence_of_element_located(
            # #         #         (By.XPATH, '/html/body/form/div[1]/div[5]/div/div[4]/div[3]/div/div[1]/a'))
            # #         # ).click()
            # #         # exitButton = WebDriverWait(driver, 10).until(
            # #         #     EC.presence_of_element_located(
            # #         #         (By.XPATH, ('/html/body/form/div[1]/div[5]/div/div[4]/div[3]/div/div[3]/div/a[1]')))
            # #         # ).click()
            # #     except Exception as e:
            # #         print(e)
            # #         pass
            # #         # my_accounts = WebDriverWait(driver, 10).until(
            #         #     EC.presence_of_element_located(
            #         #         (By.XPATH, '/html/body/form/div[1]/div[4]/div/div/div[3]/div[1]/div/div/div/ul/li[2]/a/div[1]/p'))
            #         # ).click()
            #         # pocketsClick = WebDriverWait(driver, 10).until(
            #         #     EC.presence_of_element_located(
            #         #         (By.XPATH, '/html/body/form/div[1]/div[4]/div/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div/a[8]'))
            #         # ).click()
            with open("jquery-3.4.1.min.js",errors='ignore') as f:
                driver.execute_script(f.read())
            # # while True:
            # #     try:
            # #         print("inside second try")
            # #         driver.execute_script("document.getElementById('Pockets').click()")
            # #     except:
            # #         pass
            # #     else:
            # #         break
                driver.execute_script('$( document ).ready(function() {document.getElementById("Pockets").click();});')
            cardNumber_element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[3]/div[1]/div[6]/div[2]/div/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr[3]/td[2]/a'))
            )
            cardNumber =cardNumber_element.text
            # # view_card_details = WebDriverWait(driver,10).until(
            # #     EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div[3]/div[1]/div[6]/div[1]/div[2]/div[16]/a[3]'))
            # # )
            # # view_card_details.click()
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
            cnumber = cardNumber
            expMonth = expiryDate.split('/')[0]
            expYear = expiryDate.split('/')[1]
            cvc = cvv

            return_dict[str('cnumber')] = str(cnumber)
            return_dict['expMonth'] = str(expMonth)
            return_dict['expYear'] = str(expYear)
            return_dict['cvc'] = str(cvc)
            driver.quit()
            break
        except Exception as e:
            print(f"Exception Occured {e}")
            driver.quit()
    # return {
    #     'ccnumber':cardNumber,
    #     'expMonth':expMonth,
    #     'expYear':expYear,
    #     'cvc':cvv
    # }



def aws(firstName,emailId,number,proc,return_dict):
    # global driver
    global cnumber
    global expMonth
    global expYear
    global cvc
    addressDict = generate_address()
    while True:
        try:
            options = Options()
            # options.headless = True
            driver = webdriver.Firefox(options=options)

            # chromeOptions = webdriver.ChromeOptions()
            # chromeOptions.add_argument('--incognito')
            # driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chromeOptions)
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
                EC.element_to_be_clickable((By.ID,'personal-account'))
            )
            personal.click()
            phoneNumber = driver.find_element_by_id('phone-number')
            phoneNumber.send_keys(number)
            country = WebDriverWait(driver,10).until(
                EC.element_to_be_clickable('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[4]/select')
            )
            # country = driver.find_element_by_xpath()
            country.click()
            country_choose = WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[4]/select/option[102]'))
            )
            # country_choose = driver.find_element_by_xpat('')
            country_choose.click()
            adress = driver.find_element_by_id('street-address-1')
            adress.send_keys(addressDict['street'])
            city = driver.find_element_by_id('city')
            city.send_keys(addressDict['city'])
            state = driver.find_element_by_id('state')
            state.send_keys(addressDict['state'])
            postal_code = driver.find_element_by_id('postal-code')
            postal_code.send_keys(addressDict['pincode'])
            agree = WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/agreement/div/div[2]/input'))
            )
            # agree = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/agreement/div/div[2]/input')
            agree.click()
            account_create = WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/button/span/input'))
            )
            # account_create = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/button/span/input')
            account_create.click()
            proc.join()
            ccnumber = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,'addCreditCardNumber'))
            )
            ccnumber.send_keys(return_dict['cnumber'])
            WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.ID,'expirationMonth'))
            )
            select = Select(driver.find_element_by_id('expirationMonth'))
            select.select_by_value(str(int(return_dict['expMonth']) - 1))
            select_year = Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/sup-credit-card-input/div/div[2]/div/select[2]'))
            select_year.select_by_visible_text('20' +str(expYear))
            cvc_number = driver.find_element_by_id('cvc')
            cvc_number.send_keys(return_dict['cvc'])
            acntName = driver.find_element_by_id('accountHolderName')
            acntName.send_keys(firstName)
            pan_no = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/span/span/div/div/label[2]/input')
            pan_no.click()
            verify = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/button/span/span[1]')
            choice = input("Verify(y/n")
            if choice == "n":
                break
            verify.click()
            otpTransact = WebDriverWait(driver,60).until(
                EC.presence_of_element_located((By.ID,'txtAutoOtp'))
            )
            otpt = input("Enter otp for transaction:")
            otpTransact.send_keys(otpt)
            time.sleep(2)
            WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/form/div/div/div/div/div/div[3]/div[15]/div/div[1]/input'))
            ).click()
            textSelect = WebDriverWait(driver,60).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/label[1]/input'))
            )
            textSelect.click()
            WebDriverWait(driver,20).until(
                EC.presence_of_element_located((By.ID,'phoneNumber'))
            ).send_keys(phone_number)
            # driver.find_element_by_id('').send_keys(phone_number)
            # p2.join()
            imgLink = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,'imageCaptcha'))
            ).get_attribute("ng-src")
            print("Solving Captcha")
            user_answer = ImageToTextTask.ImageToTextTask(anticaptcha_key=ANTICAPTCHA_KEY). \
                captcha_handler(captcha_link=imgLink)
            print(user_answer)
            if int(user_answer['errorId']) == 0:
                captchaAnswer = str(user_answer['solution']['text'])
            else:
                print("Captcha Not Solved")
            WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,'guess'))
            ).send_keys(captchaAnswer)
            WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/button/div[1]/span/input'))
            ).click()
            while True:
                final_otp = input("Please enter otp: ")
                if final_otp == "resend":
                    # WebDriverWait(driver,10).until(
                    #     EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/span/span/a'))
                    # ).click()
                    script = input("Please enter runtime execution script")
                    runtime_script(driver,script)
                    time.sleep(2)
                    while True:
                        try:
                            a = driver.switch_to.alert()
                            a.accept()
                            break
                        except:
                            print("Alert not found")
                            time.sleep(1)
                        textSelect = WebDriverWait(driver, 60).until(
                            EC.element_to_be_clickable((By.XPATH,
                                                        '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/label[1]/input'))
                        )
                        textSelect.click()
                        WebDriverWait(driver,10).until(
                            EC.element_to_be_clickable((By.ID,'countryCode'))
                        )
                        select = Select(driver.find_element_by_id('countryCode'))
                        select.select_by_value("101")
                        WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.ID, 'phoneNumber'))
                        ).send_keys(phone_number)
                        imgLink = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.ID, 'imageCaptcha'))
                        ).get_attribute("ng-src")
                        print("Solving Captcha")
                        user_answer = ImageToTextTask.ImageToTextTask(anticaptcha_key=ANTICAPTCHA_KEY). \
                            captcha_handler(captcha_link=imgLink)
                        print(user_answer)
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.ID, 'guess'))
                        ).send_keys(user_answer)
                        WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH,
                                                        '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/button/div[1]/span/input'))
                        ).click()

                else:
                    WebDriverWait(driver,10).until(
                        EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/input'))
                    ).send_keys(final_otp)
                    time.sleep(2)
                    driver.execute_script("document.getElementsByClassName('sms-verify-btn')[0].children[0].click()")
                    time.sleep(1)
                    driver.execute_script("document.getElementsByClassName('a-button-text')[3].click()")
                    time.sleep(1)
                    driver.execute_script("document.getElementsByClassName('a-button-input')[0].click()")
                    WebDriverWait(driver,10).until(
                        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/section/div/div[2]/div/div/div/div/form/fieldset/div/div[3]/div/div/div/div/span'))
                    )
                    driver.execute_script("document.querySelector('#aws-element-e325bdc6-4088-4113-bde9-ad2c6411b8ce > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(8)')")
                    driver.execute_script("document.querySelector('#aws-element-3f5165f1-815e-4d9e-aff3-dced5594974f > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(8)').click()")
                    WebDriverWait(driver,10).until(
                        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/section/div/div[2]/div/div/div/div/form/fieldset/div/div[6]/div/div/div/div/button'))
                    ).click()
                    WebDriverWait(driver,10).until(
                        EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/section/div/div[2]/div/div/div/div/div/div/div/div/div/div/h1/a'))
                    )
                    WebDriverWait(driver,10).until(
                        EC.element_to_be_clickable((By.XPATH,'//*[@id="aws-element-button-0f3b8a22-a00a-4b4b-8be8-274a07524883"]'))
                    ).click()
                    print("Account Created")
                    if input("Do you want to exit: ") == "y":
                        break


            break
        except Exception as e:
            print(f"Exception occured {e}")
            createChoice = input("Want to create another driver(y/n")
            if createChoice == "y":
                while True:
                    newNumber = random.randint(1000,9999)
                    if newNumber != int(email_id.split(firstName + firstName[0].lower())[1].split("@")[0]):
                        emailId = f"{firstName}{newNumber}@ruru.be"
                        # p2.join()
                        # p2 = Process(target=email_create,args=(emailId,))
                        # p2.start()
                        break
                    else:
                        continue

            # driver.quit()


if __name__ == "__main__":
    main()
    # account_reset(user_id,phone_number)
    manager = Manager()
    return_dict = manager.dict()
    # return_dict.append({})
    p1 = Process(target=account_details,args=(user_id,return_dict))
    # p2= Process(target=email_create,args=(email_id,))
    p1.start()
    # p2.start()
    # p1.join()
    # print(return_dict)
    aws(firstName,email_id,phone_number,p1,return_dict)