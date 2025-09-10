import pyodbc
from flask import Flask, render_template
from models.config import connection


def get_reporter_info_by_id(reporter_id):
    with connection.cursor() as cursor:
        query = "SELECT * FROM Reporters WHERE ReporterID = ?"
        cursor.execute(query, (reporter_id,))
        row = cursor.fetchone()
        if not row:
            return None
        reporter_data = {desc[0].lower(): getattr(row, desc[0]) for desc in cursor.description}
        return reporter_data


# def get_student_info(firstName, lastName):
#     with connection.cursor() as cursor:
#         query = f"select * from Reporters where FirstName  = '{firstName}' and LastName='{lastName}';"
#         cursor.execute(query)
#         res = cursor.fetchall()
#         return res[0]
