from database import execute_sql_query

def get_all_pricing_plans():
    query = "SELECT id, name, description, price, details, is_popular FROM pricing_plans ORDER BY id"
    return execute_sql_query(query)
