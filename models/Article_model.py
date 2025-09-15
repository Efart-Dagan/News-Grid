import pyodbc

from flask import Flask, render_template, abort
# from datetime import datetime

from models.config import connection

from datetime import datetime


def get_all_articles():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM Articles"
            cursor.execute(query)
            rows = cursor.fetchall()
            if not rows:
                return "No Articles Found"

            articles_data = []
            for row in rows:
                article_dict = {}
                for desc in cursor.description:
                    value = getattr(row, desc[0])
                    if desc[0].lower() == 'publishdate' and isinstance(value, str):
                        value = datetime.strptime(value, '%Y-%m-%d')
                    article_dict[desc[0].lower()] = value
                articles_data.append(article_dict)

    except Exception as e:
        return f"Database error: {e}"

    return articles_data


from datetime import datetime


def get_article_by_id(article_id):
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT ArticleID, Title, Content, PublishDate, CategoryID, ReporterID, Image, ViewsCount
                FROM Articles
                WHERE ArticleID = ?
            """
            cursor.execute(query, article_id)
            row = cursor.fetchone()
    except Exception as e:
        return f"Database error: {e}"

    if not row:
        return None

    article_data = {}
    for desc in cursor.description:
        value = getattr(row, desc[0])
        # המרה ל-datetime אם זה התאריך
        if desc[0].lower() == 'publishdate' and isinstance(value, str):
            value = datetime.strptime(value, '%Y-%m-%d')  # או הפורמט שלך
        article_data[desc[0].lower()] = value

    return article_data


# def add_article(Title, Content, PublishDate, CategoryID, ReporterID, ImageID, ViewsCount):
#     try:
#         with connection.cursor() as cursor:
#             query = """
#                 INSERT INTO Articles (Title, Content, PublishDate, CategoryID, ReporterID, ImageID, ViewsCount)
#                 VALUES (?, ?, ?, ?, ?, ?, ?)
#             """
#             cursor.execute(query, (Title, Content, PublishDate, CategoryID, ReporterID, ImageID, ViewsCount))
#             connection.commit()
#     except Exception as e:
#         return f"Database error: {e}"
#     return "Article added successfully"


def add_article(Title, Content, PublishDate, CategoryID, ReporterID, ImageID, ViewsCount):
    try:
        with connection.cursor() as cursor:
            # הכנסת הכתבה לטבלת Articles
            insert_article_query = """
                INSERT INTO Articles (Title, Content, PublishDate, CategoryID, ReporterID, ImageID, ViewsCount)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_article_query,
                           (Title, Content, PublishDate, CategoryID, ReporterID, ImageID, ViewsCount))

            # חייבים לבצע commit לפני קריאה ל-SCOPE_IDENTITY כדי להבטיח שהשורה נשמרה
            connection.commit()

            # שליפת ה-ID של הכתבה החדשה
            cursor.execute("SELECT SCOPE_IDENTITY()")
            new_article_id = cursor.fetchone()[0]

            print(f"✅ נוצרה כתבה חדשה עם ID: {new_article_id}")

            # הכנסת קשר בין כתב לכתבה
            insert_relation_query = """
                INSERT INTO ReporterArticle (ReporterID, ArticleID)
                VALUES (?, ?)
            """
            cursor.execute(insert_relation_query, (ReporterID, new_article_id))
            connection.commit()

    except Exception as e:
        print(f"❌ שגיאת DB: {e}")
        return f"Database error: {e}"

    return {
        "message": "Article and relation saved successfully",
        "article_id": new_article_id,
        "reporter_id": ReporterID
    }
