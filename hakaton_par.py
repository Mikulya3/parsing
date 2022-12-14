
import requests
from bs4 import BeautifulSoup as BS
import csv
from urllib import response

def get_html(url):
    response=requests.get(url)
    return response.text

def get_soup(html):
    soup=BS(html,'lxml')
    return soup
    

def get_data(soup):
    
    catalog=soup.find('div',class_='search-results-table')
    cars=catalog.find_all('div',class_='list-item list-label')
    
    for car in cars:
        try:
            title=car.find('h2',class_='name').text.replace(' ','')
        except AttributeError:
            title=''
        try:
            price=car.find('div',class_='block price').text.replace(' ','')
            print(price)
        except AttributeError:
            price=''
        try:
            image=car.find('div',class_='tmb-wrap-table').get('src')
        except AttributeError:
            image=''
        try:
            description=car.find('div',class_='block info-wrapper item-info-wrapper').text.replace(' ','')
        except AttributeError:
            description=''
        print(title)
        data=({
            'title':title,
            'price':price,
            'image':image,
            'description':description
        })
        write_csv(data)
        write_csv([title,price,image,description])
       
def write_csv(data):
    file=open ('mashina.csv', mode='a', newline='') 
    names=['title','price','image','description']
    write=csv.DictWriter(file,delimiter=',',quotechar='|',fieldnames=names)
    write.writerow(data)
    file.close

def write_csv(data):
    with open('mashina.csv','a') as file:
        file.writelines(data)



def main():
    for i in range(1,1050):
        BASE_URL=f'https://www.mashina.kg/search/all/?page={i}'
        html=get_html(BASE_URL)
        soup=get_soup(html)
        get_data(soup)
    

if __name__=='__main__':
    main()