from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv




# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
csv_file = open('earthquakesWorld3.csv', 'w')
writer = csv.writer(csv_file)
header = {'header':['magnitude','label','time','depthinKM','longLat','damageColor']}
writer.writerow(header['header'])

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://earthquake.usgs.gov/earthquakes/search/")
# Click review button to go to the review section
magnitude_button = driver.find_element_by_xpath('//label[@for="custom-mag"]')
magnitude_button .click()

minmagnitude = '5.6'

minMag = driver.find_element_by_xpath('//input[@name="minmagnitude"]')
minMag.clear()
minMag.send_keys(minmagnitude)


date_button = driver.find_element_by_xpath('//label[@for="basictime-custom"]')
date_button.click()


starttime = '2013-01-01 00:00:00'
endtime = '2017-12-31 23:59:59'

start = driver.find_element_by_xpath('//input[@name="starttime"]')
start.clear()
start.send_keys(starttime)

end = driver.find_element_by_xpath('//input[@name="endtime"]')
end.clear()
end.send_keys(endtime)

#WebElement.findElement(By.xpath('//input[@name="starttime"]')).sendKeys(starttime)
#WebElement.findElement(By.xpath('//input[@name="starttime"]')).sendKeys(endtime)


region_button = driver.find_element_by_xpath('//label[@for="basic-location-world"]')
region_button.click()


search_button = driver.find_element_by_xpath('//button[@type="submit"]')
search_button.click()

driver.implicitly_wait(5)

# continue_button = driver.find_element_by_xpath('//button')
# continue_button.click()

#wait_button.until(EC.find_element_by_xpath('//button[@aria-label="Close Alert"]'))
wait_eqLoad = WebDriverWait(driver, 10)

bigEarthquakes = wait_eqLoad.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="eq-list-item bigger"]')))

smallEarthquakes = wait_eqLoad.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="eq-list-item big"]')))

earthquakes = bigEarthquakes + smallEarthquakes

for eq in earthquakes:
	eq_dict = {}
	magnitude = eq.find_element_by_xpath('.//span[@class="list-callout"]').text
	label = eq.find_element_by_xpath('.//h1[@class="list-header"]').text
	time = eq.find_element_by_xpath('.//h2[@class="list-subheader"]').text
	depthinKM = eq.find_element_by_xpath('.//aside[@class="list-aside"]').text

	#EQ_button = driver.find_element_by_xpath('//li[@class="list-view-item selected"]')
	#EQ_button.click()
	eq.click()

	longLat = driver.find_element_by_xpath('//dd[@class="location"]').text



	damageColor ='NotAssigned'

	while True:
		try:
			damageColor = driver.find_element_by_xpath('//a[@title="PAGER estimated impact alert level"]').get_attribute("class")
			break
		except:
			break

	# if 	length(str(driver.find_element_by_xpath('//a[@title="PAGER estimated impact alert level"]'))) >4:
	# 	damageColor = driver.find_element_by_xpath('//a[@title="PAGER estimated impact alert level"]').get_attribute("class")
	# else:
	# 	damageColor ='NotAssigned'


	closeEQ_button = driver.find_element_by_xpath('//button[@class="summary-close"]')
	closeEQ_button.click()

	eq_dict['magnitude'] = magnitude
	eq_dict['label'] = label
	eq_dict['time'] = time
	eq_dict['depthinKM'] = depthinKM
	eq_dict['longLat'] = longLat
	eq_dict['damageColor'] = damageColor
	writer.writerow(eq_dict.values())


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

