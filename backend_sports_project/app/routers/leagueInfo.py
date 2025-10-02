from fastapi import APIRouter, Query # type: ignore
from app.crud.leagueInfo import get_league_info_by_id, save_league_info
from app.services.sportsdb import fetch_league_info_from_api

router = APIRouter()

@router.get("/api/leagueinfo")
def get_player_info(league: str = Query(...)):
    if not league:
        return None
    db_league_info = get_league_info_by_id(league)
    if db_league_info:
        return db_league_info
    api_league_info = fetch_league_info_from_api(league)
    save_league_info(api_league_info, league)
    return get_league_info_by_id(league)