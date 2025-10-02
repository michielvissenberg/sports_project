from sqlmodel import SQLModel, Field, Relationship # type: ignore
from typing import List

class formerteams(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idPlayer: str
    strName: str
    teams: List["teamitem"] = Relationship(back_populates="former_team")

class teamitem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idFormerTeams: int = Field(foreign_key="formerteams.id")
    strFormerTeam: str | None = None
    strPlayer: str | None = None
    strJoined: str | None = None
    strDeparted: str | None = None
    strMoveType: str | None = None
    strBadge: str = ""
    former_team: formerteams = Relationship(back_populates="teams")