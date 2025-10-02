from sqlmodel import SQLModel, Field # type: ignore
from typing import List

class LeagueTable(SQLModel, table=True):
    idTeam: str = Field(primary_key=True)
    strTeam: str | None = None
    intRank: int | None = None
    intPoints: int | None = None
    intPlayed: int | None = None
    intWin: int | None = None
    intDraw: int | None = None
    intLoss: int | None = None
    intGoalsFor: int | None = None
    intGoalsAgainst: int | None = None
    intGoalDifference: int | None = None
    strForm: str | None = None
    idLeague: str 
    strLeague: str | None = None