import re
import pyodbc
from flask import Flask, render_template, session

from models.config import connection


def set_current_user(user_id):
    session["user_id"] = user_id


def get_current_user():
    user_id = session.get("user_id")
    if user_id:
        return get_user_by_id(user_id)
    return None

## קריאה נשארת כמו שיש לך:

# פונקציה מתוקנת:



def sign_up(firstName, lastName, mail, password, imgUrl):
    print(f'{firstName}, {lastName}, {mail}, {password}, {imgUrl}')
    try:
        # בדיקת סיסמה
        validation, message = is_valid(password)
        if not validation:
            raise ValueError(message)

        with connection.cursor() as cursor:
            # שימוש ב-OUTPUT INSERTED.UserID כדי לקבל את ה-ID החדש
            query = """
                INSERT INTO Users (FirstName, LastName, PasswordHash, Email, ProfilePictureURL, AccountStatus)
                OUTPUT INSERTED.UserID
                VALUES (?, ?, ?, ?, ?, ?)
            """
            values = (firstName, lastName, password, mail, imgUrl, 'Active')
            cursor.execute(query, values)

            # שליפת ה-ID של המשתמש החדש
            row = cursor.fetchone()
            if row is None:
                raise Exception("Failed to retrieve the new user ID")
            user_id = row[0]

            # שמירת השינויים במסד
            connection.commit()
            print("User added successfully!")

        # החזרת אובייקט המשתמש
        return get_user_by_id(user_id)

    except ValueError as ve:
        print(f"Validation error: {ve}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise


def sign_in(Email, password):
    with connection.cursor() as cursor:
        query = "SELECT * FROM Users WHERE Email=? AND PasswordHash=?"
        cursor.execute(query, (Email, password))
        row = cursor.fetchone()
        if row:
            return [{"UserID": row[0], "FirstName": row[1], "LastName": row[2], "PasswordHash": row[3], "Email": row[4],
                     "ProfilePictureURL": row[5], "AccountStatus": row[6], "type": "user"}]
        else:
            query = "SELECT * FROM Reporters WHERE Email=? AND PasswordHash=?"
            cursor.execute(query, (Email, password))
            row = cursor.fetchone()
            if row:
                return [{"ReporterID": row[0], "FirstName": row[1], "LastName": row[2], "PasswordHash": row[3],
                         "Email": row[4], "ProfilePictureURL": row[5], "AccountStatus": row[6],
                         "JobDescription": row[7], "type": "user"}]

        return {"type": "not user"}


def is_valid(password):
    print([c for c in password])
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    return True, "Password is valid."


def get_user_by_id(user_id):
    with connection.cursor() as cursor:
        query = "SELECT * FROM Users WHERE UserID=?"
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()
        if row:
            return {"UserID": row[0], "FirstName": row[1], "LastName": row[2],
                    "PasswordHash": row[3], "Email": row[4],
                    "ProfilePictureURL": row[5], "AccountStatus": row[6]}
        return None

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


# def sign_up():
#     with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
#          firstName=input("Enter your first name")
#          lastName=input("Enter your lastName")
#          password=input("Choose password")
#          mail=input("Enter your mail")
#          imgUrl=input("Enter your imgUrl")
#     try:
#         # Validate the password
#         validation, message = isValid(password)
#         if not validation:
#             raise ValueError(message)
#
#         # Insert user into the database
#         cursor = connection.cursor()
#         query = """
#                 INSERT INTO Users (firstName, lastName, password, mail, imgUrl, status)
#                 VALUES (%s, %s, %s, %s, %s, %s)
#             """
#         values = (firstName, lastName, password, mail, imgUrl, 'Active')
#         cursor.execute(query, values)
#         connection.commit()
#         print("User added successfully!")
#
#     except ValueError as ve:  # Catch validation errors
#         print(f"Validation error: {ve}")
#
#     except Exception as e:  # Catch all other exceptions
#         print(f"An error occurred: {e}")
