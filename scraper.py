# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests
from bs4 import BeautifulSoup


def scrape():
    
    url = 'http://www.scrapethissite.com/pages/simple/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    for i in soup.find_all('h3') :
        print("Country name:" + i.text)
    for j in soup.find_all(class_ =["country-capital", "country-population" , "country-area"]): 
        print(j)

    for country, capital, population, area in zip(soup.find_all('h3'), soup.find_all(class_ = "country-capital"), soup.find_all(class_ = "country-population"), soup.find_all(class_ = "country-area")):
        print("Country :" + country.text.strip(), "Capital :" + capital.text, "Population :" + population.text, "Area :" + area.text)
    print(text)
    print(link)



if __name__ == '__main__':
    scrape()
