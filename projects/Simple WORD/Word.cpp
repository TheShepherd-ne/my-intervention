#include <iostream>
using namespace std ;
//--------------------------------------------------------------------------

//--------------------------------------------------------------------------
int main ()
{
	int m=2000 ;
	char s [m] ;
	
	cout << "\n\t Write any thing you want : " ; cin.getline ( s , m ) ;
	
	cout << "\n\t How do you want to change what you write ? " ;
	
	int n=1 ;
	for ( n ; n < 7 ; n++ )
	{
		if (n=1) cout << "\n\t\t" << n << ". Sentence case " ;
		if (n=2) cout << "\n\t\t" << n << ". lowercase " ;
		if (n=3) cout << "\n\t\t" << n << ". UPPERCASE " ;
		if (n=4) cout << "\n\t\t" << n << ". Capitalize Each Word " ;
		if (n=5) cout << "\n\t\t" << n << ". tOGGLE CASE " ;
		if (n=6) cout << "\n\t\t" << n << ". Word Count " ;	
	}
	
	cout << "\n\n\t Enter Num 1~6 : " ; cin >> n ;
//--------------------------------------------------------	
	switch (n)
{	case 1 :
	{
		if ( s[0] != '\0' )
			if ( s[0] >= 'a' && s[0] <= 'z' )
			s[0] -= 32 ;
		
	}
	cout << "\n Sentence case : " << s ; break;


	case 2 :
	{
		for ( int i=0 ; s[i] != '\0' ; i++ )
			if ( s[i] >= 'A' && s[i] <= 'Z' )
			s[i] += 32 ;
		
	}
	cout << "\n lower case : " << s ; break;

	
	case 3 :
	{
		for ( int i=0 ; s[i] != '\0' ; i++ ) //NULL = '\0'
			if ( s[i] >= 'a' && s[i] <= 'z' ) //a-->97 ya z-->122
			s[i] -= 32 ;
	
	}
	cout << "\n UPPER CASE : " << s ; break;


	case 4 :
	{
		int y = 0 ;
		s[0] -= 32 ;
		for ( int i=0 ; s[i]!='\0' ; i++ )
		{
			y++ ;
			if ( 32 <= s[i] && s[i]<=38 || 40<=s[i] && s[i]<64 || 91<=s[i] && s[i]<96 || 123<=s[i] && s[i]<=127 )
			{
				if ( s[y]>='a' && s[y]<='z' )
				s[y] -=32 ;
			}
		
		}
	}
	cout << "\n Capitalize Each Word : " << s ; break;



	case 5 :
	{
		for ( int i=0 ; s[i] != '\0' ; i++ )
			if ( s[i] >= 'a' && s[i] <= 'z' )
				s[i] -= 32 ;
				s[0] += 32 ;
	
	}
	cout << "\n tOGGLE CASE : " << s ; break;


	int j;
	case 6 :
	{
		j = 1;
		for (int i=0 ; s[i] != '\0' ; i++)
		{
			if ( s[i] == ' ' )
				j++;
		}
		
		
	}
	cout << "\n Word count : " << j ; break;

}
	
	return 0;
}

//---------------------------------------


