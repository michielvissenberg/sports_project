from sqlmodel import select # type: ignore
from app.models.teamInfo import TeamInfo
from app.database import get_session

def get_team_info_by_name(team_name: str):
    with get_session() as session: 
        statement = select(TeamInfo).where(TeamInfo.strTeam == team_name)
        return session.exec(statement).first()

def save_team_info(team_info_data: dict, team: str):
    with get_session() as session:
        statement = select(TeamInfo).where(TeamInfo.idTeam == team_info_data["idTeam"])
        existing = session.exec(statement).first()

        if existing:
            return existing 
        
        team_info = TeamInfo(
            idTeam=team_info_data["idTeam"],
            strTeam=team,
            strLeague=team_info_data["strLeague"],
            strStadium=team_info_data.get("strStadium"),
            intFormedYear=team_info_data.get("intFormedYear"),
            strKeywords=team_info_data.get("strKeywords"),
            strLocation=team_info_data.get("strLocation"),
            intStadiumCapacity=team_info_data.get("intStadiumCapacity"),
            strWebsite=team_info_data.get("strWebsite"),
            strDescriptionEN=team_info_data.get("strDescriptionEN"),
            strBadge=team_info_data.get("strBadge") or "",
            strLogo=team_info_data.get("strLogo") or "",

        )
        session.add(team_info)
        session.commit()
