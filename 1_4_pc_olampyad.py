
# (----------------- Class -----------------)

# (----------------- Function -----------------)

def result (a) :
    return ' '.join(a)

# (----------------- Main -----------------)

counter = int( input() )
female = []
male = []

entries = []
# input
for c in range(0, counter) :
    entries.append( input() )

splited_list = []

for item in entries :
    splited_list.append( item.split('.') )

for i in range(0, counter) :
    splited_list[i][1] = splited_list[i][1].title()
    # splited_list[i][2] = splited_list[i][2].lower()
    if splited_list[i][0] == "f" :
        female.append(splited_list[i])
    else :
        male.append(splited_list[i])

female = sorted(female)
male = sorted(male)

for i in range( 0, len(female) ) :
    print( result (female[i]) )

for i in range( 0, len(male) ) :
    print( result (male[i]) )