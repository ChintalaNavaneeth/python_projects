from pytesseract import image_to_string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import pytesseract
import time


def login():
    driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
    driver.get("http://vtop2.vitap.ac.in:8070/vtop/initialProcess")

    q = driver.find_element_by_xpath("//*[@id='closedHTML']/div/div/div/div[2]/div/div/a").is_displayed()

    if q:
        driver.find_element_by_xpath("//*[@id='closedHTML']/div/div/div/div[2]/div/div/a").click()
        driver.find_element_by_xpath("//*[@id='page-wrapper']/div/div[1]/div[1]/div[3]/div/button").click()
        time.sleep(3)
        driver.find_element_by_id("uname").send_keys("18MIS7042")
        driver.find_element_by_xpath("//*[@id='passwd']").send_keys("navaneeth0404")
        element = driver.find_element_by_xpath("//*[@id='captchaRefresh']/div/img")  # find part of the page you want image of
        location = element.location
        size = element.size
        #driver.save_screenshot('screenshot.png')
        captcha_text = get_captcha_text(location, size)
        print(captcha_text)

    else:
        driver.find_element_by_xpath("//*[@id='uname']").send_keys("18MIS7042")
        driver.find_element_by_xpath("//*[@id='passwd']").send_keys("navaneeth0404")


def get_captcha_text(location, size):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Users/navan/PycharmProjects/selenium2/venv/Scripts/pytesseract'
    im = Image.open('screenshot.png')  # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')
    captcha_text = image_to_string(Image.open('screenshot.png'))
    return captcha_text


login()
