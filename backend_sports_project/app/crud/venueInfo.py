from sqlmodel import select # type: ignore
from app.models.venueInfo import venueInfo
from app.database import get_session

def get_venue_info_by_name(venue: str):
    with get_session() as session: 
        statement = select(venueInfo).where(venueInfo.strVenue == venue)
        return session.exec(statement).first()

def save_venue_info(venueInfoData: dict, venue: str):
    with get_session() as session:
        statement = select(venueInfo).where(venueInfo.strVenue == venueInfoData["strVenue"])
        existing = session.exec(statement).first()

        if existing:
            return existing 
        
        venueStats = venueInfo(
            strVenue=venue,
            strVenueAlternate=venueInfoData.get("strVenueAlternate"),
            strDescriptionEN=venueInfoData.get("strDescriptionEN"),
            intCapacity=venueInfoData.get("intCapacity"),
            intFormedYear=venueInfoData.get("intFormedYear"),
            strThumb=venueInfoData.get("strThumb") or "",
            strLocation=venueInfoData.get("strLocation"),
        )
        
        session.add(venueStats)
        session.commit()