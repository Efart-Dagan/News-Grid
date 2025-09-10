import re
import pyodbc
from flask import Flask, render_template
conn_str = "DRIVER={SQL Server};SERVER=RIVI;DATABASE=news"


app=Flask(__name__,static_url_path='',static_folder='static',template_folder='template')




import pyodbc

# def sign_in():
#     with pyodbc.connect(conn_str) as connection:  # יצירת החיבור ל-DB
#         cursor = connection.cursor()
#         name = input("הכנס שם פרטי: ")
#         password = input("הכנס סיסמא: ")

#         # חיפוש בטבלת Users
#         query = f"SELECT * FROM Users WHERE FirstName={name} AND PasswordHash={password}"
#         cursor.execute(query, (name, password))  # שימוש בפרמטרים למניעת SQL Injection
#         row = cursor.fetchone()

#         if row:
#             columns = [column[0] for column in cursor.description]  # שליפת שמות העמודות
#             user_data = dict(zip(columns, row))  # יצירת מילון מהתוצאה
#             return {"role": "user", "data": user_data}

#         # חיפוש בטבלת article
#         query = f"SELECT * FROM article WHERE FirstName={name} AND PasswordHash={password}"
#         cursor.execute(query, (name, password))
#         row = cursor.fetchone()

#         if row:
#             columns = [column[0] for column in cursor.description]
#             reporter_data = dict(zip(columns, row))
#             return {"role": "reporter", "data": reporter_data}

#         return False


def sign_in(username,password):
    with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
        cursor = connection.cursor()  # סמן באמצעותו נריץ שאילתות ונשלוף את תוצאות השאילתא
        # name = input("הכנס שם פרטי")
        # password = input("הכנס סיסמא")
        query = f"SELECT * FROM Users where FirstName='{username}' and PasswordHash='{password}'"
        cursor.execute(query)  # הרצת השאילתא
        row = cursor.fetchone()  # שליפת השורות בטבלת התוצאה
        if row:
            return [{"UserID":row[0],"FirstName":row[1],"LastName":row[2],"PasswordHash":row[3],"Email":row[4],"ProfilePictureURL":row[5],"AccountStatus":row[6],"type":"user"}]
        else:
             query = f"SELECT * FROM Article where FirstName='{username}' and PasswordHash='{password}'"
             cursor.execute(query)  # הרצת השאילתא
             row = cursor.fetchone()
             if row:
                 return [{"ReporterID": row[0], "FirstName": row[1], "LastName": row[2], "PasswordHash": row[3],
                          "Email": row[4], "ProfilePictureURL": row[5], "AccountStatus": row[6],
                          "JobDescription": row[7], "type": "user"}]

        return {"type":"not user"}

            
            



def sign_up():
    with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
         firstName=input("Enter your first name")
         lastName=input("Enter your lastName")
         password=input("Choose password")
         mail=input("Enter your mail")
         imgUrl=input("Enter your imgUrl")
    try:
        # Validate the password
        validation, message = isValid(password)
        if not validation:
            raise ValueError(message)

        # Insert user into the database
        cursor = connection.cursor()
        query = """
                INSERT INTO Users (firstName, lastName, password, mail, imgUrl, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
        values = (firstName, lastName, password, mail, imgUrl, 'Active')
        cursor.execute(query, values)
        connection.commit()
        print("User added successfully!")

    except ValueError as ve:  # Catch validation errors
        print(f"Validation error: {ve}")

    except Exception as e:  # Catch all other exceptions
        print(f"An error occurred: {e}")


def isValid(password):
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."

        # Check if the password has at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."

        # Check if the password has at least one digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."

        # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    return True





