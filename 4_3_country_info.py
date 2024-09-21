#   (...: libs :...)
import mysql.connector
import requests
from bs4 import BeautifulSoup

#   (...: defs :...)
#   input Your DATABASE information
def send_to_db (name, capital, population, area) :
    try :
        mydb = mysql.connector.Connect(
            host = 'localhost',
            user = '',
            password = '',
            database = ''
        )

        mouse = mydb.cursor()
        mouse.execute( 'INSERT INTO country_info VALUES (%s, %s, %s, %s)', (name, capital, population, area) )
        mydb.commit()

    except  mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally :
        mouse.close()
        mydb.close()

def get_info( url ) :
    res = requests.get( url )
    soup = BeautifulSoup( res.text, 'html.parser' )

    country_pack = soup.find_all('div', class_='col-md-4 country')
    
    country_inf = []
    counter = 0

    for item in country_pack :
        name = item.find( 'h3', class_='country-name' ).text.strip()
        capital = item.find( 'span', class_='country-capital').text
        population = item.find( 'span', class_='country-population').text
        area = item.find( 'span', class_='country-area').text
        
        country_inf.append( (name.replace('\n', ''), capital.replace('\n', ''), population.replace('\n', ''), area.replace('\n', '')) )
        send_to_db( name.replace('\n', ''), capital.replace('\n', ''), population.replace('\n', ''), area.replace('\n', '') )

        counter += 1
        if counter == 20 :
            break

    # for item in country_inf :
    #     print( item, '\n' )   # if you want to see the result without checking your database, use ' ctrl+/ ' to uncomment this part :)

#   (...: main :...)
website = 'https://www.scrapethissite.com/pages/simple/'

get_info( website )
print('DONE :)')