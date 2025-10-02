from fastapi import APIRouter, Query # type: ignore
from app.crud.venueInfo import get_venue_info_by_name, save_venue_info
from app.services.sportsdb import fetch_venue_info_from_api

router = APIRouter()

@router.get("/api/venueinfo")
def get_team_info(venue: str = Query(...)):
    db_venue_info = get_venue_info_by_name(venue)
    if db_venue_info:
        return db_venue_info
    api_venue_info = fetch_venue_info_from_api(venue)
    save_venue_info(api_venue_info, venue)
    return get_venue_info_by_name(venue)