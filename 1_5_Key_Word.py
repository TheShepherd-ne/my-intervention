
# (-------------------- Funcs --------------------)

def txt_divider (txt) :
    divided_txt = txt.split(".")
    return divided_txt  # return devided txt by .

def extract_key ( txt ) :
    keyword = []
    indexes = []
    splited_txt = []
    
    txt = txt_divider( txt )
    for item in txt :
        splited_txt.append( ( item.split() ) )

    for i in range(0, len(splited_txt) ) :
        for indx, word in enumerate( splited_txt[i] ) :
            if indx >= 1 :
                if word[0].isupper() :
                            keyword.append( word )
                            if i >= 1 :
                                indexes.append( indx + len ( splited_txt[ i-1 ] ) + 1 )
                            else :
                                indexes.append( indx + 1 )

    for i in range( 0, len( indexes ) ) :
        print( f"{indexes[i]}:{keyword[i].replace(',', '')}" )
    if keyword == [] :
     print( 'None' )
    else :
     return keyword

# (-------------------- Main --------------------)

# entry_txt = 'The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.'
# extract_key ( entry_txt )
# # tst_txt = 'How are you boys. We are here'
# extract_key ( tst_txt )

get_txt = input()
extract_key ( get_txt )