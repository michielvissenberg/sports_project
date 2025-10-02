from sqlmodel import select # type: ignore
from app.models.teamSchedule import TeamSchedule
from app.database import get_session
from sqlalchemy import or_ # type: ignore

def get_team_schedule_by_id(team_id: str):
    with get_session() as session: 
        statement = select(TeamSchedule).where(
            or_(
                TeamSchedule.idHomeTeam == team_id,
                TeamSchedule.idAwayTeam == team_id
            )
        )
        return session.exec(statement).first()
    
def save_team_schedule(schedule_data: dict):
    with get_session() as session:
        existing = session.exec(
            select(TeamSchedule).where(TeamSchedule.idEvent == schedule_data["idEvent"])
        ).first()
        if existing:
            return existing 
        
        team_schedule = TeamSchedule(
            idEvent=schedule_data["idEvent"],
            strEvent=schedule_data["strEvent"],
            strFilename=schedule_data["strFilename"],
            strHomeTeam=schedule_data["strHomeTeam"],
            idHomeTeam=schedule_data["idHomeTeam"],
            strAwayTeam=schedule_data["strAwayTeam"],
            idAwayTeam=schedule_data["idAwayTeam"],
            dateEvent=schedule_data["dateEvent"],
            strTime=schedule_data["strTime"],
            strHomeTeamBadge=schedule_data.get("strHomeTeamBadge"),
            strAwayTeamBadge=schedule_data.get("strAwayTeamBadge"),
            strThumb=schedule_data.get("strThumb"),
        )
        session.add(team_schedule)
        session.commit()
