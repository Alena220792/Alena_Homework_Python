from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = create_engine(db_connection_string)

# Пробные тесты
def test_db_connection():
# Используем инспектор для получения информации о таблицах
	inspector = inspect(db)
	names = inspector.get_table_names()
	assert 'student' in names, f"Таблица 'student' не найдена. Список таблиц: {names}"
	

def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM student"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['user_id'] == 42568
    assert row1['level'] == "Pre-Intermediate"

    connection.close()


def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM student WHERE user_id = :user_id")
    result = connection.execute(sql_statement, {"user_id": 44133})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0]["level"] == "Beginner "

    connection.close()

# Тест на добавление
def test_add_student():
    user_id = 12345
    level = "Beginner"
    connection = db.connect()

    connection.execute(text("INSERT INTO student (user_id, level) VALUES (:u, :l)"), {"u": user_id, "l": level})
    connection.commit() 

    result = connection.execute(text("SELECT level FROM student WHERE user_id = :u"), {"u": user_id})
    assert result.scalar().strip() == level
    connection.commit() 

    connection.execute(text("DELETE FROM student WHERE user_id = :u"), {"u": user_id})
    connection.commit() 
    
    connection.close()

# Тест на изменение
def test_update_student():
    user_id = 777888  
    old_level = "Beginner"
    new_level = "Advanced"
    
    connection = db.connect()

    connection.execute(text("INSERT INTO student (user_id, level) VALUES (:u, :l)"), 
                       {"u": user_id, "l": old_level})
    connection.commit()

    connection.execute(text("UPDATE student SET level = :new_l WHERE user_id = :u"), 
                       {"new_l": new_level, "u": user_id})
    connection.commit()

    result = connection.execute(text("SELECT level FROM student WHERE user_id = :u"), 
                                {"u": user_id})
    
    assert result.scalar().strip() == new_level
    connection.commit()

    connection.execute(text("DELETE FROM student WHERE user_id = :u"), 
                       {"u": user_id})
    connection.commit()
    connection.close()

# Тест на удаление
def test_delete_student():
    user_id = 999111  
    level = "Intermediate"
    connection = db.connect()

    connection.execute(text("INSERT INTO student (user_id, level) VALUES (:u, :l)"), 
                       {"u": user_id, "l": level})
    connection.commit()

    connection.execute(text("DELETE FROM student WHERE user_id = :u"), 
                       {"u": user_id})
    connection.commit()

    result = connection.execute(text("SELECT * FROM student WHERE user_id = :u"), 
                                {"u": user_id})
    
    rows = result.all()
    connection.commit()

    assert len(rows) == 0
    connection.close()