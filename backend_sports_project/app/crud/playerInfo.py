from sqlmodel import select # type: ignore
from app.models.playerInfo import PlayerInfo
from app.database import get_session

def get_player_info_by_name(player_name: str):
    with get_session() as session: 
        statement = select(PlayerInfo).where(PlayerInfo.strName == player_name)
        return session.exec(statement).first()

def save_player_info(player_info_data: dict, player: str):
    with get_session() as session:
        existing = session.get(PlayerInfo, player_info_data["idPlayer"])
        if existing:
            return existing 
        
        player_info = PlayerInfo(
            idPlayer=player_info_data["idPlayer"],
            strName=player,
            strTeam=player_info_data.get("strTeam"),
            strSport=player_info_data.get("strSport"),
            strPosition=player_info_data.get("strPosition"),
            dateBorn=player_info_data.get("dateBorn"),
            strNationality=player_info_data.get("strNationality"),
            strThumb=player_info_data.get("strThumb") or "",
            strCutout=player_info_data.get("strCutout") or "",
        )
        session.add(player_info)
        session.commit()