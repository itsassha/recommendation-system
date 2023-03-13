# Connect library
import pyodbc
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Connect to SQL database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=server_name;DATABASE=db_name;UID=username;PWD=password')

# Retrieve data from SQL
sql_query = "SELECT user_id, item_id, rating FROM ratings_table"
df = pd.read_sql(sql_query, conn)

# Clean and preprocess data
df.dropna(inplace = True)
df['user_id'] = df['user_id'].astype('category')
df['item_id'] = df['item_id'].astype('category')

# Split data into training and testing sets
train_data, test_data = train_test_split(df, test_size = 0.2)

# Convert data to sparse matrix format
train_sparse_matrix = csr_matrix((train_data['rating'].astype(float), (train_data['user_id'].cat.codes, train_data['item_id'].cat.codes)))
test_sparse_matrix = csr_matrix((test_data['rating'].astype(float), (test_data['user_id'].cat.codes, test_data['item_id'].cat.codes)))

# Compute cosine similarity between items
item_similarity = cosine_similarity(train_sparse_matrix.T)

# Make recommendations for new users
def get_item_recommendations(user_id):
    user_index = train_data['user_id'].cat.codes[user_id]
    item_scores = item_similarity.dot(train_sparse_matrix[user_index].T).toarray().reshape(-1)
    sorted_items = sorted(zip(train_data['item_id'].cat.categories, item_scores), key=lambda x: -x[1])
    return sorted_items

# Test the model on a new user
user_id = 100
recommended_items = get_item_recommendations(user_id)[:10]
print(f"Recommended items for user {user_id}: {recommended_items}")
