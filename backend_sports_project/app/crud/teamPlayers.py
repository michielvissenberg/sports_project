from sqlmodel import select # type: ignore
from app.models.player import Player
from app.database import get_session

def get_team_players_by_id(team: str):
    with get_session() as session:
        statement = select(Player).where(Player.idTeam == team)
        return session.exec(statement).all()

def save_team_players(players_data: list, league: str):
    with get_session() as session:
        for item in players_data:
            existing = session.exec(
                select(Player).where(Player.idPlayer == item.get("idPlayer"))
            ).first()
            if existing:
                existing.strPlayer = item.get("strPlayer")
                existing.idTeam = item.get("idTeam")
                existing.strTeam = item.get("strTeam")
                existing.strDescriptionEN = item.get("strDescriptionEN")
            else: 
                player = Player(
                    idPlayer=item.get("idPlayer"),
                    strPlayer=item.get("strPlayer"),
                    idTeam=item.get("idTeam"),
                    strTeam=item.get("strTeam"),
                    strDescriptionEN=item.get("strDescriptionEN")
                )
                session.add(player)
        session.commit()
