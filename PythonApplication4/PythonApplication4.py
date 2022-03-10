import time
from flask import Flask, jsonify, request
from statistics import mode
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

app = Flask(__name__)
#filtreleme için gerekli olan metotlar tanımlandı
def SearchWithinSec(locationdistance):
    Select(browser.find_element_by_xpath("//*[@id='location-distance']")).select_by_visible_text(str(locationdistance))
    return
def markaSec(marka): 
    Select(browser.find_element_by_xpath("//*[@id='make_select']")).select_by_visible_text(str(marka))
    return

def NewUsedSec(stocktype):
    Select(browser.find_element_by_xpath("//*[@id='stock-type-select']")).select_by_visible_text(str(stocktype))
    return

def MinYearSec(yearmin): 
    Select(browser.find_element_by_xpath("//*[@id='year_year_min_select']")).select_by_visible_text(str(yearmin))
    return

def MaxYearSec(yearmax): 
    Select(browser.find_element_by_xpath("//*[@id='year_year_max_select']")).select_by_visible_text(str(yearmax))
    return

def BodyStyleSec(bodyStyles):
    Bodies={
        "cargovan":"//*[@id='panel_body_styles']/div[1]/label",
        "convertible":"//*[@id='panel_body_styles']/div[2]/label",
        "coupe":"//*[@id='panel_body_styles']/div[3]/label",
        "hatchback":"//*[@id='panel_body_styles']/div[4]/label",
        "minivan":"//*[@id='panel_body_styles']/div[5]/label",
        "passengervan":"//*[@id='panel_body_styles']/div[6]/label",
        "pickuptruct":"//*[@id='panel_body_styles']/div[7]/label",
        "suv":"//*[@id='panel_body_styles']/div[8]/label",
        "sedan":"//*[@id='panel_body_styles']/div[9]/label",
        "wagon":"//*[@id='panel_body_styles']/div[10]/label"}
    browser.find_element_by_id("trigger_body_styles").click()
    time.sleep(3)
    for i in range(0,len(bodyStyles)):
        (browser.find_element_by_xpath(Bodies[bodyStyles[i].lower()])).click()
        time.sleep(3)
        browser.find_element_by_id("trigger_body_styles").click()
    return

def CapTypeSec(capTypes):
    captype={
        "crew":"//*[@id='panel_cab_types']/div[1]/label",
        "extended":"//*[@id='panel_cab_types']/div[2]/label",
        "regular":"//*[@id='panel_cab_types']/div[3]/label"} 
    browser.find_element_by_id("trigger_cab_types").click()
    time.sleep(3)
    for i in range(0,len(capTypes)):
        (browser.find_element_by_xpath(captype[capTypes[i].lower()])).click()
        time.sleep(3)
        browser.find_element_by_id("trigger_cab_types").click()
    return

def exteriorColorSec(color):
    Colors = {
        "beige": "//*[@id='panel_exterior_colors']/div[1]/label", 
        "black": "//*[@id='panel_exterior_colors']/div[2]/label",
        "blue": "//*[@id='panel_exterior_colors']/div[3]/label",
        "brown": "//*[@id='panel_exterior_colors']/div[4]/label",
        "gold": "//*[@id='panel_exterior_colors']/div[5]/label",
        "gray": "//*[@id='panel_exterior_colors']/div[6]/label",
        "green": "//*[@id='panel_exterior_colors']/div[7]/label",
        "orange": "//*[@id='panel_exterior_colors']/div[8]/label",
        "purple": "//*[@id='panel_exterior_colors']/div[9]/label",
        "red": "//*[@id='panel_exterior_colors']/div[10]/label",
        "silver": "//*[@id='panel_exterior_colors']/div[11]/label",
        "white": "//*[@id='panel_exterior_colors']/div[12]/label",
        "yellow": "//*[@id='panel_exterior_colors']/div[13]/label"}
    browser.find_element_by_id("trigger_exterior_colors").click()     
    time.sleep(3)
    for i in range(0,len(color)):
        (browser.find_element_by_xpath(Colors[color[i].lower()])).click()
        time.sleep(3)    
    browser.find_element_by_id("trigger_exterior_colors").click()
    return

