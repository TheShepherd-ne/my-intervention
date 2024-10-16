#   (...: libs :...)
import mysql.connector
import requests
from bs4 import BeautifulSoup

#   (...: defs :...)
#   input Your DATABASE information
# def user_account () :
print('Do you entered your database properties?')
ans = input('y/n : ')
if ans == 'n' :
    print( "Enter your database properties please ..." )
    host = input("db's host : ")
    user = input('db user : ')
    password = input('db pass : ')
    database = input('db name : ')
    table_name = input('table name : ')
    # print('enter target table name in GETINFO.py/send_to_db and GETINFO.py/db_fetch')
else :
    pass

def send_to_db ( name, capital, population, area) :
    try :
        global host
        global user
        global password
        global database
        global table_name

        mydb = mysql.connector.Connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        mouse = mydb.cursor()   #   change final_proj
        query = f'INSERT INTO {table_name} VALUES (%s, %s, %s, %s)'
        mouse.execute( query, ( name, capital, population, area) )
        mydb.commit()

    except  mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally :
        mouse.close()
        mydb.close()

def db_fetch () :
    try :
        global host
        global user
        global password
        global database
        global table_name

        mydb = mysql.connector.Connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        mouse = mydb.cursor()   #   change final_proj
        query = f"Select * From {table_name}"
        mouse.execute( query )

        datas = mouse.fetchall()

        return datas

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally :
        mouse.close()
        mydb.close()

def get_info( url ) :
    res = requests.get( url )
    soup = BeautifulSoup( res.text, 'html.parser' )

    country_pack = soup.find_all('div', class_='col-md-4 country')
    
    country_inf = []

    for item in country_pack :
        name = item.find( 'h3', class_='country-name' ).text.strip()
        capital = item.find( 'span', class_='country-capital').text
        population = item.find( 'span', class_='country-population').text
        area = item.find( 'span', class_='country-area').text
        
        country_inf.append( (name.replace('\n', ''), capital.replace('\n', ''), population.replace('\n', ''), area.replace('\n', '')) )
        send_to_db( name.replace('\n', ''), capital.replace('\n', ''), population.replace('\n', ''), area.replace('\n', '') )
