from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.cnn.com/asia"

path = "/Users/lyang/Downloads/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

titles = []

containers = driver.find_elements(by="xpath", value='//span[@class="cd__headline-text vid-left-enabled"]')

for container in containers:
    title = container.find_element(by="xpath",value='.').text
    titles.append(title)

print(titles)