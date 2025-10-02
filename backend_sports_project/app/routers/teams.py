from fastapi import APIRouter, Query # type: ignore
from app.crud.team import get_teams_by_league, save_teams
from app.services.sportsdb import fetch_teams_from_api

router = APIRouter()

@router.get("/api/teams")
def get_teams(league: str = Query(...)):
    db_teams = get_teams_by_league(league)
    if db_teams:
        return db_teams
    api_teams = fetch_teams_from_api(league)
    save_teams(api_teams, league)
    return get_teams_by_league(league)
