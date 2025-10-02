from sqlmodel import create_engine, Session, SQLModel # type: ignore

engine = create_engine("sqlite:///./sports.db")

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
