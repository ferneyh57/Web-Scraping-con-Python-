import csv
from bs4 import BeautifulSoup


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.amazon.com/-/es/")
