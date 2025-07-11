from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flasx.database import Base

class TargetProvince(Base):
    __tablename__ = 'target_provinces'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    province_id = Column(Integer, ForeignKey('provinces.id'))

    province = relationship("Province")  
