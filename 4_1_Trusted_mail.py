import re

def Validating( e_addr ) :
    isvalid = r'^[a-zA-Z0-9]+@[a-z]+\.[a-z]{2,}$'

    if re.match( isvalid, e_addr ) :
        return 'OK'
    else :
        return 'WRONG'

#   (....: Main :....)

entry_mail = input()

print( Validating( entry_mail ) )

