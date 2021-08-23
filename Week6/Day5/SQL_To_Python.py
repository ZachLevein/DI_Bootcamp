import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Nanach123'
DATABASE = 'MCA'

# Using those details, we can now create a connection object:
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

# Think of this as the place that runs your queries, kind like the pgAdmin query tool.
cursor = connection.cursor()

# Now a query can be defined
query = 'SELECT biz_name FROM business LIMIT 30';

# submit the query to the cursor to execute 
cursor.execute(query)

# The cursor now contains the query results 
query_results = cursor.fetchall()

# Closing the database
connection.close()
