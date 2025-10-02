from sqlmodel import SQLModel, Field # type: ignore

class Player(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idPlayer: str = Field(index=True, unique=True)
    strPlayer: str
    idTeam: str
    strTeam: str
    strDescriptionEN: str | None = None