def transmissionSec(trans):
    Transmissions = {
        "automanual": "//*[@id='panel_transmissions']/div[1]/label", 
        "automatic": "//*[@id='panel_transmissions']/div[2]/label", 
        "cvt": "//*[@id='panel_transmissions']/div[3]/label", 
        "manual": "//*[@id='panel_transmissions']/div[4]/label", 
        "unknown": "//*[@id='panel_transmissions']/div[5]/label"}
    browser.find_element_by_id("trigger_transmissions").click()     
    time.sleep(3) 
    for i in range(0,len(trans)):
        (browser.find_element_by_xpath(Transmissions[trans[i].lower()])).click()
        time.sleep(3)    
    browser.find_element_by_id("trigger_transmissions").click()
    return

def driveTrainSec(drivetrains):
    Transmissions = {
        "allwheel": "//*[@id='panel_drivetrains']/div[1]/label", 
        "fourwheel": "//*[@id='panel_drivetrains']/div[2]/label", 
        "frontwheel": "//*[@id='panel_drivetrains']/div[3]/label", 
        "rearwheel": "//*[@id='panel_drivetrains']/div[4]/label"}
    browser.find_element_by_id("trigger_drivetrains").click()     
    time.sleep(3) 
    for i in range(0,len(drivetrains)):
        (browser.find_element_by_xpath(Transmissions[drivetrains[i].lower()])).click()
        time.sleep(3)    
    browser.find_element_by_id("trigger_drivetrains").click()
    return

# drop down listten 50 seçeneği seçtilerek 50 araç listelenmesi sağlandı
def listele():
    Select(browser.find_element_by_xpath("//*[@id='pagination-dropdown']")).select_by_visible_text(
        "50 results per page")
    return

browser=webdriver.Chrome("C:\\Users\\MONSTER\\chromedriver_win32\\chromedriver.exe") 
browser.get("https://www.cars.com/for-sale/searchresults.action")
listele()



#route /list olarak belirlendi
@app.route("/list")
def jsonDonustur():
    #gelen request parametresi eğer boş değil ise ilgili metot çağrılıyor
    colorList = list(request.args.getlist("extcolor"))
    if colorList is not None:
        exteriorColorSec(colorList)
        time.sleep(3)
        
    bodyList=list(request.args.getlist("bodystyle"))
    if bodyList is not None:
        BodyStyleSec(bodyList)
        time.sleep(3)

    capTypeList=list(request.args.getlist("captype"))
    if capTypeList is not None:
        CapTypeSec(capTypeList)
        time.sleep(3)
   
    transmissionList=list(request.args.getlist("trans"))
    if transmissionList is not None:
        transmissionSec(transmissionList)
        time.sleep(3)
        
    driveTrainList=list(request.args.getlist("drivetrain"))
    if driveTrainList is not None:
        driveTrainSec(driveTrainList)
        time.sleep(3)
    
    markaList=request.args.get("brand")
    if markaList is not None:
        markaSec(markaList)
        time.sleep(3)
  
    newUsedList=request.args.get("newused")
    if newUsedList is not None:
        NewUsedSec(newUsedList)
        time.sleep(3)

    searchWithinList=request.args.get("searchwithin")
    if searchWithinList is not None:
        SearchWithinSec(searchWithinList)
        time.sleep(3)
    
    minYearList=request.args.get("minyear")
    if minYearList is not None:
        MinYearSec(minYearList)
        time.sleep(3) 
    
    maxYearList=request.args.get("maxyear")
    if maxYearList is not None:
        MaxYearSec(maxYearList)
        time.sleep(3)
    
    result=dict()
    result["cars"]=[]
    for x in range(1):
        car = dict()
        browser.find_element(by=By.CLASS_NAME,value="vehicle-card-link").click()
        time.sleep(2)
        car["title"]=browser.find_element_by_xpath("//*[@id='ae-main-content']/div[5]/section/header/div[1]/h1").text
        car["price"]=browser.find_element_by_xpath("//*[@id='ae-main-content']/div[5]/section/header/div[2]/span").text
        car["extcolor"]=browser.find_element_by_xpath("//*[@id='ae-main-content']/div[5]/div[2]/section[1]/dl/dd[1]").text
        car["transmission"]=browser.find_element_by_xpath("//*[@id='ae-main-content']/div[5]/div[2]/section[1]/dl/dd[6]").text
        result["cars"].append(car)
        return result
    return json.dumps(result) #json çıktısı


if  __name__ == "__main__":
    app.run()
