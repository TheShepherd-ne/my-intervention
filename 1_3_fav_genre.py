# Favorite Genre

# (------------------ Class ------------------)

# (------------------ defs ------------------)

def splitter (  entry ) :
    return entry.split()

def which_genre ( entry, genres ) :
    for key in genres :
        if entry == key :
            genres[key] += 1
    
    return genres

# (------------------ Main ------------------)

genres = { "Action": 0 , "Adventure": 0 , "Comedy": 0 , "History": 0 , "Horror": 0 , "Romance": 0 }
datas = []

# input >
counter = int( input() )
enter = []

for i in range( 0, counter ) :
    enter.append( str( input() ) )

for i in enter :
    datas.append( splitter(i) )

for i in range(0, counter) :
    for j in range(1, 4) :
        if datas[i][j] == None :
            datas[i][j] = 0
        else :
            which_genre( datas[i][j], genres )

print( genres.items() )

sorted_dict = dict( sorted( genres.items(), key = lambda item : ( item[1] ), reverse=True ))

for keys, value in sorted_dict.items() :
    print( f'{keys} : {value}' )

# output >
# Action : 3
# Comedy : 2
# History : 2
# Horror : 2
# Romance : 2
# Adventure : 1