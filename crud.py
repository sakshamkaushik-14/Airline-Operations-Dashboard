import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user = 'root',
        password = '',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print('Connection established')
except:
    print('Connection error')

# Search/Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# Update
mycursor.execute("""
UPDATE airport
SET name = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)


