# college_database.py

import mysql.connector
from mysql.connector import Error


def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # Change if needed
            password="password",  # Change to your MySQL password
            database="College"
        )

        if connection.is_connected():
            print("Connected to College database.")

            cursor = connection.cursor()

            # Total students
            cursor.execute("SELECT COUNT(*) FROM School;")
            total_students = cursor.fetchone()[0]
            print(f"\nTotal Students: {total_students}")

            # Display first 10 students
            cursor.execute("SELECT * FROM School LIMIT 10;")
            rows = cursor.fetchall()

            print("\nFirst 10 Students")
            print("-" * 80)

            for row in rows:
                print(row)

            # Example search
            student_id = 1001
            cursor.execute(
                "SELECT * FROM School WHERE student_id = %s",
                (student_id,)
            )

            student = cursor.fetchone()

            print("\nSearch Result")
            print("-" * 80)

            if student:
                print(student)
            else:
                print("Student not found.")

            # Average marks
            cursor.execute("SELECT AVG(marks) FROM School;")
            average_marks = cursor.fetchone()[0]

            print(f"\nAverage Marks: {average_marks:.2f}")

            # Top 5 students
            cursor.execute("""
                SELECT student_id, name, marks
                FROM School
                ORDER BY marks DESC
                LIMIT 5
            """)

            top_students = cursor.fetchall()

            print("\nTop 5 Students")
            print("-" * 80)

            for student in top_students:
                print(student)

    except Error as e:
        print("Database Error:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("\nDatabase connection closed.")


if __name__ == "__main__":
    connect_database()
