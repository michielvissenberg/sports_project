from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi import FastAPI # type: ignore
from app.routers import teams, leagues, teamInfo, teamPlayers, playerInfo, formerTeams, leagueTable, leagueInfo, venueInfo, teamSchedule
from app.database import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(teams.router)
app.include_router(leagues.router)
app.include_router(teamInfo.router)
app.include_router(teamPlayers.router)
app.include_router(playerInfo.router)
app.include_router(formerTeams.router)
app.include_router(leagueTable.router)
app.include_router(leagueInfo.router)
app.include_router(venueInfo.router)
app.include_router(teamSchedule.router)
init_db() 

