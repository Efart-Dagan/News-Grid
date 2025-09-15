# import pyodbc
# from flask import Flask, render_template, request, redirect, url_for
# from models import login_model, Article_model
# from models.Reporters_model import get_reporter_info_by_id
# from models.Category_model import get_category_by_id , add_category ,get_all_categories
#
# app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')
# app.secret_key = "any_secret_key_you_like"
#
# # conn_str = "DRIVER={SQL Server};SERVER=RIVI;DATABASE=news"
# conn_str = "DRIVER={SQL Server};SERVER=RIVI;DATABASE=news;"
#
#
# @app.route('/login.html', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         print("hello")
#         username = request.form['username']
#         password = request.form['password']
#         user = login_model.sign_in(username, password)
#         if user and user[0]['type'] == 'user':
#             return redirect(url_for('index'))
#         else:
#             return redirect(url_for('index'))
#     return render_template('login.html')
#
#
# @app.route('/')
# def index():
#     articles = Article_model.get_all_articles()
#     return render_template('index.html', articles=articles)
#
#
# @app.route('/article/<int:article_id>')
# def article_details(article_id):
#     article = Article_model.get_article_by_id(article_id)
#     if not article:
#         return "Article not found"
#     reporter = get_reporter_info_by_id(article['reporterid'])
#     category = get_category_by_id(article['categoryid'])
#     return render_template("article.html", article=article, reporter=reporter, category=category)
#
#
#
# @app.route("/add_article", methods=["GET", "POST"])
# def add_article_page():
#     if request.method == "POST":
#         title = request.form["title"]
#         content = request.form["content"]
#         publishdate = request.form["publishdate"]
#         categoryid = request.form["categoryid"]
#         reporterid = request.form["reporterid"]
#         imageid = request.form.get("imageid")
#         viewscount = request.form.get("viewscount", 0)
#
#         result = Article_model.add_article(title, content, publishdate, categoryid, reporterid, imageid, viewscount)
#         print(result)
#         return redirect(url_for("index"))  # אחרי שמירה נחזור לעמוד הבית
#
#     return render_template("add_article.html")
#
# from flask import request, redirect, url_for, flash
#
# @app.route('/add_category', methods=['GET', 'POST'])
# def add_category_page():
#     if request.method == 'POST':
#         name = request.form['categoryName']
#         desc = request.form['categoryDescription']
#         result = add_category(name, desc)
#         if "successfully" in result:
#             flash("Category added successfully!", "success")
#             return redirect(url_for('index'))  # או לעמוד שבו רוצים לחזור
#         else:
#             flash(result, "danger")
#
#     return render_template('add_category.html')
#
#
# @app.route("/add_article", methods=["GET", "POST"])
# def add_article_page():
#     categories = get_all_categories()  # שליפת כל הקטגוריות
#     if request.method == "POST":
#         title = request.form["title"]
#         content = request.form["content"]
#         category_id = request.form["category"]  # נקבל את ה-id של הקטגוריה
#         # ... שאר השדות
#         result = Article_model.add_article(title, content, category_id, ...)
#         return redirect(url_for("index"))
#
#     return render_template("add_article.html", categories=categories)
#
#
# if __name__ == '__main__':
#     app.run(port=300)
#
# # with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #     cursor = connection.cursor()  # סמן באמצעותו נריץ שאילתות ונשלוף את תוצאות השאילתא
# #     query = "SELECT * FROM Employee_tbl"
# #     cursor.execute(query)  # הרצת השאילתא
# #     data = cursor.fetchall()  # שליפת השורות בטבלת התוצאה
# #     print(data)
#
#
# # select one by one
#
#
# # select, insert, update, delete
# # insert
# # with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #     cursor = connection.cursor()
# #     query = "INSERT INTO Employee_tbl VALUES('2545687', 'Cohen', 'Rivka', '65847', '054-8542367', 'Rabbi Akiva 64', 'Petach Tikva', 6, '2015-05-12', 9)"
# #     cursor.execute(query)
# #     print(cursor.rowcount)  # מס' השורות שהושפעו כתוצאה מהשאילתא
#
#
# # insert with parameters - 1. using format string
# # with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #     name = input("Enter your name: ")
# #     position = input("Enter your position: ")
# #     cursor = connection.cursor()
# #     query = f"INSERT INTO Employee_tbl VALUES('6594784', 'Cohen', '{name}', '65847', '054-8542367', 'Rabbi Akiva 64', 'Petach Tikva', {position}, '2015-05-12', 9)"
# #     cursor.execute(query)
# #     print(cursor.rowcount)
#
#
# # insert with parameters - 2. using ?
# # with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #     name = input("Enter your name: ")
# #     position = input("Enter your position: ")
# #     cursor = connection.cursor()
# #     query = "INSERT INTO Employee_tbl VALUES('658452', 'Cohen', ?, '65847', '054-8542367', 'Rabbi Akiva 64', 'Petach Tikva', ?, '2015-05-12', 9)"
# #     cursor.execute(query, (name, position))
# #     print(cursor.rowcount)
#
#
# # update
# # with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #     cursor = connection.cursor()
# #     query = "select * from Users"
# #     cursor.execute(query)
# #     print(cursor.rowcount)
# #
#
# # # delete
#
# # def DeleteUserByPaF():
# #     with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #         cursor = connection.cursor()
# #         userName=input("הכנס שם פרטי משתמש למחיקה")
# #         userPassword=input("הכנס סיסמת משתמש למחיקה")
# #         query = f"DELETE Users WHERE FirstName='{userName}' and PasswordHash='{userPassword}'"
# #         if cursor.rowcount!=1:
# #             print("oops first name or password is wrong")
# #         cursor.execute(query)
#
#
# # def getAllUserByNamePassword():
# #    with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #         cursor = connection.cursor()  # סמן באמצעותו נריץ שאילתות ונשלוף את תוצאות השאילתא
# #         name =input("הכנס שם פרטי")
# #         password =input("הכנס סיסמא")
# #         query = f"SELECT * FROM Users where FirstName='{name}' and PasswordHash='{password}'"
# #         cursor.execute(query)  # הרצת השאילתא
# #         row = cursor.fetchone()  # שליפת השורות בטבלת התוצאה
# #         if row:
# #             print(row)
# #         else:
# #            print("oopsssss")
#
# # cnt = 1
#
# # while cnt <= 5 and row!=None:
# #    print(row)
# #    row = cursor.fetchone()
# #    cnt += 1
#
# ##עובד
# # שליפת נתונים
# # def getAllUsers():
# #      with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #        cursor = connection.cursor()  # סמן באמצעותו נריץ שאילתות ונשלוף את תוצאות השאילתא
# #        query = "SELECT * FROM Users"
# #        cursor.execute(query)  # הרצת השאילתא
# #        row = cursor.fetchone()  # שליפת השורות בטבלת התוצאה
# #        cnt = 1
# #        while cnt <= 5 and row!=None:
# #           print(row)
# #           row = cursor.fetchone()
# #           cnt += 1
#
#
# # getAllUsers()
# ##הכנסת משתמש
#
# # def insertUser():
# #
# #     with pyodbc.connect(conn_str) as connection:  # יצירת החיבור לDB
# #          firstName=input("Enter your first name")
# #          lastName=input("Enter your lastName")
# #          password=input("Enter your password")
# #          mail=input("Enter your mail")
# #          imgUrl=input("Enter your imgUrl")
# #          cursor = connection.cursor()
# #          query = f"INSERT INTO Users VALUES('{firstName}', '{lastName}', {password},'{mail}',{imgUrl},'Active')"
# #          cursor.execute(query)
#
#
# # insertUser()
# # getAllUsers()
# # getAllUserByNamePassword()
# # DeleteUserByPaF()
# #
import pyodbc
from flask import Flask, render_template, request, redirect, url_for, flash
from models import login_model, Article_model
from models.Reporters_model import get_reporter_info_by_id
from models.Category_model import get_category_by_id, add_category, get_all_categories
from models.login_model import isValid
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')
app.secret_key = "any_secret_key_you_like"

