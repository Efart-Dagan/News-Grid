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

