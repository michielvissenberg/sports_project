from sqlmodel import SQLModel, Field # type: ignore

class TeamSchedule(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idEvent: int
    strEvent: str
    strFilename: str
    strHomeTeam: str
    idHomeTeam: str
    strAwayTeam: str
    idAwayTeam: str
    dateEvent: str
    strTime: str
    strHomeTeamBadge: str | None = None
    strAwayTeamBadge: str | None = None
    strThumb: str | None = None