conn_str = "DRIVER={SQL Server};SERVER=RIVI;DATABASE=news;"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login_model.sign_in(username, password)
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/signup', methods=['POST'])
def signup_route():  # שם שונה מהפונקציה login_model.sign_up
    # כאן תקרא ל-login_model.sign_up
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    mail = request.form['mail']
    password = request.form['password']
    imgUrl = request.form['imgUrl']

    try:
        user = login_model.sign_up(firstName, lastName, mail, password, imgUrl)
        return redirect(url_for('login'))
    except Exception as e:
        return render_template('login.html', signup_error=str(e))


@app.route('/')
def index():
    articles = Article_model.get_all_articles()
    return render_template('index.html', articles=articles)


# @app.route('/signup', methods=['POST'])
# def signup():
#     try:
#         with pyodbc.connect(conn_str) as connection:
#             firstName = request.form['firstName']
#             lastName = request.form['lastName']
#             password = request.form['password']
#             mail = request.form['mail']
#             imgUrl = request.form['imgUrl']
#
#             # Validate the password
#             validation, message = isValid(password)
#             if not validation:
#                 raise ValueError(message)
#
#             cursor = connection.cursor()
#             query = """
#                     INSERT INTO Users (firstName, lastName, password, mail, imgUrl, status)
#                     VALUES (?, ?, ?, ?, ?, ?)
#                 """
#             values = (firstName, lastName, password, mail, imgUrl, 'Active')
#             cursor.execute(query, values)
#             connection.commit()
#
#         return redirect(url_for('login'))  # אחרי הרשמה מעבירים למסך login
#
#     except ValueError as ve:
#         return f"Validation error: {ve}", 400
#     except Exception as e:
#         return f"An error occurred: {e}", 500
#

@app.route('/article/<int:article_id>')
def article_details(article_id):
    article = Article_model.get_article_by_id(article_id)
    print(article)
    if not article:
        return "Article not found"
    reporter = get_reporter_info_by_id(article['reporterid'])
    category = get_category_by_id(article['categoryid'])
    return render_template("article.html", article=article, reporter=reporter, category=category)


@app.route('/add_category', methods=['GET', 'POST'])
def add_category_page():
    if request.method == 'POST':
        name = request.form['categoryName']
        desc = request.form['categoryDescription']
        result = add_category(name, desc)
        if "successfully" in result:
            flash("Category added successfully!", "success")
            return redirect(url_for('index'))
        else:
            flash(result, "danger")
    return render_template('add_category.html')


@app.route("/add_article", methods=["GET", "POST"])
def add_article_page():
    categories = get_all_categories()  # שליפת כל הקטגוריות
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        publishdate = request.form["publishdate"]
        reporterid = request.form["reporterid"]
        imageid = request.form.get("imageid")
        viewscount = request.form.get("viewscount", 0)

        # קח את ה-ID של הקטגוריה
        category_id_str = request.form.get("category")  # name מה-select
        if not category_id_str:
            flash("יש לבחור קטגוריה!", "danger")
            return redirect(url_for("add_article_page"))
        CategoryID = int(category_id_str)

        result = Article_model.add_article(title, content, publishdate, CategoryID, reporterid, imageid, viewscount)
        print(result)
        return redirect(url_for("index"))

    return render_template("add_article.html", categories=categories)


if __name__ == '__main__':
    app.run(port=300)
