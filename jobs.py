import requests
from selenium import webdriver

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

def getscreenshot(url):
    driver = webdriver.PhantomJS(executable_path=r"/phantomjs/phantomjs/bin/phantomjs")
    driver.set_window_size(1024, 768) # optional
    driver.get('https://google.com/')
    driver.save_screenshot('screen.png') # save a screenshot to disk
    #sbtn = driver.find_element_by_css_selector('button.gbqfba')
    #sbtn.click()
