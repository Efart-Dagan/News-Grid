import pyodbc

conn_str = "DRIVER={SQL Server};SERVER=RIVI;DATABASE=news"
connection = pyodbc.connect(conn_str)