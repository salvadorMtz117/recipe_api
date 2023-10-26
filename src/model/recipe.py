import db
from sqlalchemy import Column, Integer, String

class Recipe(db.Base):
    """Modelo de receta"""
    __tablename__ = "tc_recipe"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(Integer, nullable=False)

    def __init__(self,name,type):
        self.name = name
        self.type = type
    
    def __repr__(self):
        return f'Recipe({self.name},{self.type})'
    
    def __str__(self):
        return self.name