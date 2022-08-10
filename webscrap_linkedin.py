from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

website = "https://www.ratemds.com/best-doctors/va/reston/?page=2"

path = "/Users/lyang/Downloads/chromedriver"

#headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service, options=options)
titles = []
specialties = []
specialties2 = []
comments = []

driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="search-item doctor-profile"]')

for container in containers:
    title = container.find_element(by="xpath",value='./a/h2[@class="search-item-doctor-name"]').text
    specialty = container.find_element(by="xpath",value='./div[@class="search-item-specialty"]').text
    comment = container.find_element(by="xpath",value='./div/div/p[@class="rating-comment"]/span').text

    titles.append(title)
    specialties.append(specialty)
    comments.append(comment)

driver.find_elements(by="xpath", value="//a[@aria-label='Next page']").click()
time.sleep(1)

d = {'Name':titles,'Specialty':specialty,'Specialty_2':specialty_2,'Comment':comments}
df = pd.DataFrame(d)

print(df)