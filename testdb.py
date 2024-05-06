import sqlite3

def view_database_details(database_name):
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Get tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        print("Tables in the database:")
        for table in tables:
            print(table[0])

        print("\nValues in each table:")
        for table in tables:
            print(f"\nTable: {table[0]}")
            cursor.execute(f"SELECT * FROM {table[0]};")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    database_name = "main.db"  # Replace with the name of your SQLite database
    view_database_details(database_name)
