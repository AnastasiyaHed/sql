# Разобраться  с библиотекой psycopg2

import psycopg2

# Соединение с базой данных
conn = psycopg2.connect(
    host="127.0.0.1",
    database="admindb",
    user="admin",
    password="admin"
)

# Создание таблицы студентов
create_students_table = """
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL,
    gender VARCHAR(10) NOT NULL
);
"""

# Создание таблицы аудиторий
create_classrooms_table = """
CREATE TABLE classrooms (
    classroom_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    capacity INTEGER NOT NULL
);
"""

# Создание связи между студентами и аудиториями
create_student_classroom_table = """
CREATE TABLE student_classroom (
    student_id INTEGER,
    classroom_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (classroom_id) REFERENCES classrooms (classroom_id)
);
"""
# Создание курсора
with conn.cursor() as cursor:
    # Создание таблицы студентов
    cursor.execute(create_students_table)

    # Создание таблицы аудиторий
    cursor.execute(create_classrooms_table)

    # Создание таблицы для связи студентов и аудиторий
    cursor.execute(create_student_classroom_table)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Таблицы успешно созданы в базе данных.")