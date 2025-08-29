from database import execute_sql_query

def get_all_features():
    query = "SELECT id, title, description, image_url, is_active FROM features WHERE is_active = TRUE ORDER BY id"
    return execute_sql_query(query)
