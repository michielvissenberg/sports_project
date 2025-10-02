from sqlmodel import SQLModel, Field # type: ignore

class Team(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idTeam: str
    strTeam: str
    strLeague: str
    strStadium: str | None = None
