import time
from selenium import webdriver
import getpass
import sys

try:
    browser=webdriver.Chrome(r"C:\Users\djsam\Desktop\Files\Selenium_Drivers\chromedriver")
except:
    browser=webdriver.Firefox()

browser.maximize_window()
browser.implicitly_wait(20)
browser.get("https://www.instagram.com/")
time.sleep(1)

userID=input("Enter your Username \n")

login_username_Field=browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")
login_username_Field.send_keys(userID)

userPasscode=getpass.getpass(prompt="Enter your password \n")

login_passcode_Field=browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input")
login_passcode_Field.send_keys(userPasscode)

login_passcode_Field.submit()

time.sleep(2.5)

notifNOTNOW=browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm")
notifNOTNOW.click()

searchBar=browser.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input")

choice = 'N'

like_profile_handle=input("Enter the Instagram handle to like. \n")
choice=input(f"\nCONFIRM @{like_profile_handle}. Press Y to confirm. Press N to exit \n")
if(choice == 'Y'):
    browser.get(f"https://www.instagram.com/{like_profile_handle}")

    #time.sleep(2)
    total_posts=browser.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(1) > span > span")

    post_Opener=browser.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0")
    post_Opener.click()

    #time.sleep(0.7)
    i=0
    likeCounter=0
    alreadyLiked=0

    for i in range(int(total_posts.text)):

        #time.sleep(1.5)
        like_Button=browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg')
        if(browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg > path').value_of_css_property('fill') == 'rgb(237, 73, 86)'):
            print("\n \t Image already liked! \t \n")
            alreadyLiked+=1
        else:
            like_Button.click()
            likeCounter+=1
            time.sleep(0.1)

        if(i==(int(total_posts.text)-1)):
            pass
        else:
            next_button=browser.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow")
            next_button.click()

    print(f"\nTotal posts liked: {likeCounter} \n")
    print(f"Total posts liked previously: {alreadyLiked}")
    input()
else:
    sys.exit(0)