from DataBase import engine

try:
    with engine.connect() as conn:
        print("База данных подключена")
except Exception as e:
    print(f"Ошибка: {e}")