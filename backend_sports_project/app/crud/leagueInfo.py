from sqlmodel import select # type: ignore
from app.models.leagueInfo import LeagueInfo
from app.database import get_session

def get_league_info_by_id(league_id: str):
    with get_session() as session: 
        statement = select(LeagueInfo).where(LeagueInfo.idLeague == league_id)
        return session.exec(statement).first()

def save_league_info(league_info_data: dict, league_id: str):
    with get_session() as session:
        existing = session.get(LeagueInfo, league_info_data["idLeague"])
        if existing:
            return existing 
    
        league_info = LeagueInfo(
            idLeague=league_id,
            strLeague=league_info_data.get("strLeague"),
            strCountry=league_info_data.get("strCountry"),
            intFormedYear=league_info_data.get("intFormedYear"),
            strWebsite=league_info_data.get("strWebsite") or "",
            strDescriptionEN=league_info_data.get("strDescriptionEN") or "",
            strBanner=league_info_data.get("strBanner") or "",
            strBadge=league_info_data.get("strBadge") or "",
            strLogo=league_info_data.get("strLogo") or "",
            strTrophy=league_info_data.get("strTrophy") or "",
        )

        session.add(league_info)
        session.commit()
        