from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from .db import Base

class Category(Base):
    __tablename__ = "issues_issuecategory"  # Django table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

class Issue(Base):
    __tablename__ = "issues_issue"  # Django table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey("issues_issuecategory.id"))
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    photo = Column(String, nullable=True)
    status = Column(String, default="new")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
