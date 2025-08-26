import pandas as pd
import matplotlib.pyplot as plt

class MOVIES:
    def __init__(self):
        self.file=pd.read_csv("C:\\Users\\hp\\Downloads\\movies_dataset_beginner_messy.csv")


class Basic_Exploration(MOVIES):
    def display(self):
        display_rows=self.file.head(10)
        self.file.info()
        return f"\n first 10 rows are \n {display_rows}"
    

    #handling missing values
    def handling_missing_values(self):
        self.file['IMDb Rating']=self.file['IMDb Rating'].fillna(self.file['IMDb Rating'].median())
        self.file['Genre']=self.file['Genre'].fillna(self.file['Genre'].value_counts().idxmax())
        self.file['Director']=self.file['Director'].fillna(self.file['Director'].mode()[0])
        self.file['Country']=self.file['Country'].fillna('India')
        self.file['Release Year']=self.file['Release Year'].fillna(self.file['Release Year'].max())
        return self.file
    
    def delete_exact_duplicates(self):
        drop=self.file.drop_duplicates()
        return drop
        
class Content_Analysis(MOVIES):
    def newest_movie(self):
        new=self.file['Release Year'].idxmax()
        return "newest movie is:" ,self.file.loc[new,'Title']
    
    def oldest_movie(self):
        old=self.file['Release Year'].idxmin()
        return "oldest movie is:" ,self.file.loc[old,'Title']
    
    def director_titles(self):
        max_titles_director=self.file['Director'].mode()[0]
        return f"director having most number of titles is:\n{max_titles_director} and the titles they have are:\n{self.file.loc[self.file['Director']==max_titles_director,'Title']}"
    
    def count(self):
        count=self.file['Type']
        check_movies=(count=="Movie").sum()
        check_tv_shows=(count=="TV Show").sum()
        return f"total number of movies are:{check_movies} \n total number of TV shows are:{check_tv_shows}"
    
    def movies_per_genre(self):
        type=self.file[self.file['Type']=="Movie"]
        genre=type['Genre'].value_counts().sort_values(ascending=False)
        return f"movies according to genre are:\n{genre}"
    
    def movies_per_director(self):
       type=self.file[self.file['Type']=="Movie"]
       title=type.groupby('Director')['Title'].count()
       return f"director having most of the movie tiles is:\n{title}"

    def top_actors(self):
        top=self.file.groupby('Actor')['Title'].count().sort_values(ascending=False).head(4)
        return f"top actor who have done maximum movies are:\n{top}"
    
    
class RELEASE_TRENDS(MOVIES):
    def number_movies_per_year(self):
       plt.hist(self.file['Release Year'],color='aqua',edgecolor='blue')
       plt.xlabel('Release Year')
       plt.ylabel('Number of Movies released')
       plt.title('The number of Movies released per Year')
       plt.show()
       return f"graph displayed"


    def max_decade_movie(self):
        self.file['Decade']=(self.file['Release Year']//10)*10
        max_movie=self.file.groupby('Decade')['Title'].count().sort_values(ascending=False).head(1)
        return f"maximum movies were released in year:\n{max_movie}"
    
    def movies_per_country(self):
        country=self.file['Country'].dropna()
        plt.bar(country.values, country.index,color='orange',edgecolor='red')
        plt.xlabel("Country")
        plt.ylabel("The number of movies")
        plt.title("The number of Movies per country")
        plt.show()
        country=self.file.groupby('Country')['Title'].count().sort_values(ascending=False).head(5)
        return f"Distribution of movies per country (top 5 countries) is:{country}" 
    

class RATINGS_DURATIONS(MOVIES):
    def avg_imdbrating(self):
        self.file['IMDb Rating']=self.file['IMDb Rating'].fillna(self.file['IMDb Rating'].median())
        total=self.file['IMDb Rating'].mean()
        return f"the average IMDb rating is:{total}"
    
    def highest_movies(self):
        highest=self.file.groupby('Title')['IMDb Rating'].value_counts().sort_values()
        return highest
    
    def duration_movies_tvshows(self):
        self.file[['time','unit']]=self.file['Duration'].str.split(" ",expand=True)
        self.file['time']=pd.to_numeric(self.file['time'],errors='coerce')
        movies=self.file[self.file['Type']=="Movie"]
        tv_shows=self.file[self.file['Type']=='TV Show']
        duration_movie=movies['time'].mean()
        duration_tv=tv_shows['time'].mean()
        return f"Average duration of movies is:{duration_movie} min \n Average duration of Tv shows is:{duration_tv} seasons"
    
    def longest_movie_tvshow(self):
        self.file[['time','unit']]=self.file['Duration'].str.split(" ",expand=True)
        self.file['time']=pd.to_numeric(self.file['time'],errors='coerce')
        movies=self.file[self.file['Type']=="Movie"]
        tv_shows=self.file[self.file['Type']=='TV Show']
        duration_movie=movies['time'].max()
        duration_tv=tv_shows['time'].max()
        return f"maximum duration of a movies is: {duration_movie} min \n maximum duration of a Tv shows is: {duration_tv} seasons"
    

basics=Basic_Exploration()
content=Content_Analysis()
release=RELEASE_TRENDS()
rating=RATINGS_DURATIONS()

print()
print(basics.display())
print()
print(basics.handling_missing_values())
print()
print(basics.delete_exact_duplicates())
print()
print(content.newest_movie())
print()
print(content.oldest_movie())
print()
print(content.director_titles())
print()
print(content.count())
print()
print(content.movies_per_genre())
print()
print(content.movies_per_director())
print()
print(content.top_actors())
print()
print(release.number_movies_per_year())
print()
print(release.max_decade_movie())
print()
print(release.movies_per_country())
print()
print(rating.avg_imdbrating())
print()
print(rating.highest_movies())
print()
print(rating.duration_movies_tvshows())
print()
print(rating.longest_movie_tvshow())