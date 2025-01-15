from sqlalchemy import Column, Integer, String, Text

from database_config.Config import Model1Base


class Course(Model1Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    level = Column(String(50))
    goals = Column(Text)
    duration = Column(String(50))
    hours = Column(String(50))
    summary = Column(Text)
    teacher = Column(String(255))


