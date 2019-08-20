#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

import time
import json
from video_play_aiqiyi import *

def t2s(t):
    if(str(t).count(":") == 2):
        h,m,s = t.strip().split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        m,s = t.strip().split(":")
        return int(m) * 60 + int(s)

url = input("url: ")
print("please choose definition: 1 1080pClient, 2 1080p, 3 720p, 4 GaoQing, 5 LiuChang, 6 JiSu")
qixidu = input("please input the num: ")
video_def = "GaoQing"
if(qixidu == 1):
    print("1080pClient")
    video_def = "1080pClient"
elif(qixidu == 2):
    print("1080p")
    video_def = "1080p"
elif(qixidu == 3):
    print("720p")
    video_def = "720p"
elif(qixidu == 4):
    print("GaoQing")
    video_def = "GaoQing"
elif(qixidu == 5):
    print("LiuChang")
    video_def = "LiuChang"
elif(qixidu == 6):
    print("JiSu")
    video_def = "JiSu"
else:
    print("error")

#driver = webdriver.Firefox(executable_path="./geckodriver")
driver = webdriver.Firefox(firefox_profile='./profile0808', executable_path="./geckodriver")


driver.implicitly_wait(30)#设置加载driver加载元素时所等待的最长的时间，
#driver.get("https://www.iqiyi.com/v_19rrdh6354.html")
driver.get(url)

print("successful operation\r\n")

print("waiting for the advertising\r\n")
time.sleep(40)
print("advertising is over\r\n")

driver.save_screenshot('error.png')
test_play = video_play_aiqiyi(driver)
test_play.play(video_def)

time.sleep(10)
during_second = t2s(driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/iqpdiv/iqpdiv[1]/iqpdiv[2]/iqpdiv/iqpdiv[4]/iqpdiv[1]/iqpdiv[2]/iqpspan[3]').get_attribute('textContent'))
print("the total time is %d second" % (during_second))
print("the video is playing......\r\n")

time.sleep(during_second - 20)
driver.save_screenshot('aiqiyi_test.png')

driver.close()
driver.quit()
print 'game over'
