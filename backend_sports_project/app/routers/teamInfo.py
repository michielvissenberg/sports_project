from fastapi import APIRouter, Query # type: ignore
from app.crud.teamInfo import get_team_info_by_name, save_team_info
from app.services.sportsdb import fetch_team_info_from_api

router = APIRouter()

@router.get("/api/teaminfo")
def get_team_info(team: str = Query(...)):
    db_team_info = get_team_info_by_name(team)
    if db_team_info:
        return db_team_info
    api_team_info = fetch_team_info_from_api(team)
    save_team_info(api_team_info, team)
    return get_team_info_by_name(team)