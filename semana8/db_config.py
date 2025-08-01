import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="WEYDUjdhdcjsl1903Q###",
        database="videojuegos_db",
        port=3307
    )
    return connection