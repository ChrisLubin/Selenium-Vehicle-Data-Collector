import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import os

driver = webdriver.Chrome('/Users/Chris/Documents/Selenium/chromedriver')  # Optional argument, if not specified will search path.
driver.set_window_size(500, 900)
driver.set_window_position(0, 0)
driver.get('https://www.cars.com/research/compare/')

makeDropdown = driver.find_element_by_id('make-dropdown')
makeDropdown.click()
modelDropdown = driver.find_element_by_id('model-dropdown')
yearDropdown = driver.find_element_by_id('year-dropdown')

options1 = [x for x in makeDropdown.find_elements_by_tag_name("option")]

sqlQuery = "INSERT INTO CarInfo (make, model, year) VALUES "

for make in options1:
  sqlQuery = "INSERT INTO CarInfo (make, model, year) VALUES "
  if make.text != "":
    makeText = make.text
    make.click()
    modelDropdown.click()
    options2 = [x for x in modelDropdown.find_elements_by_tag_name("option")]
    for model in options2:
      if model.text != "":
        modelText = model.text
        model.click()
        modelDropdown.click()
        options3 = [x for x in yearDropdown.find_elements_by_tag_name("option")]
        for year in options3:
          if year.text != "":
            yearText = year.text
            sqlQuery += "('" + makeText + "', '" + modelText + "', " + yearText + "),"
            print "('" + makeText + "', '" + modelText + "', " + yearText + "),"
            #year.click()
            #yearDropdown.click()
    sqlQuery = sqlQuery.rstrip(',')
    sqlQuery += ";\n\n"
    print sqlQuery

    resultFile = open('output2.txt', 'a')
    resultFile.write(sqlQuery + "\n\n")
    resultFile.close()

driver.quit()
driver.stop_client()
