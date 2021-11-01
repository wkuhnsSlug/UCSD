import pandas as pd
import matplotlib.pyplot as plt
import math

print(pd.__version__)
path = "C:\\Users\\Will\\PycharmProjects\\pandaPractice\\venv\\data\\"

movies = pd.read_csv(path+'titles.csv')
cast = pd.read_csv(path+'cast.csv.zip')
release_dates = pd.read_csv(path+'release_dates.csv', parse_dates=['date'], infer_datetime_format=True)

def section_one(movies, cast):
    '''
    :param movies:
    :param cast:
    '''
    # q1
    movies[movies.title.str.contains('^Harry Potter', regex=True, na=False)].sort_values('year', ascending=False)
    # q2
    len(movies[movies.year == 2015])
    # 8702
    # q3
    # including 2018?
    len(movies[(movies.year >= 2000) & (movies.year <= 2018)])
    # 114070
    # q4
    len(movies[movies.title == "Hamlet"])
    # 20
    # q5
    movies[(movies.title == 'Hamlet') & (movies.year >= 2000)].sort_values('year')
    # q6
    len(cast[(cast.title == "Inception") & (pd.isnull(cast.n))])
    # 27
    # q7
    len(cast[(cast.title == "Inception") & (cast.n)])
    # 51
    # q8
    cast[(cast.title == "Inception") & (cast.n)].sort_values('n').head(10)
    # q9 A
    cast[(cast.character == "Albus Dumbledore")]
    # q9 B
    cast[(cast.character == "Albus Dumbledore")].drop_duplicates('name')
    # q10 A
    len(cast[(cast.name == "Keanu Reeves")])
    # 62
    # q10 B
    cast[(cast.name == "Keanu Reeves") & (cast.n == 1) & (cast.year >= 1999)].sort_values('year')
    # q11 A
    people = cast[(cast.type == "actor") | (cast.type == "actress")]
    len(people[(people.year >= 1950) & (people.year <= 1960)])
    # 234635
    # q11 B
    len(people[(people.year >= 2007) & (people.year <= 2017)])
    # 1452413
    # q12 A
    len(cast[(cast.n == 1) & (cast.year >= 2000)])
    # 60568
    # q12 B
    len(cast[(cast.n > 1) & (cast.n) & (cast.year >= 2000)])
    # 1001710
    # q12_C
    len(cast[(pd.isnull(cast.n)) & (cast.year >= 2000)])
    # 887484

#section two
top_ten = movies.title.value_counts()[:10]
print(top_ten)

#q1
def most_released_2000s(movies):
    '''
    :param movies:
    :return the 3 years with most movies released in the 2000s:
    '''
    top_three = movies.year.value_counts()[:3]
    print(top_three)

#q2 & 7
def films_by_decade(movies):
    decades = movies.sort_values('year')
    decades['decades'] = decades.year//10*10
    pl = decades.decades.value_counts()[:12].sort_values()
    pl.plot(kind="barh")
    pl2 = decades[decades.title=='Hamlet'].decades.value_counts().sort_values()
    pl2.plot(kind="barh")
#q3
def most_common(cast):
    cast['character'].value_counts()[:10]
    cast[cast.character == "Herself"]['name'].value_counts()[:10]
    cast[cast.character == "Himself"]['name'].value_counts()[:10]

#q4
def most_freq(cast):
    cast[cast['character'].str.startswith('Zombie')]['character'].value_counts()[:10]
    cast[cast['character'].str.startswith('Police')]['character'].value_counts()[:10]

#q5 & 6
def keanu_plot(cast):
    cast[cast.name == 'Keanu Reeves']['year'].value_counts().plot(kind="barh")
    cast[cast.name == 'Keanu Reeves'].plot.scatter(x='year', y='n')

#q8
len(cast[(cast.n==1) & (cast.year>1959) & (cast.year<1970)])
len(cast[(cast.n==1) & (cast.year>1999) & (cast.year<2010)])

#q9 & 10
def frank_oz_flim_years(cast):
    frank_oz_movies = cast[cast.name == 'Frank Oz']
    frank_oz_movies[frank_oz_movies['title'].duplicated()].sort_values('year')['title'].drop_duplicates()
    frank_oz_movies[frank_oz_movies['character'].duplicated()]['character'].drop_duplicates()

#section 3

christmas = release_dates[(release_dates.title.str.contains('Christmas')) & (release_dates.country == 'USA')]
christmas.date.dt.month.value_counts().sort_index().plot(kind='bar')

#q1
summer = release_dates[(release_dates.title.str.contains('Summer')) & (release_dates.country == 'USA')]
summer.date.dt.month.value_counts().sort_index().plot(kind='bar')

#q2
action = release_dates[(release_dates.title.str.contains('Action')) & (release_dates.country == 'USA')]
action.date.dt.isocalendar().week.value_counts().sort_index().plot(kind='bar')

#q3 & 4
def keanu_movies_by_DoR(cast, release_datas):
    keanu_movies = cast[(cast.name == "Keanu Reeves") & (cast.n == 1)]
    usa_movies = release_dates[release_dates.country == 'USA']
    keanu_usa = pd.merge(keanu_movies, usa_movies, how='inner', on='title')
    keanu_usa['date']= pd.to_datetime(keanu_usa.date)
    keanu_usa = keanu_usa.sort_values(by='date')
    keanu_usa.date.dt.month.value_counts().sort_index().plot(kind='bar')

#q5
def ian_movies_by_DoR(cast, release_datas):
    ian_movies = cast[cast.name == "Ian McKellen"]
    usa_movies = release_dates[release_dates.country == 'USA']
    ian_usa = pd.merge(ian_movies, usa_movies, how='inner', on='title')
    ian_usa['date'] = pd.to_datetime(ian_usa.date)
    ian_usa = ian_usa.sort_values(by='date')
    ian_usa.date.dt.year.value_counts().sort_index().plot(kind='bar')