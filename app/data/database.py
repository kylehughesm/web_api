from sqlalchemy import create_engine
from config import Config


_engine = None

def init_engine():
    global _engine

    if _engine is None:
        _engine = create_engine(Config.DATABASE_URL)

    return _engine
