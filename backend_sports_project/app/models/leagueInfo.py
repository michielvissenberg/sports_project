from sqlmodel import SQLModel, Field # type: ignore

class LeagueInfo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idLeague: str
    strLeague: str | None = None
    strCountry: str | None = None
    intFormedYear: str | None = None
    strWebsite: str = ""
    strDescriptionEN: str = ""
    strBanner: str = ""
    strBadge: str = ""
    strLogo: str = ""
    strTrophy: str = ""
