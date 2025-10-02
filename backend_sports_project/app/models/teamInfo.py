from sqlmodel import SQLModel, Field # type: ignore

class TeamInfo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idTeam: str
    strTeam: str
    strLeague: str
    strStadium: str 
    intFormedYear: str 
    strKeywords: str 
    strLocation: str
    intStadiumCapacity: str
    strWebsite: str
    strDescriptionEN: str 
    strBadge: str | None = None
    strLogo: str | None = None
    
