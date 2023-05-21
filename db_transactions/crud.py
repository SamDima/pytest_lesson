from db import get_session, User


def create_user(name, session=None):
    user = User(name=name)

    if session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user.id
    else:
        with get_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user.id


def db_update_user(id, name, session=None):
    if session:
        user = session.query(User).filter(User.id
                                          == id
                                          ).first()
        user.name=name
        session.commit()
        session.refresh(user)
        return user.name
    else:
        with get_session() as session:
            user = session.query(User).filter(User.id
                                              == id
                                              ).first()
            user.name = name
            session.commit()
            session.refresh(user)
            return user.name


