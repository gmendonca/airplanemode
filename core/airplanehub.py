from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'http://www.decolar.com/shop/flights/results/roundtrip/FLN/SAO/2016-08-01/2016-08-04/1/0/0/NA/NA/NA/NA/NA?from=SB'
driver = webdriver.Firefox()

driver.get(url)
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'flights-tab-airlinePricesMatrix')))

    print driver.title
finally:
    driver.quit()
