# Health Planing

# (.................: Class :.................)

class Health_Plan :
    def __init__( self, class_name, ages, heights, weights ) :
        self.class_name = class_name
        self.age = ages
        self.height = heights
        self.weight = weights

    def A_avrg(self) :
        a_sum = 0
        for item in self.age :
            a_sum += item
        return a_sum/len(self.age)
    
    def H_avrg(self) :
        h_sum = 0
        for item in self.height :
            h_sum += item
        return h_sum/len(self.height)

    def W_avrg(self) :
        w_sum = 0
        for item in self.weight :
            w_sum += item
        return w_sum/len(self.weight)

# (.................: Func :.................)

def h_compare( x, y ) :
    if x != y :
        return 'A' if x>y else 'B'
    else :
        return 'Same'

def w_compare( x, y ) :
    if x != y :
        return 'B' if x>y else 'A'
    else :
        return 'Same'

def splitter( entry ) :
    splited = entry.split()
    int_list = [ int(num) for num in splited ]
    return int_list
# (.................: Main :.................)

A_ages = []; A_height = []; A_weight = []
B_ages = []; B_height = []; B_weight = []

count_A  = splitter( input() )
A_ages   = splitter( input() )
A_height = splitter( input() )
A_weight = splitter( input() )

count_B  = splitter( input() )
B_ages   = splitter( input() )
B_height = splitter( input() )
B_weight = splitter( input() )

frst_class = Health_Plan('A', A_ages, A_height, A_weight)
print( frst_class.A_avrg() ); print( frst_class.H_avrg() ); print( frst_class.W_avrg() )

scnd_class = Health_Plan('B', B_ages, B_height, B_weight)
print( scnd_class.A_avrg() ); print( scnd_class.H_avrg() ); print( scnd_class.W_avrg() )

compairing = [ ( frst_class.H_avrg(), scnd_class.H_avrg() ), ( frst_class.W_avrg(), scnd_class.W_avrg() ) ]


if h_compare( frst_class.H_avrg(), scnd_class.H_avrg() ) != 'Same' :
    print( h_compare( frst_class.H_avrg(), scnd_class.H_avrg() ) )
elif w_compare( frst_class.W_avrg(), scnd_class.W_avrg() ) != 'Same' :
    print( w_compare( frst_class.W_avrg(), scnd_class.W_avrg() ) )
else :
    print('Same')