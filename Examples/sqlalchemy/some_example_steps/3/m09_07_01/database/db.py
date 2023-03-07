#  під'єднуємося до БД
import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# postgresql://username:password@domain_name:port/database_name
file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()  # для читання та розпарсювання конфіг-файлу
config.read(file_config)  # читаємо

username = config.get('DB', 'USER')  # секція, параметр - беремо з прочитаного
password = config.get('DB', 'PASSWORD')
database_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')
port = config.get('DB', 'PORT')
# sqlalchemy розумний сам драйвер доставить під певну БД, але при використанні асинхронного - треба прописувати
url = f'postgresql://{username}:{password}@{domain}:{port}/{database_name}' # окрему змінну, бо для alembic треба використовувати 

engine = create_engine(url, echo=True)

DBSession = sessionmaker(bind=engine)
session = DBSession()
