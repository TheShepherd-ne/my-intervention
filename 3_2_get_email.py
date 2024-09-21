import mysql.connector

def power_db ( username, password ) :
    try :
        db = mysql.connector.connect( host = 'localhost', user = '...', password = '...', database = '...' )
        
        cursor = db.cursor()
        sql = f'INSERT INTO login (username, password) VALUES (%s, %s);'
        cursor.execute( sql, (username, password) )
        db.commit()
    
    except mysql.connector.Error as err :
        print(f"Error: {err}")
    
    finally :
        cursor.close()
        db.close()

def get_email ( email, password ) :

    if "@" not in email or email.count("@") != 1:
        return False
    
    user, domain = email.split("@")
    
    if len(user) == 0 or len(domain) == 0:
        return False
    
    if "." not in domain:
        return False
    
    domain_parts = domain.split(".")
    if any(len(part) == 0 for part in domain_parts):
        return False
    
    if password == '' :
        return False
    
    return True

#   (..: Main :..)

emailaddr = input()
passwrd = input()

while get_email(emailaddr, passwrd) is not True :
    print("Your email address is NOT correct\nCorrect Form : < expression@string.string >\nPlease try again")
    emailaddr = input()
    passwrd = input()

power_db(emailaddr, passwrd)