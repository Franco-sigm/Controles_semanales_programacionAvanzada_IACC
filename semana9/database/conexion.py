import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="WEYDUjdhdcjsl1903Q###",
        database="saludtotal",
        port=3307
    )
