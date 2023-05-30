from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from db import User
from db_transactions.crud import create_user

SQLALCHEMY_DATABASE_URL_TEST = "postgresql+psycopg2://postgres:pass@localhost:5432/starwars_test"

Base_test = declarative_base()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL_TEST,
)

Session = sessionmaker(bind=engine)


@contextmanager
def get_session_test():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def test_create_user_db(session):
    user_name = "test_user_00723"
    user = User(name=user_name)
    session.add(user)
    session.commit()
    assert user.id is not None


def test_create_user_db_2(session):
    id  = create_user(name='New Name', session=session)
    assert id is not None





