from sqlmodel import select # type: ignore
from app.models.team import Team
from app.database import get_session

def get_teams_by_league(league: str):
    with get_session() as session:
        statement = select(Team).where(Team.strLeague == league)
        return session.exec(statement).all()

def save_teams(teams_data: list, league: str):
    with get_session() as session:
        for item in teams_data:
            team = Team(
                idTeam=item["idTeam"],
                strTeam=item["strTeam"],
                strLeague=league,
                strStadium=item.get("strStadium")
            )
            session.add(team)
        session.commit()
