from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def getDriver():
  option = webdriver.ChromeOptions()
  option.add_argument('--headless')

  return webdriver.Chrome(service=Service('D:\John\STKI\Scraping by Subject\driver\chromedriver.exe'), options=option)

def parsePage(driver, page_link):
  driver.get(page_link)
  soup = BeautifulSoup(driver.page_source, 'html.parser')

  return soup

def getRawJSON(soup, selector = 'pre'):
  content_raw = soup.select(selector)
  content = content_raw[0].text

  return content

def getSubjectsLink(soup, selector):
  content_raw = soup.select(selector)
  content = [x['href'][:-5] for x in content_raw]

  return content

def writeContentToFile(content, file):
  with open(file, 'w') as f:
    f.write(content)