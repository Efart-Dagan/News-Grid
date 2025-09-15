import pyodbc

conn_str = "DRIVER={SQL Server};SERVER=DESKTOP-F6TEN9G;DATABASE=news"
connection = pyodbc.connect(conn_str)