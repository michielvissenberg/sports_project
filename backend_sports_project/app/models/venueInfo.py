from sqlmodel import SQLModel, Field # type: ignore

class venueInfo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    strVenue: str = Field(index=True, unique=True)
    strVenueAlternate: str | None = None
    strDescriptionEN: str | None = None
    intCapacity: int | None = None
    intFormedYear: int | None = None
    strThumb: str = ""
    strLocation: str | None = None