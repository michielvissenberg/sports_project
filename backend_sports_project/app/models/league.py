from sqlmodel import SQLModel, Field # type: ignore

class League(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idLeague: str
    strLeague: str
