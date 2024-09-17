import psycopg2
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

def create_db_connection():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        return None

def create_tables():
    """Create tables for models and performance tracking in the database."""
    conn = create_db_connection()
    if conn:
        with conn.cursor() as cur:
            # Create table for models, storing the actual model binary
            cur.execute("""
            CREATE TABLE IF NOT EXISTS models (
                id SERIAL PRIMARY KEY,
                filename VARCHAR(255),
                model BYTEA,  -- Store the model as a binary object
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
            
            # Create table for performance tracking
            cur.execute("""
            CREATE TABLE IF NOT EXISTS performance (
                id SERIAL PRIMARY KEY,
                model_id INTEGER REFERENCES models(id) ON DELETE CASCADE,
                problem TEXT,
                solution JSONB,
                prediction JSONB,
                accuracy FLOAT,
                evaluated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
            conn.commit()
            print("Tables created successfully")
        conn.close()
    else:
        print("Failed to create tables")

def save_model(filename, model):
    """Save a model to the database."""
    conn = create_db_connection()
    if conn:
        with conn.cursor() as cur:
            # Convert the model to a binary format to store in the database
            model_binary = psycopg2.Binary(model)
            
            cur.execute("""
            INSERT INTO models (filename, model) VALUES (%s, %s) RETURNING id;
            """, (filename, model_binary))
            model_id = cur.fetchone()[0]
            conn.commit()
            print(f"Model saved with ID: {model_id}")
        conn.close()
        return model_id
    else:
        print("Failed to save model")
        return None

def save_performance(model_id, problem, solution, prediction, accuracy):
    """Save performance metrics for a model to the database."""
    conn = create_db_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO performance (model_id, problem, solution, prediction, accuracy) 
            VALUES (%s, %s, %s, %s, %s);
            """, (model_id, problem, json.dumps(solution), json.dumps(prediction), accuracy))
            conn.commit()
            print("Performance saved successfully")
        conn.close()
    else:
        print("Failed to save performance")

if __name__ == "__main__":
    create_tables()
