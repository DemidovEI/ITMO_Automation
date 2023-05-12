from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/elements')


print(driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.row > div:nth-child(2)').text)
