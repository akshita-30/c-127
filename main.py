from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('/Users/HP_BOOK_PRO/Desktop/c-127/venv/chromedriver')
browser.get(start_url)
time.sleep(10)
def scrape():
    headers = ['name','light_years_from_earth','planet_mass','stellar_magnitude','discovery_date']
    planet_data = []
    for i in range(0,492):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all('ul',attrs={'class','exoplanet'}):
            li_tags = ul_tag.find_all('li')
            temp = []
            for index,li_tag in enumerate(li_tags):
                if index == 0 :
                    temp.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp.append(li_tag.contents[0])
                    except:
                        temp.append('')
            planet_data.append(temp)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scraper.csv','w')as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planet_data)
scrape()                    