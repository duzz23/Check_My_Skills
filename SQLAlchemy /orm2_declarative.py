# Дикларотивная база

# инпртируем различные поля из библиотеки
from datetime import datetime
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    Text,
    false,
    DateTime,
)
from sqlalchemy.orm import declarative_base

# 'указатель какой движок мы используем sqlite и название'
DB_URL = 'sqlite:///db.example2'
# Никогра в приложение в продакщен не должно быть true только false иначи будут проблемы с безопастностью
DB_ECHO = False

# подключение к БД (create_engine()) echo=DB_ECHO(можно не указывать никогда, тогда она будет выключено)
engine = create_engine(url=DB_URL, echo=DB_ECHO)
# доступен обьккт для создания таблицы Table, в ковычках имя таблицы
# metadata особый обьект что бы следить за таблицами, добавляется в __init__()
# matadata.register(self)

Base = declarative_base(bind=engine)


# заполнение таблици с данными юзеров
class User(Base):
    # имя таблици
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    # nullable = False если поле обязательное
    username = Column(String(32), unique=True, nullable=False)
    # server_default указывает какое значение будет по умолчанию в ДБ
    archived = Column(Boolean, default=False, server_default=false())
    # время будет тогда когда создаем новую зпись
    created_at = Column(DateTime, default=datetime.utcnow)

    # можно указать имя поля если это требует условия к примеру с паролеми
    # _password = Column('password', String)
    #
    # @property
    # def password(self) -> str:
    #     return self.password
    # # и сетор
    # @password.setter
    # def password(self, value):
    #     self.password = hash(value)

#Создание таблицы
def main():
    # .drop_all() если хотим добавить новые поля в таблицу с начало нужно удалить старую и наее место создать новую
    # Base.metadata.drop_all()
    Base.metadata.create_all()


if __name__ == "__main__":
    main()
