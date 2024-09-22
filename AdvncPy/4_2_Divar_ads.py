#   (....: Libs :....)
from bs4 import BeautifulSoup
import requests

#   (....: defs :....)
def special_search ( url, search_key ) :
    res = requests.get( url )
    soup = BeautifulSoup( res.text, 'html.parser')

    ads = soup.find_all('div', class_='kt-post-card__body')
    ad_links = soup.find_all('a')
    ad_title = soup.find_all('h2', class_='kt-post-card__title')
    tag = soup.find_all('div', class_='kt-post-card__description')

    for ad in ads :
        target = ad.find( 'div', class_='kt-post-card__description' )
        if target != None :
            if str( target.text ) == search_key :
                print( f"> {ad.find('h2', class_='kt-post-card__title').text} ---> {target.text}" )

#   (....: main :....)

url1 = 'https://divar.ir/s/tehran'

special_search(url1 , 'پرداخت توافقی')