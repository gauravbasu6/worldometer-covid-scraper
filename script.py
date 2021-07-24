import requests
from bs4 import BeautifulSoup
import csv

r= requests.get('https://www.worldometers.info/coronavirus/')
html_doc = r.text

soup = BeautifulSoup(html_doc,'lxml')

csv_file = open("worldometer-total.csv",'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Serial no','Country','Cases','Link'])


table = soup.find(id="main_table_countries_today")
print('Serial No\tCountry\tTotal Cases')
for tr in table.findAll('tr'):
    try:
        if(tr['style']!="display: none"):
            print(f"{tr.td.text}\t{tr.td.next_sibling.next_sibling.text}\t{tr.td.next_sibling.next_sibling.next_sibling.next_sibling.text}\thttps://www.worldometer.com/coronavirus/{tr.td.next_sibling.next_sibling.a['href']}")
            csv_writer.writerow([tr.td.text,tr.td.next_sibling.next_sibling.text,tr.td.next_sibling.next_sibling.next_sibling.next_sibling.text,f"https://www.worldometer.com/coronavirus/{tr.td.next_sibling.next_sibling.a['href']}"])
    except:
        pass
