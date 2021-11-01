#s1
movies =[]
cast =[]
# q1
movies[movies.title.str.contains('^Harry Potter', regex= True, na=False)].sort_values('year',ascending=False)

'''
	title 	year
143147 	Harry Potter and the Deathly Hallows: Part 2 	2011
152831 	Harry Potter and the Deathly Hallows: Part 1 	2010
109213 	Harry Potter and the Half-Blood Prince 	2009
50581 	Harry Potter and the Order of the Phoenix 	2007
187926 	Harry Potter and the Goblet of Fire 	2005
61957 	Harry Potter and the Prisoner of Azkaban 	2004
82791 	Harry Potter and the Chamber of Secrets 	2002
223087 	Harry Potter and the Sorcerer's Stone 	2001
'''

# q2
len(movies[movies.year == 2015])
#8702

# q3
#including 2018?
len(movies[(movies.year >= 2000) & (movies.year <= 2018)])
#114070

# q4
len(movies[movies.title == "Hamlet"])
#20

# q5
movies[(movies.title=='Hamlet') & (movies.year >=2000)].sort_values('year')
'''
 	title 	year
55639 	Hamlet 	2000
1931 	Hamlet 	2009
227953 	Hamlet 	2011
178290 	Hamlet 	2014
186137 	Hamlet 	2015
191940 	Hamlet 	2016
244747 	Hamlet 	2017
'''

# q6
len(cast[(cast.title=="Inception") & (pd.isnull(cast.n))])
#27

# q7
len(cast[(cast.title=="Inception") & (cast.n)])
#51

#q8
cast[(cast.title=="Inception") & (cast.n)].sort_values('n').head(10)
'''
 	title 	year 	name 	type 	character 	n
590576 	    Inception 	2010 	Leonardo DiCaprio   	actor 	    Cobb 	            1.0
859993  	Inception 	2010 	Joseph Gordon-Levitt 	actor 	    Arthur 	            2.0
3387147 	Inception 	2010 	Ellen Page 	            actress    	Ariadne 	        3.0
940923  	Inception 	2010 	Tom Hardy 	            actor   	Eames 	            4.0
2406531 	Inception 	2010 	Ken Watanabe 	        actor   	Saito 	            5.0
1876301 	Inception 	2010 	Dileep Rao 	            actor   	Yusuf 	            6.0
1615709 	Inception 	2010 	Cillian Murphy 	        actor 	    Robert Fischer 	    7.0
183937  	Inception 	2010 	Tom Berenger 	        actor 	    Browning 	        8.0
2765969 	Inception 	2010 	Marion Cotillard 	    actress 	Mal 	            9.0
1826027 	Inception 	2010 	Pete Postlethwaite  	actor 	    Maurice Fischer     10.0
'''

# q9 A
cast[(cast.character=="Albus Dumbledore")]
'''
title 	year 	name 	type 	character 	n
704984 	Epic Movie                              	2007 	Dane Farwell 	        actor 	Albus Dumbledore 	17.0
792421 	Harry Potter and the Goblet of Fire 	    2005 	Michael Gambon      	actor 	Albus Dumbledore 	37.0
792423 	Harry Potter and the Order of the Phoenix 	2007 	Michael Gambon      	actor 	Albus Dumbledore 	36.0
792424 	Harry Potter and the Prisoner of Azkaban 	2004 	Michael Gambon      	actor 	Albus Dumbledore 	27.0
947789 	Harry Potter and the Chamber of Secrets 	2002 	Richard Harris      	actor 	Albus Dumbledore 	32.0
947790 	Harry Potter and the Sorcerer's Stone   	2001 	Richard Harris      	actor 	Albus Dumbledore 	1.0
1685537 Ultimate Hero Project 	                    2013 	George (X) O'Connor 	actor 	Albus Dumbledore 	NaN
2248085 Potter                                  	2015 	Timothy Tedmanson 	    actor 	Albus Dumbledore 	NaN
'''
#q9 B
cast[(cast.character=="Albus Dumbledore")].drop_duplicates('name')
'''

title 	year 	name 	type 	character 	n
704984 	Epic Movie 	                                2007 	Dane Farwell         	actor 	Albus Dumbledore 	17.0
792421 	Harry Potter and the Goblet of Fire 	    2005 	Michael Gambon 	        actor 	Albus Dumbledore 	37.0
947789 	Harry Potter and the Chamber of Secrets 	2002 	Richard Harris       	actor 	Albus Dumbledore 	32.0
1685537 Ultimate Hero Project 	                    2013 	George (X) O'Connor 	actor 	Albus Dumbledore 	NaN
2248085 Potter 	                                    2015 	Timothy Tedmanson 	    actor 	Albus Dumbledore 	NaN
'''
#q10 A
len(cast[(cast.name=="Keanu Reeves")])
#62
#q10 B
cast[(cast.name=="Keanu Reeves") & (cast.n==1) & (cast.year>=1999)].sort_values('year')
'''
 	title 	year 	name 	type 	character 	n
1892390 	The Matrix 	                    1999 	Keanu Reeves 	actor 	Neo 	                1.0
1892397 	The Replacements            	2000 	Keanu Reeves 	actor 	Shane Falco 	        1.0
1892358 	Hard Ball 	                    2001 	Keanu Reeves 	actor 	Conor O'Neill       	1.0
1892383 	Sweet November              	2001 	Keanu Reeves 	actor 	Nelson Moss 	        1.0
1892348 	Constantine                    	2005 	Keanu Reeves 	actor 	John Constantine       	1.0
1892388 	The Lake House 	                2006 	Keanu Reeves 	actor 	Alex Wyler          	1.0
1892382 	Street Kings                 	2008 	Keanu Reeves 	actor 	Detective Tom Ludlow 	1.0
1892385 	The Day the Earth Stood Still 	2008 	Keanu Reeves 	actor 	Klaatu 	                1.0
1892359 	Henry's Crime 	                2010 	Keanu Reeves 	actor 	Henry Torne 	        1.0
1892342 	47 Ronin 	                    2013 	Keanu Reeves 	actor 	Kai 	                1.0
1892361 	John Wick                   	2014 	Keanu Reeves 	actor 	John Wick 	            1.0
1892366 	Knock Knock                 	2015 	Keanu Reeves 	actor 	Evan 	                1.0
1892399 	The Whole Truth             	2016 	Keanu Reeves 	actor 	Ramsey              	1.0
1892362 	John Wick: Chapter 2            2017 	Keanu Reeves 	actor 	John Wick           	1.0
1892378 	Siberia                     	2018 	Keanu Reeves 	actor 	Lucas Hill           	1.0
'''
#q11 A
people=cast[(cast.type=="actor") | (cast.type=="actress")]
len(people[(people.year>=1950) & (people.year<=1960)])
#234635
#q11 B
len(people[(people.year>=2007) & (people.year<=2017)])
#1452413
#q12 A
len(cast[(cast.n==1) & (cast.year>=2000)])
#60568
#q12 B
len(cast[(cast.n>1) & (cast.n) & (cast.year>=2000)])
#1001710
#q12_C
len(cast[(pd.isnull(cast.n)) & (cast.year>=2000)])
#887484
