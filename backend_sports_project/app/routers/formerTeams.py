from fastapi import APIRouter, Query # type: ignore
from app.crud.formerTeams import get_former_teams, save_former_teams
from app.services.sportsdb import fetch_former_teams_from_api

router = APIRouter()

@router.get("/api/formerteams")
def get_player_info(player: str = Query(...)):
    if not player:
        return None
    db_player_info = get_former_teams(player)
    if db_player_info:
        return db_player_info
    api_player_info = fetch_former_teams_from_api(player)
    save_former_teams(api_player_info, player)
    return get_former_teams(player)