import psycopg2

# Database connection parameters
dbname = "Claudia"
user = "Marc"
password = "#G3heim123"
host = "192.168.178.4"
port = "5432"

SQL1 = "select count(*) from projects.series_import"
SQL2 = "select count(*) from projects.movies_import"

try:
  connection = psycopg2.connect(dbname=dbname, host=host, port=port, user=user, password=password)

  # Print connection details (optional)
  print("Connection established successfully!")
  print(f"Database name: {connection.info.dbname}")
  print(f"Username: {connection.info.user}")
  print(f"Host: {connection.info.host}")
  print(f"Port: {connection.info.port}")
  print()

  with connection:
      with connection.cursor() as curs:
          curs.execute(SQL1)
          for record in curs:
            print(record)

  with connection:
      with connection.cursor() as curs:
          curs.execute(SQL2)
          for record in curs:
            print(record)

except Exception as e:
  print("Error connecting to database:", e)

finally:
  if connection:
    connection.close()
    print("Database connection closed.")