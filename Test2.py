from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def testFunc():
    pair = 'GBPJPY'
    # todo: use short xpath

    pairXpath = '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div/div'
    intervalXpath = '//*[@id="header-toolbar-intervals"]/div/div/div'
    wantedIntervalXpath = '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[12]/div/div[1]/div'
    openCandle = '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]'
    highCandle = '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]'
    lowCandle = '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[2]'
    closeCandle = '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[5]/div[2]'
    
   

    driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver.exe")
    driver.get('https://www.tradingview.com/chart')
    driver.fullscreen_window()
    # element=driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]')

    element = driver.find_element_by_xpath(pairXpath)
    print(element.get_attribute('innerHTML'))
    element.click()

    inputElement = driver.find_element_by_xpath(
        '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input')
    inputElement.send_keys(pair)

    driver.implicitly_wait(2)
    choosePair = driver.find_element_by_xpath(
        '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[4]/div/div/div[3]/div[1]/div[2]/div/span/em')
    choosePair.click()

    durationElement = driver.find_element_by_xpath(intervalXpath)
    durationElement.click()

    driver.find_element_by_xpath(wantedIntervalXpath).click()
    print(driver.find_element_by_xpath(intervalXpath).get_attribute('innerHTML'))

    durationElement.click()

    driver.find_element_by_xpath(wantedIntervalXpath).click()



    # driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[4]/div/div/div[3]/div[1]/div[2]/div/span/emq')
    coordinates = driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/canvas[2]").location
    print(coordinates)
    el = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/canvas[2]")
    action = ActionChains(driver)

    lastElementList=[0,0,0,0]
    memoryElement=[]
    elementList=[]
    offsetX=0
    count=0

    for i in range(290):
        count+=1
        action.move_to_element_with_offset(el, offsetX, 550)
        action.perform()
        print(driver.find_element_by_xpath(openCandle).get_attribute('innerHTML'))

        print(element.get_attribute('innerHTML'))
        candleValue=driver.find_element_by_xpath(openCandle).get_attribute('innerHTML')
        print(candleValue)
        intcandleValue=float(candleValue)

        memoryElement.append(intcandleValue)

        print(driver.find_element_by_xpath(highCandle).get_attribute('innerHTML'))
        print(element.get_attribute('innerHTML'))
        candleValue=driver.find_element_by_xpath(highCandle).get_attribute('innerHTML')
        intcandleValue=float(candleValue)

        memoryElement.append(intcandleValue)

        print(driver.find_element_by_xpath(lowCandle).get_attribute('innerHTML'))
        print(element.get_attribute('innerHTML'))
        candleValue=driver.find_element_by_xpath(lowCandle).get_attribute('innerHTML')
        intcandleValue=float(candleValue)

        memoryElement.append(intcandleValue)

        print(driver.find_element_by_xpath(closeCandle).get_attribute('innerHTML'))
        print(element.get_attribute('innerHTML'))
        candleValue=driver.find_element_by_xpath(closeCandle).get_attribute('innerHTML')
        intcandleValue=float(candleValue)

        memoryElement.append(intcandleValue)

        if memoryElement == lastElementList:
            pass
        else:
            elementList.append(memoryElement)
            lastElementList==memoryElement
            memoryElement=[]

        offsetX+=5
        print(count)
    print(elementList)
    print(len(elementList))
    csv_document = open('./csv_files/test2.csv', 'w')
    writer = csv.writer(csv_document)
    print(elementList[1])
   
    for i in range(len(elementList)):
        writer.writerow(elementList[i])

