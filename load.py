import psycopg2
from config import *

def load_data(data):
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    cursor = conn.cursor()

    for _, row in data.iterrows():

        cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        order_id INTEGER,
        customer_name VARCHAR(100),
        product VARCHAR(100),
        quantity INTEGER,
        price NUMERIC,
        total_amount NUMERIC
    )
""")



        
        cursor.execute(
            """
            INSERT INTO sales
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (
                row["order_id"],
                row["customer_name"],
                row["product"],
                row["quantity"],
                row["price"],
                row["total_amount"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded into Supabase PostgreSQL successfully.")
