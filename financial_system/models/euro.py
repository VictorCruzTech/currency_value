from sqlalchemy import Column, Integer, Float

from financial_system.models.mixins import CreatedUpdatedMixin

from .meta import Base


class EuroPrice(Base, CreatedUpdatedMixin):
    __tablename__ = "euro_price"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
