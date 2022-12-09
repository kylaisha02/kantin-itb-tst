from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
#from sqlalchemy.orm import relationship

from database import connection

class Menu_kantin(connection.Base):
    __tablename__ = "menu_kantin"

    id_kantin = Column(Integer, primary_key=True)
    id_menu = Column(Integer, primary_key=True)
    nama_menu = Column(String)
    harga_menu = Column(Integer)
    ketersediaan = Column(String)
    
    #owner = relationship("User", back_populates="items")