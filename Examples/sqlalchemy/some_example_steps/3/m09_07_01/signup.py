from sqlalchemy.exc import SQLAlchemyError
from database.db import session
from database.models import User

if __name__ == '__main__':
    login = input('Login: ')
    password = input('Password: ')
    try:
        user = User(login=login, password=password)  # створюємо користувача
        session.add(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()  # відкат якщо помилка
        print(e)
    finally:
        session.close()
