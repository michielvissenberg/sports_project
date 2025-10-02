from fastapi import APIRouter, Query # type: ignore
from app.crud.playerInfo import get_player_info_by_name, save_player_info
from app.services.sportsdb import fetch_player_info_from_api

router = APIRouter()

@router.get("/api/playerinfo")
def get_player_info(player: str = Query(...)):
    if not player:
        return None
    db_player_info = get_player_info_by_name(player)
    if db_player_info:
        return db_player_info
    api_player_info = fetch_player_info_from_api(player)
    save_player_info(api_player_info, player)
    return get_player_info_by_name(player)