from models.config import connection


def get_category_by_id(category_id):
    with connection.cursor() as cursor:
        query = "SELECT * FROM Categories WHERE CategoryID = ?"
        cursor.execute(query, (category_id,))
        row = cursor.fetchone()
        if not row:
            return None
        category_data = {desc[0].lower(): getattr(row, desc[0]) for desc in cursor.description}
        return category_data


def add_category(CategoryName, CategoryDescription):
    try:
        with connection.cursor() as cursor:
            query = """
                    INSERT INTO Categories (CategoryName, CategoryDescription)
                    VALUES (?, ?)
                """
            cursor.execute(query, (CategoryName, CategoryDescription))
            connection.commit()
    except Exception as e:
        return f"Database error: {e}"

    return "Category added successfully"

def get_all_categories():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM Categories"  # בדוק שהשם של הטבלה נכון
            cursor.execute(query)
            categories = cursor.fetchall()  # מחזיר רשימה של טאפלים או dicts, תלוי בהגדרת cursor
            return categories
    except Exception as e:
        print(f"Database error: {e}")
        return []
