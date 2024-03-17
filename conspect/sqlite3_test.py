import sqlite3

DB_NAME = "sqlite_db.db"

with sqlite3.connect(DB_NAME) as sqlite_conn:
      sql_request = "SELECT * FROM courses WHERE reviews_qty >= 30;"
      sql_cursor = sqlite_conn.execute(sql_request) 
    #   for record in sql_cursor:
    #       print(record[1])
      records = sql_cursor.fetchall()    
      print(records)    



# Add records to the table
# courses = [
#     (1, "Python course", 100, 30),  # id, title, students_qty, reviews_qty 
#     (2, "Java course", 150, 40),
#     (3, "C++ course", 200, 50),
#     (4, "C# course", 250, 60),
#     (5, "Ruby course", 300, 70)         
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     # Убедитесь, что передаете данные, соответствующие структуре таблицы.
#     # В вашем запросе на вставку 4 параметра, но они должны соответствовать столбцам в таблице
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()




# # Create new table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)

