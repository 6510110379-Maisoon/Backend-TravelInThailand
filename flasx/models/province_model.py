from sqlalchemy import Column, Integer, String, Boolean
from flasx.database import Base

class Province(Base):
    __tablename__ = 'provinces'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_secondary = Column(Boolean, default=False)
    tax_reduction = Column(Integer, default=0, nullable=False)

