# Traveling dictionary
# (.............: :)ctions :.............)

def translator ( samples, txt_part ) :
    my_dict = []
    for word in samples :
        my_dict.append( word.split() )
    
    
    result = ""
    for i in range( 0, len(my_dict) ) :
        for j in range( 0, len(my_dict[i]) ) :
            if txt_part == my_dict[i][j] :
                return str(my_dict[i][0])

def TheEnd ( sample, txt ) :
    splited_txt = []
    splited_txt = txt.split()

    output = ''

    for item in splited_txt :
        if translator ( sample, item ) == None :
            output += str(item) + " "
        else :
            output += translator( sample, item ) + " "
    
    print(output)
# (.............: Main :.............)
n = int( input() )

entries = []

for i in range(0, n) :
    entries.append( input() )
target = input()

TheEnd( entries, target )
