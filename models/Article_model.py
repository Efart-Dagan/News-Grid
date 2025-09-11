import pyodbc

from flask import Flask, render_template, abort
# from datetime import datetime

from models.config import connection


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
                article_dict = {desc[0].lower(): getattr(row, desc[0]) for desc in cursor.description}
                articles_data.append(article_dict)

    except Exception as e:
        return f"Database error: {e}"

    return articles_data  # מחזיר רשימה של מילונים


def get_article_by_id(article_id):
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT ArticleID, Title, Content, PublishDate, CategoryID, ReporterID, ImageID, ViewsCount
                FROM Articles
                WHERE ArticleID = ?
            """
            cursor.execute(query, article_id)
            row = cursor.fetchone()
    except Exception as e:
        return f"Database error: {e}"

    if not row:
        return None

    article_data = {desc[0].lower(): getattr(row, desc[0]) for desc in cursor.description}
    return article_data

def add_article(Title, Content, PublishDate, CategoryID, ReporterID, ImageID, ViewsCount):

