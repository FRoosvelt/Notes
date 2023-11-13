from sqlalchemy import Column, Integer, Text, BigInteger

from db_api.database import Base


# Таблица заметок
class Notes_table(Base):
    __tablename__ = "Notes"
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    title = Column(Text)
    description = Column(Text)
