import config
import psycopg

with psycopg.connect(
    dbname=config.PGDATABASE,
    user=config.PGUSER,
    password=config.PGPASSWORD,
    host=config.PGHOST,
    port=5432,
) as connection:

    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS brand (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50)      NOT NULL     UNIQUE
            )
        """
        cursor.execute(query)

        query_insert = "INSERT INTO brand (name) VALUES (%s)"
        cursor.execute(query_insert, ('Nissan', ))




