from sqlmodel import select # type: ignore
from app.models.formerTeams import formerteams, teamitem
from app.database import get_session

def get_former_teams(player_id: str):
    with get_session() as session: 
        statement = select(formerteams).where(formerteams.idPlayer == player_id)
        former_team = session.exec(statement).first()  
        if not former_team:
            return None      
        return {
            "id": former_team.id,
            "idPlayer": former_team.idPlayer,
            "strName": former_team.strName,
            "teams": [
                {
                    "strFormerTeam": t.strFormerTeam,
                    "strPlayer": t.strPlayer,
                    "strJoined": t.strJoined,
                    "strDeparted": t.strDeparted,
                    "strMoveType": t.strMoveType,
                    "strBadge": t.strBadge,
                }
                for t in former_team.teams
            ]
        }

def save_former_teams(formerTeamsData: list, player_id: str):
    with get_session() as session:
        if not formerTeamsData:
            return
        teams = []
        for teamData in formerTeamsData:
            existing = session.get(formerteams, teamData["idPlayer"])
            if existing:
                teams.append(existing)
        if len(teams) > 0:
            return teams
        
        former_teams = formerteams(
            idPlayer=player_id,
            strName=formerTeamsData[0].get("strPlayer"),
        )

        session.add(former_teams)
        session.flush()

        for teamData in formerTeamsData:
            team_item = teamitem(
                idFormerTeams=former_teams.id,
                strFormerTeam=teamData.get("strFormerTeam"),
                strPlayer=teamData.get("strPlayer"),
                strJoined=teamData.get("strJoined"),
                strDeparted=teamData.get("strDeparted"),
                strMoveType=teamData.get("strMoveType"),
                strBadge=teamData.get("strBadge", "")
            )
            session.add(team_item)

        session.commit()
