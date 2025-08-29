from database import execute_sql_query

def save_contact_message(name, email, subject, message):
    query = """
    INSERT INTO contacts (name, email, subject, message) 
    VALUES (%s, %s, %s, %s)
    RETURNING id
    """
    return execute_sql_query(query, (name, email, subject, message))

def save_newsletter_subscription(email):
    query = """
    INSERT INTO newsletter_subscribers (email, subscribed_at) 
    VALUES (%s, CURRENT_TIMESTAMP)
    RETURNING id
    """
    return execute_sql_query(query, (email,))
