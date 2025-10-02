from fastapi import APIRouter, Query # type: ignore
from app.crud.teamSchedule import get_team_schedule_by_id, save_team_schedule
from app.services.sportsdb import fetch_team_schedule_from_api

router = APIRouter()

@router.get("/api/teamschedule")
def get_team_schedule(team: str = Query(...)):
    db_team_schedule = get_team_schedule_by_id(team)
    if db_team_schedule:
        return db_team_schedule
    api_team_schedule = fetch_team_schedule_from_api(team)
    save_team_schedule(api_team_schedule)
    return get_team_schedule_by_id(team)
