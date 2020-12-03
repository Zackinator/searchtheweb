from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from decouple import config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Insert the chromedriver dir
webdriver1 = "C:/Users/zacka/Desktop/python/networkmonitor/reddit_automations/searchweb/chromedriver.exe"



class initiate(object):
    #method
    def searchweb(self):
        # the way to locate the button or thing you want on a website in chrome is
        # by pressing cmd + shift + c and then you can use your mouse to find the
        # info on the element that you want and you can copy the full xpath.
        "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        "C:/Users/zacka/Desktop/python/networkmonitor/reddit_automations/chromedriver.exe"
        options = webdriver.ChromeOptions()
        searchquery = input("Enter the search query please...\n")
        q = searchquery
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        #options.add_argument("--disable-extensions") # optional and off-topic, but it conveniently prevents the popup 'Disable developer mode extensions'
        # options.add_argument('--incognito')
        # options.add_argument('--headless')
        driver = webdriver.Chrome(webdriver1, chrome_options=options)
        #driver.maximize_window();
        action = ActionChains(driver)
        # doodlechome
        driver.get('https://www.google.com')
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='https://consent.google.com']")))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='introAgreeButton']"))).click()
        button = driver.find_element_by_name('q')
        button.click()
        button.send_keys(q)
        button.send_keys(Keys.RETURN)

        # cuckcuckgo
        driver = webdriver.Chrome(webdriver1)
        driver.get('https://www.duckduckgo.com')
        button = driver.find_element_by_name('q')
        button.click()
        button.send_keys(q)
        button.send_keys(Keys.RETURN)


        # bingbadabom
        driver = webdriver.Chrome(webdriver1, chrome_options=options)
        driver.get('https://www.bing.com')
        button = driver.find_element_by_name('q')
        button.click()
        button.send_keys(q)
        button.send_keys(Keys.RETURN)

        input("press ENTER to Exit")

    def searchwebtab(self):

        "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        options = webdriver.ChromeOptions()
        searchquery = input("Enter the search query please...\n")
        q = searchquery
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-extensions") # optional and off-topic, but it conveniently prevents the popup 'Disable developer mode extensions'
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        # options.add_argument('--incognito')
        # options.add_argument('--headless')
        driver = webdriver.Chrome(webdriver1, chrome_options=options)
        driver.maximize_window();
        action = ActionChains(driver)
        driver.get('https://www.google.com')
        # doodlechome
        window_before = driver.window_handles[0]
        print(window_before)
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='https://consent.google.com']")))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='introAgreeButton']"))).click()
        button = driver.find_element_by_name('q')
        button.click()
        button.send_keys(q)
        button.send_keys(Keys.RETURN)

        # cuckcuckgo website
        driver.execute_script("window.open('https://www.duckduckgo.com');")
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        source = driver.find_element_by_name('q')
        source.click()
        source.send_keys(q)
        source.send_keys(Keys.RETURN)

        # BIGNO website
        driver.execute_script("window.open('https://www.bing.com');")
        window_after = driver.window_handles[2]
        driver.switch_to_window(window_after)
        source = driver.find_element_by_name('q')
        source.click()
        source.send_keys(q)
        source.send_keys(Keys.RETURN)
        input('press ENTER to exit')

if __name__ in "__main__":
    print("Hello this is a application for using unbiased searchengines\n")
    print("\n1.Search in multiple tabs\n\n2.Search in multiple Windows\n")
    choice = input('\nEnter your Choice:> ')
    myObject = initiate()
    if choice == str(1):
        print("Choice 1")
        myObject.searchwebtab()
    elif choice == str(2):
        print("Choice 2")
        myObject.searchweb()
    else:
        print("No valid input provided...\n")
        print("Exiting")
