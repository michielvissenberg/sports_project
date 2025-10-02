from fastapi import APIRouter, Query # type: ignore
from app.crud.leagueTable import get_league_table_by_id, save_league_table
from app.services.sportsdb import fetch_league_table_from_api

router = APIRouter()

@router.get("/api/leagueTable")
def get_league_table(league: str = Query(...)):
    db_leagues = get_league_table_by_id(league)
    if db_leagues:
        return db_leagues
    api_leagues = fetch_league_table_from_api(league)
    save_league_table(api_leagues, league)
    return get_league_table_by_id(league)
