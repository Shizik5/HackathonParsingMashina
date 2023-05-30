import requests
from bs4 import BeautifulSoup
import csv

def write_csv(data):
    with open('mashina.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([data['title'],data['price'],data['image'],data['discription']])

def get_html(url):
    response = requests.get(url)
    return response.text

url = f'https://www.mashina.kg/search/all/?page=1'
access = get_html(url)
page = BeautifulSoup(access,'lxml')
katalog = page.find_all('div','table-view-list image-view clr label-view')
for i in katalog:
    title = i.find('h2', class_ = 'name').text
    price = i.find('div', class_ = 'block price').text
    image = 'https://www.mashina.kg/' + i.find('div', class_='Еще 5 фото внутри').get('src')
    discription = i.find('div', class_ = 'block info-wrapper item-info-wrapper').text
    ls = {'title':title, 'price':price, 'image':image, 'discription':discription}
    write_csv(ls)
