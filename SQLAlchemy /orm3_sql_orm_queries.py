"""Создание таблици в PostgreSQL и дабавление в нее данных"""
from sqlalchemy import JSON
from sqlalchemy.orm import (
    declarative_base,
    Session as SessionType,
    sessionmaker,
    scoped_session,
)
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
    func,
)
from sqlalchemy.dialects.postgresql import (
    JSONB,
)
"""Создаем фаил"""
#указатель какой движок мы используем postgresql и название'
DB_URl = "postgresql+psycopg2://demouser:demouser@localhost:5435/blog"
DB_ECHO = True

#подключение к БД (create_engine()) echo=DB_ECHO(можно не указывать никогда, тогда она будет выключено)
engine = create_engine(url=DB_URl, echo=DB_ECHO)

Base = declarative_base(bind=engine)

"""Создаем сессию"""

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

"""Создаем таблицу"""

class User(Base):
    # имя таблици
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    # nullable = False если поле обязательное
    username = Column(String(32), unique=True, nullable=False)
    # server_default указывает какое значение будет по умолчанию в ДБ
    archived = Column(Boolean, default=False, server_default=false())
    # время будет тогда когда создаем новую зпись
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())

    # Делаем строковое представоение обекта
    def __str__(self):
        return f'User(id={self.id}, usernamr={self.username!r}, archived={self.archived}, create_at={self.created_at!r})'
    def __repr__(self):
        return str(self)

"""Функция для создания юзера"""

def create_user(session: SessionType, username: str) -> User:
    user = User(username=username)
    #Добавляем узеза
    session.add(user)
    print("user (added)", user)
    #Сохраняем юзера
    session.commit()
    print("seved user", user)
    #Возврашаем результат
    return user

"""Функция для создания uheggs группы юзеров"""

def create_grupe_users(session: SessionType, *usernames: str) -> list[User]:
    users = []
    for username in usernames:
        user = User(username=username)
        session.add(user)
        users.append(user)
    session.commit()
    return users

"""Функция запроса всех юзеров"""
def get_all_user(session: SessionType) -> list[User]:
    users = session.query(User).order_by(User.id).all()
    return users
"""Функция запроса по имени"""
def get_all_user_name(session: SessionType, username: str) -> User | None:
    user = session.query(User).filter_by(username=username).one_or_none()
    print("user", user)
    return user
"""Функция запрос по id"""
def get_all_user_id(session: SessionType, user_id: int) -> User | None:
    user = session.get(User, user_id)
    print("user", user)
    return user

"""!! Функция поиска по совподению !!"""
def get_users_by_username_match(session: SessionType, username_part: str) -> list[User]:
    users = session.query(User).filter(User.username.ilike(f'%{username_part}%')).all()
    print('User', users)
    return users

def main():
    Base.metadata.create_all()

    session: SessionType = Session()
    # Создает вызлв юзера
    # create_user(session, "Andrey")
    # Создаем группы юзеров
    # create_grupe_users(session, "stats", "vadim", "volender", "rodot")
    #Запроса всех юзеров
    # get_all_user(session)
    # # Запроса одноно по имени
    # get_all_user_name(session, 'Oleg')
    # # Запроса одного по id
    # get_all_user_id(session, 1)
    # get_all_user_id(session, 100)
    # Запроса всех юзеров где есть  а
    get_users_by_username_match(session, "a")

    session.close()


if __name__ == "__main__":
    main()


