import logging
import databases

import ormar
import sqlalchemy
from sqlalchemy.exc import OperationalError

from app.settings import settings

try:
    database = databases.Database(settings.db_url)
    engine = sqlalchemy.create_engine(settings.db_url)
    metadata = sqlalchemy.MetaData()
    metadata.create_all(engine)
except OperationalError:
    logging.warning("Database not found, falling back to sqlite3")
    fallback_db_url = "sqlite:///fallback_db.sqlite3"
    database = databases.Database(fallback_db_url)
    engine = sqlalchemy.create_engine(fallback_db_url)
    metadata = sqlalchemy.MetaData()
    metadata.create_all(engine)


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
