from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
#from sqlalchemy.orm import relationship

from database import connection


class List_kantin(connection.Base):
    __tablename__ = "list_kantin"

    id = Column(Integer, primary_key=True)
    nama = Column(String)
    lokasi = Column(String)

    #items = relationship("Item", back_populates="owner")