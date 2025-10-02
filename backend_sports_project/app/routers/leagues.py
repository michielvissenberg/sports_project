from fastapi import APIRouter, Query # type: ignore
from app.crud.league import get_leagues_from_db, save_leagues
from app.services.sportsdb import fetch_leagues_from_api

router = APIRouter()

@router.get("/api/leagues")
def get_leagues():
    db_leagues = get_leagues_from_db()
    if db_leagues:
        return db_leagues
    api_leagues = fetch_leagues_from_api()
    save_leagues(api_leagues)
    return get_leagues()

