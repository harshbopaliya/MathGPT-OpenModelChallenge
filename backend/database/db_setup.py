import psycopg2
from psycopg2 import sql

def create_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="mathgpt",
            user="your_username",
            password="your_password"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        return None

def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS models (
            id SERIAL PRIMARY KEY,
            filename VARCHAR(255),
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit()
        print("Tables created successfully")

if __name__ == "__main__":
    conn = create_db_connection()
    if conn:
        create_tables(conn)
        conn.close()
