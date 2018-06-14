import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.livechennai.com/Vegetable_price_chennai.asp'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

#to find filename

date_tab = soup.find(class_='col-sm-8')
file_name = date_tab.find('h1').contents[0]

#to find date

a = file_name

file_name_split = (a.split('-'))
file_name_without_name  = (file_name_split[1])

file_name_without_slash = (file_name_split[0])
	
filename_date = (file_name_without_name.split('/'))
year = filename_date[-1]
months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
month = months[filename_date[-2]]
day = filename_date[-3]
date_of_file = year + '-' + month + '-' + day
	
file_nam = file_name_without_slash + '-' + date_of_file + '.csv'
csv_file = csv.writer(open(file_nam,'w'))
csv_file.writerow([' NAME ',' PRICE (Rs) ',' DATE '])

# to find price

table = soup.find('table', attrs={'class':'table-price1'})

table_row = table.find_all('tr')

for row in table_row:
	name_veg = row.find_all('td')[1].contents[0]
	price_veg = row.find_all('td')[2].contents[0]
	csv_file.writerow([name_veg,price_veg,date_of_file])
	
