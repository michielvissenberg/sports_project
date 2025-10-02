from fastapi import APIRouter, Query # type: ignore
from app.crud.teamPlayers import get_team_players_by_id, save_team_players
from app.services.sportsdb import fetch_team_players_from_api

router = APIRouter()

@router.get("/api/players")
def get_team_info(team: str = Query(...)):
    db_team_info = get_team_players_by_id(team)
    if db_team_info:
        return db_team_info
    api_team_info = fetch_team_players_from_api(team)
    save_team_players(api_team_info, team)
    return get_team_players_by_id(team)