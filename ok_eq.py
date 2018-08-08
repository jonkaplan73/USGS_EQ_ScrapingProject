
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

#<svg class="leaflet-zoom-animated" width="766" height="694" viewBox="-63 -57 766 694" style="transform: translate3d(-63px, -57px, 0px);"><g><path stroke-linejoin="round" stroke-linecap="round" fill-rule="evenodd" pointer-events="none" stroke="#900" stroke-opacity="1" stroke-width="1" fill="#900" fill-opacity="0.4" d="M113 397L113 183L527 183L527 397z"></path></g></svg>


# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
csv_file = open('earthquakes.csv', 'w')
writer = csv.writer(csv_file)
header = {'header':['magnitude','label','time','depthinKM']}
writer.writerow(header['header'])

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://earthquake.usgs.gov/earthquakes/search/")
# Click review button to go to the review section
magnitude_button = driver.find_element_by_xpath('//label[@for="custom-mag"]')
magnitude_button .click()

minmagnitude = '3.5'

minMag = driver.find_element_by_xpath('//input[@name="minmagnitude"]')
minMag.clear()
minMag.send_keys(minmagnitude)

date_button = driver.find_element_by_xpath('//label[@for="basictime-custom"]')
date_button.click()


starttime = '1975-01-01 00:00:00'
endtime = '2018-01-01 00:00:00'

start = driver.find_element_by_xpath('//input[@name="starttime"]')
start.clear()
start.send_keys(starttime)

end = driver.find_element_by_xpath('//input[@name="endtime"]')
end.clear()
end.send_keys(endtime)

#WebElement.findElement(By.xpath('//input[@name="starttime"]')).sendKeys(starttime)
#WebElement.findElement(By.xpath('//input[@name="starttime"]')).sendKeys(endtime)


region_button = driver.find_element_by_xpath('//label[@for="basic-location-us"]')
region_button.click()

advanced_search_button = driver.find_element_by_xpath('//h2[@id="search-advanced"]')
advanced_search_button.click()

name="maxlatitude"

#37.1585	-94.298
#33.548	-103.0704
#Oklahoma Settings
maxlatitude = '37.2'
minlatitude = '33.5'
maxlongitude = '-94.2' #really max
minlongitude = '-103.1' #really min

maxLat = driver.find_element_by_xpath('//input[@name="maxlatitude"]')
maxLat.clear()
maxLat.send_keys(maxlatitude)

minLat = driver.find_element_by_xpath('//input[@name="minlatitude"]')
minLat.clear()
minLat.send_keys(minlatitude)

maxLong = driver.find_element_by_xpath('//input[@name="maxlongitude"]')
maxLong.clear()
maxLong.send_keys(maxlongitude)

minLong = driver.find_element_by_xpath('//input[@name="minlongitude"]')
minLong.clear()
minLong.send_keys(minlongitude)


search_button = driver.find_element_by_xpath('//button[@type="submit"]')
search_button.click()

#wait_button.until(EC.find_element_by_xpath('//button[@aria-label="Close Alert"]'))

wait_eqLoad = WebDriverWait(driver, 10)
medEarthquakes = wait_eqLoad.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="eq-list-item bigger"]')))
smallEarthquakes = wait_eqLoad.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="eq-list-item"]')))
earthquakes = smallEarthquakes + medEarthquakes

#earthquakes = driver.find_element_by_xpath('//div[@class="eq-list-item big"]')

for eq in earthquakes:
	eq_dict = {}
	magnitude = eq.find_element_by_xpath('.//span[@class="list-callout"]').text
	label = eq.find_element_by_xpath('.//h1[@class="list-header"]').text
	time = eq.find_element_by_xpath('.//h2[@class="list-subheader"]').text
	depthinKM = eq.find_element_by_xpath('.//aside[@class="list-aside"]').text

	#EQ_button = driver.find_element_by_xpath('//li[@class="list-view-item selected"]')
	#EQ_button.click()
	# eq.click()

	# longLat = driver.find_element_by_xpath('//dd[@class="location"]').text

	# closeEQ_button = driver.find_element_by_xpath('//button[@class="summary-close"]')
	# closeEQ_button.click()

	eq_dict['magnitude'] = magnitude
	eq_dict['label'] = label
	eq_dict['time'] = time
	eq_dict['depthinKM'] = depthinKM
	#eq_dict['longLat'] = longLat
	writer.writerow(eq_dict.values())
	print(label)


	#print('='*100)
	#print('label')
	#print(label)
	#print('magnitude ')
	#print(magnitude )
	#print('time')
	#print(time)
	#print('depthinKM')
	#print(depthinKM)
	#print('longLat')
	#print(longLat)
	#print('='*100)

# expected conditional
# wait until not - while loads earthquakes

#raise ValueError('A very specific bad thing happened.')

