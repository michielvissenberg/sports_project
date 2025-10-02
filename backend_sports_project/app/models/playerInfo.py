from sqlmodel import SQLModel, Field # type: ignore

class PlayerInfo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idPlayer: str
    strName: str
    strTeam: str | None = None
    strSport: str | None = None
    strPosition: str | None = None
    dateBorn: str | None = None
    strNationality: str | None = None
    strThumb: str = ""
    strCutout: str = ""