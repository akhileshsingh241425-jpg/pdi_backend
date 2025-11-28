"""
Database initialization script
Run this to create the MySQL database
"""
import pymysql
import sys

def create_database():
    try:
        # Connect to MySQL server (without specifying database)
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        
        with connection.cursor() as cursor:
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS pdi_database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✓ Database 'pdi_database' created successfully!")
            
            # Use the database
            cursor.execute("USE pdi_database")
            
            # Show tables
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print(f"✓ Current tables: {len(tables)}")
            
        connection.commit()
        connection.close()
        
        print("\n✓ Database initialization complete!")
        print("\nNext steps:")
        print("1. Run: pip install -r requirements.txt")
        print("2. Start server: python run.py")
        print("\nThe Flask app will automatically create tables on startup.")
        
    except Exception as e:
        print(f"✗ Error creating database: {e}")
        sys.exit(1)

if __name__ == '__main__':
    create_database()
