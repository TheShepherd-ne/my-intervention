#   (...: LIBS :...)
from GETINFO import get_info
from GETINFO import db_fetch
from sklearn import tree
from sklearn.linear_model import LinearRegression

#   (...: DEFS :...)
def input_to_db( url ) :
    get_info( url )

def estimating( popularity ) :
    try :
        x = []
        y = []

        infos = db_fetch()
        for row in infos :
            x.append( row[2] )
            y.append( row[3] )

        x = [ [value] for value in x ]
        y = [ [value] for value in y ]

        clf = LinearRegression()
        clf = clf.fit( x, y )
        newdata = [ [ popularity ] ]
        answer = clf.predict(newdata)
        
        print(f'area maybe : { answer }')

    except Exception as err:
        print(f"Error: {err}")

#   (...: MAIN :...)
url = 'https://www.scrapethissite.com/pages/simple/'
input_to_db( url )
print('datas are in your database now :)\n')
estimating( int( input("Population : ") ) )