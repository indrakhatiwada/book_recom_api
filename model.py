import numpy as np
import pandas as pd


books = pd.read_csv('books.csv',sep=";",error_bad_lines =False, encoding ='latin-1')

books.head()


books.columns

books = books[['ISBN','Book-Title','Book-Author', 'Year-Of-Publication', 'Publisher',]]

books.head(2)

books.rename(columns = {'Book-Title': 'title','Book-Author':'author', 'Year-Of-Publication': 'year','Publisher': 'publisher' },inplace= True)

books.head(2)

users = pd.read_csv('users.csv', sep=";",error_bad_lines = False, encoding ='latin-1')


users.rename(columns={'User-ID':'user_id', 'Location': 'location','Age':'age'},inplace= True)
users.head()


ratings = pd.read_csv('ratings.csv', sep=";",error_bad_lines = False, encoding='latin-1')

ratings.head(2)



ratings.head(2)



books.shape



users.shape

ratings.shape


ratings.head(2)



ratings.rename(columns= {'User-ID': 'user_id',  'Book-Rating':'ratings'}, inplace= True)


ratings.head(2)

ratings.head(2)

x = ratings['user_id'].value_counts() > 200

y = x[x].index

y

ratings.head(2)

ratings = ratings[ratings['user_id'].isin(y)]

ratings.shape

ratings.head()

rating_with_books = ratings.merge(books, on="ISBN")

rating_with_books.shape

number_rating = rating_with_books.groupby('title')['ratings'].count().reset_index()

number_rating.rename(columns={'ratings':'number of rating'}, inplace = True)

final_rating = rating_with_books.merge(number_rating, on='title')


final_rating.shape

final_rating =final_rating[final_rating['number of rating']>=50]

final_rating.shape

#remove duplicate entries
final_rating.drop_duplicates(['user_id','title'],inplace= True)

final_rating.head(2)

book_pivot = final_rating.pivot_table(columns="user_id", index="title",values='ratings')

book_pivot.fillna(0, inplace=True)


book_pivot

from scipy.sparse import csr_matrix
book_sparse = csr_matrix(book_pivot)
#changes book pivot to sparse matrix

type(book_sparse)

from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(algorithm = 'brute')


model.fit(book_sparse)

distances,suggestions = model.kneighbors(book_pivot.iloc[237,:].values.reshape(1,-1), n_neighbors=6)

suggestions

for i in range(len (suggestions)):
    print(book_pivot.index[suggestions[i]])

np.where(book_pivot.index == 'Animal Farm')[0][0]


def recommend_book(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances,suggestions = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
    return (book_pivot.index[suggestions[i]])

# recommend_book('Animal Farm')

# recommend_book('Second Nature')

# recommend_book('Harry Potter and the Chamber of Secrets (Book 2)')

# recommend_book('The Cradle Will Fall')




# recommend_book('Animal Farm')

# recommend_book("Harry Potter and the Goblet of Fire (Book 4)")


