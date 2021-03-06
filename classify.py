import pandas as pd
import numpy as np
import json
import nltk
import re
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# %matplotlib inline
pd.set_option('display.max_colwidth', 300)

meta = pd.read_csv("movie.metadata.tsv", sep = '\t', header = None)
# print (meta.head())

# rename columns
meta.columns = ["movie_id",1,"movie_name",3,4,5,6,7,"genre"]

plots = []

with open("plot_summaries.txt", 'r', encoding="utf8") as f:
  reader = csv.reader(f, dialect='excel-tab')
  for row in tqdm(reader):
    plots.append(row)

movie_id = []
plot = []

# extract movie Ids and plot summaries
for i in tqdm(plots):
  movie_id.append(i[0])
  plot.append(i[1])

# create dataframe
movies = pd.DataFrame({'movie_id': movie_id, 'plot': plot})

# change datatype of 'movie_id'
meta['movie_id'] = meta['movie_id'].astype(str)

# merge meta with movies
movies = pd.merge(movies, meta[['movie_id', 'movie_name', 'genre']], on = 'movie_id')

# an empty list
genres = []

# extract genres
for i in movies['genre']:
  genres.append(list(json.loads(i).values()))

# add to 'movies' dataframe
movies['genre_new'] = genres

# print (movies.head())

# remove samples with 0 genre tags
movies_new = movies[~(movies['genre_new'].str.len() == 0)]
print (movies_new.shape, movies.shape)

# get all genre tags in a list
all_genres = sum(genres,[])
print(len(set(all_genres)))

all_genres = nltk.FreqDist(all_genres)

# create dataframe
all_genres_df = pd.DataFrame({'Genre': list(all_genres.keys()),
                              'Count': list(all_genres.values())})


g = all_genres_df.nlargest(columns="Count", n = 50)
plt.figure(figsize=(12,15))
ax = sns.barplot(data=g, x= "Count", y = "Genre")
ax.set(ylabel = 'Count')
plt.show()