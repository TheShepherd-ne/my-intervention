import mysql.connector

def connecting_to_db () :
    try :
        mydb = mysql.connector.Connect(
            host = 'localhost',
            user = 'root',
            password = 'theey',
            database = 'mproj'
        )
        print("Connected to database\n")

        curser = mydb.cursor()
        Query = 'SELECT * FROM emoplee;'
        curser.execute(Query)

        emp_data = []

        for (Name, Height, Weight) in curser :
            emp_data.append( (Name, Height, Weight) )
        sorted_employees = sorted(emp_data, key=lambda x: (x[1], -x[2]), reverse=True)
        
        for item in sorted_employees :
            print(f"{ item[0] } { item[1] } { item[2] }")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally :
        curser.close()
        mydb.close()

# (....: Main :....)

connecting_to_db()