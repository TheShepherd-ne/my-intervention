from datetime import datetime

def calculate_age( birth_date ) :
    try :
        birth_date = datetime.strptime( birth_date, "%Y/%m/%d" )
        today = datetime.now()

        age = today.year - birth_date.year - ( ( today.month, today.day ) < ( birth_date.month, birth_date.day ) )
        return age
    except ValueError:
        return "WRONG"

birth_date_input = input()

print( calculate_age(birth_date_input) )