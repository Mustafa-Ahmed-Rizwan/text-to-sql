import sqlite3

#create database
connection = sqlite3.connect('student.db')

#create a cursor
cursor=connection.cursor()

# Create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS STUDENT (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(25),
    COURSE VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INTEGER
);
"""
cursor.execute(create_table_query)

# insert records into the table
insert_query = """
INSERT INTO STUDENT (NAME, COURSE, SECTION, MARKS) VALUES (?, ?, ?, ?) """
values=[
    ('John Doe', 'Computer Science', 'A', 85),
    ('Jane Smith', 'Mathematics', 'B', 90),
    ('Alice Johnson', 'Physics', 'A', 78),
    ('Bob Brown', 'Chemistry', 'C', 88)
]
cursor.executemany(insert_query, values)
# Commit the changes
connection.commit()

data=cursor.execute("""SELECT * FROM STUDENT""")
# Fetch all records
for row in data:
    print(row)
# Close the connection
if connection:
    connection.close()
    