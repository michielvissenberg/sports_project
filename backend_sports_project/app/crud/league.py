from sqlmodel import select # type: ignore
from app.models.league import League
from app.database import get_session

def get_leagues_from_db():
    with get_session() as session:
        statement = select(League)
        return session.exec(statement).all()

def save_leagues(leagues_data: list):
    with get_session() as session:
        for item in leagues_data:
            league = League(
                idLeague=item["idLeague"],
                strLeague=item["strLeague"],
            )
            session.add(league)
        session.commit()
