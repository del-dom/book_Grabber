from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


url = "https://www.packtpub.com/packt/offers/free-learning"

username = ''  # YOUR USERNAME
password = ''  # YOUR PASSWORD
X_Y_Offset = 500
# ^ Helps in clearing content-overlay may need to be
# adjusted for screan size as it is in pixels.

browser = webdriver.Firefox()
browser.get(url)

browser.find_element_by_xpath("//div[(@id='account-bar-login-register')]/a[(@class='login-popup')]/div[(@class='float-left')]").click()

sleep(1)

browser.find_element_by_xpath("//div[(@id='account-bar')]/div[(@class='section-inner')]/div[(@id='account-bar-form')]/div[(@id='account-bar-form-login')]/div[(@class='account-bar-form-left')]/form[(@id='packt-user-login-form')]/div/div[(@id='login-form')]/div[(@id='login-form-email')]/div[(@id='email-wrapper')]/input[(@id='email')]").send_keys(username)

browser.find_element_by_xpath("//div[(@id='account-bar')]/div[(@class='section-inner')]/div[(@id='account-bar-form')]/div[(@id='account-bar-form-login')]/div[(@class='account-bar-form-left')]/form[(@id='packt-user-login-form')]/div/div[(@id='login-form')]/div[(@id='login-form-pass')]/div[(@id='password-wrapper')]/input[(@id='password')]").send_keys(password)


# .send_keys(username)
browser.find_element_by_xpath("//div[(@id='account-bar')]/div[(@class='section-inner')]/div[(@id='account-bar-form')]/div[(@id='account-bar-form-login')]/div[(@class='account-bar-form-left')]/form[(@id='packt-user-login-form')]/div/div[(@id='login-form')]/div[(@id='login-form-submit')]/input[(@id='edit-submit-1')]").click()

sleep(2)  # gives time for the browser to login

action = ActionChains(browser)
el = browser.find_element_by_xpath("//div[(@id='content-overlay')]")
if el.is_displayed():
    action.move_to_element_with_offset(el, X_Y_Offset, X_Y_Offset)
    action.click()
    action.perform()



sleep(2)  # gives time for the overlay to clear
browser.find_element_by_xpath("//div[(@id='deal-of-the-day')]/div[(@class='dotd-main-book cf')]/div[(@class='section-inner')]/div[(@class='dotd-main-book-summary float-left')]/div[(@class='dotd-main-book-form cf')]/div[(@class='float-left free-ebook')]/a[(@class='twelve-days-claim')]/div[(@class='book-claim-token-inner')]/input[(@class='form-submit')]").click()


'''
for form in browser.forms():
    if form.attrs['id'] == 'packt-user-login-form':
        browser.form = form
        break
print browser.form
browser['email'] = username
browser['password'] = password
result = browser.submit
print result
print browser
# browser.open()
# html = res.read()
# print res

//div[(@id='account-bar-login-register')/a[(@class='login-popup')]/div[(@class='float-left')]'''