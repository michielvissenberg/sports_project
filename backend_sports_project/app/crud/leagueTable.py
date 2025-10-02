from sqlmodel import select # type: ignore
from app.models.leagueTable import LeagueTable
from app.database import get_session

def get_league_table_by_id(league_id: str):
    with get_session() as session: 
        statement = select(LeagueTable).where(LeagueTable.idLeague == league_id)
        return session.exec(statement).all()
    
def save_league_table(league_table_data: list, league: str):
    with get_session() as session:
        for entry in league_table_data:
            statement = select(LeagueTable).where(LeagueTable.idTeam == entry["idTeam"])
            existing = session.exec(statement).first()
            if existing:
                continue 
            
            league_table_entry = LeagueTable(
                idTeam=entry["idTeam"],
                strTeam=entry["strTeam"],
                intRank=entry["intRank"],
                intPoints=entry["intPoints"],
                intPlayed=entry["intPlayed"],
                intWin=entry["intWin"],
                intDraw=entry["intDraw"],
                intLoss=entry["intLoss"],
                intGoalsFor=entry["intGoalsFor"],
                intGoalsAgainst=entry["intGoalsAgainst"],
                intGoalDifference=entry["intGoalDifference"],
                strForm=entry["strForm"],
                idLeague=league,
                strLeague=entry["strLeague"]
            )
            session.add(league_table_entry)
        session.commit()