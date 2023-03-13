# recommendation-system

1) Connecting to the SQL database
We establish a connection to the SQL database using the pyodbc library. We provide the necessary connection information, such as server name, database name, username and password.

2) Extracting data from SQL
We extract the rating data from SQL using an SQL query and store it in a pandas data frame.

3) Data cleaning and preprocessing
We clean up the data by deleting all rows with missing values. Then we convert the user_id and item_id columns into categorical variables. Categorical variables can be encoded as integers to improve performance and reduce memory usage.

4) Separation of data into training and test sets
We divided the data into training and test sets using the train_test_split function from sklearn.

5) Data conversion to sparse matrix format
We convert the training and testing data into a sparse matrix format using the csr_matrix function from scipy. A sparse matrix is a matrix with a large number of zero values, which is a common scenario in recommendation systems. Sparse matrices can be stored more efficiently than dense matrices, and you can work with them faster.

6) Calculation of cosine similarity between elements
We calculate the cosine similarity between the elements in the training data using the cosine_similarity function from sklearn. Cosine similarity is a measure of similarity between two nonzero vectors. In the context of recommendation systems, it is an indicator of how similar two elements are based on how users rated them.

7) We give recommendations to new users
We define a function named get_item_recommendations, which takes the user ID as input and returns a list of recommended products based on their similarity to the products that the user rated highly. We calculate the similarity between the user-evaluated elements and all other elements in the training data using cosine similarity estimates that we calculated earlier. Then we sort the products by their degree of similarity and return the N best products as recommendations.

8) Testing the model on a new user
We are testing the model by generating recommendations for a new user with ID 100. We call the get_item_recommendations function with user ID 100, and it returns a list of recommended items.

---

1) Подключение к базе данных SQL
Мы устанавливаем соединение с базой данных SQL, используя библиотеку pyodbc. Мы предоставляем необходимые сведения о подключении, такие как имя сервера, имя базы данных, имя пользователя и пароль.

2) Извлечение данные из SQL
Мы извлекаем данные рейтинга из SQL с помощью SQL-запроса и храним их в фрейме данных pandas.

3) Очистка и предварительная обработка данных
Мы очищаем данные, удаляя все строки с отсутствующими значениями. Затем мы преобразуем столбцы user_id и item_id в категориальные переменные. Категориальные переменные могут быть закодированы в виде целых чисел для повышения производительности и уменьшения использования памяти.

4) Разделение данных на обучающие и тестовые наборы
Мы разделили данные на обучающий и тестовый наборы, используя функцию train_test_split от sklearn.

5) Преобразование данных в формат разреженной матрицы
Мы преобразуем данные обучения и тестирования в формат разреженной матрицы, используя функцию csr_matrix от scipy. Разреженная матрица - это матрица с большим количеством нулевых значений, что является распространенным сценарием в рекомендательных системах. Разреженные матрицы могут храниться более эффективно, чем плотные матрицы, и с ними можно работать быстрее.

6) Вычисление косинусного сходство между элементами
Мы вычисляем косинусное сходство между элементами в обучающих данных, используя функцию cosine_similarity от sklearn. Косинусное сходство - это мера сходства между двумя ненулевыми векторами. В контексте систем рекомендаций это показатель того, насколько похожи два элемента, основанный на том, как пользователи оценили их.

7) Даем рекомендации новым пользователям
Мы определяем функцию с именем get_item_recommendations, которая принимает идентификатор пользователя в качестве входных данных и возвращает список рекомендуемых товаров на основе их сходства с товарами, которые пользователь высоко оценил. Мы вычисляем сходство между оцененными пользователем элементами и всеми другими элементами в обучающих данных, используя оценки косинусного сходства, которые мы вычислили ранее. Затем мы сортируем товары по степени их сходства и возвращаем N лучших товаров в качестве рекомендаций.

8) Тестируем модель на новом пользователе
Мы тестируем модель, генерируя рекомендации для нового пользователя с идентификатором 100. Мы вызываем функцию get_item_recommendations с идентификатором пользователя 100, и она возвращает список рекомендуемых элементов.
