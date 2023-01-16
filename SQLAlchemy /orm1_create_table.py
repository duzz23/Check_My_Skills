#инпртируем различные поля из библиотеки
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    Text,
)
#'указатель какой движок мы используем sqlite и название'
DB_URL = 'sqlite:///db.example1'
# Никогра в приложение в продакщен не должно быть true только false иначи будут проблемы с безопастностью
DB_ECHO = False

#подключение к БД (create_engine()) echo=DB_ECHO(можно не указывать никогда, тогда она будет выключено)
engine = create_engine(url=DB_URL, echo=DB_ECHO)
# доступен обьккт для создания таблицы Table, в ковычках имя таблицы
# metadata особый обьект что бы следить за таблицами, добавляется в __init__()
#matadata.register(self)


metadata = MetaData()
authors_table = Table(
    "authors",
    metadata,
    # дальше передаем колонки, pip install sqlalchemy-stubs что     бы плдсказывал написание кода
    Column("id", Integer, primary_key=True),
    # String(16) ограницений на 16 символов unique=True, что бы     имя было уникальым nullable=False
    Column("username", String(16), unique=True, nullable=False),
    Column("email", String(200), unique=True),
    Column("bio", Text),
)


# Вызов метога который создает таблицу
def main():
    metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
