# Q 1

def isPrime ( i ) :
    j = 1
    counter = 0

    while j <= i :
        if i % j == 0 :
            counter += 1
        j += 1

    if counter == 2 :
        return True
    else :
        return False

# (------------------------------------)
# x ---> input list     r ---> prime nums

def result (x, r) :

    maxim = 0
    bigger = 0

    for i in range( 0, len( r ) ) :
        if r[ i ] >= maxim :
            maxim = r[ i ]
            if x[ i ] >= bigger :
                bigger = x[ i ]
    
    return f"{bigger} {maxim}"

# (------------------------------------)
# d ---> Deivisior Number
# pc --> Prime Counts

def divider ( x ) :
    d = 1
    pc = 0
    
    if isPrime( x ) == True :
        pc += 1
    else :
        while d <= x/2 :
            if x % d == 0 :
                if isPrime( d ) == True :
                    pc += 1
            d += 1
    return pc

# (------------------Main------------------)

print("\n")

UserTest = []
for i in range( 0, 10 ) :
    UserTest.append( int( input() ) )

testlist = [ 123, 43, 54, 12, 76, 84, 98, 678, 543, 231, 25 ]

primes_count = []

for i in UserTest:
    primes_count.append( divider( i ) )

#range( 0, len( testlist )
print( result( UserTest, primes_count ) )