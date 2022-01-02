import string
from _decimal import Decimal

import sqlalchemy

import factory
import transaction

from financial_system.models import DBSession
from financial_system.models.dolar import DolarPrice
from financial_system.models.euro import EuroPrice



class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    
    @classmethod
    def generate(cls, total, commit=False, **kwargs):
        """Generate x number of register.
        :param int total: total of register to generate.
        :param bool commit: if True, objects will be committed to the database.
        """

        objs = []
        for x in range(total):
            objs.append(cls(**kwargs))

        DBSession.add_all(objs)
        DBSession.flush()

        if commit:
            transaction.commit()
            DBSession.add_all(objs)

        return objs if total > 1 else objs[0]


class DolarPriceFactory(BaseFactory):
    
    class Meta:
        model = DolarPrice
        sqlalchemy_session = DBSession
    
    price = 21.08


class EuroPriceFactory(BaseFactory):
    
    class Meta:
        model = EuroPrice
        sqlalchemy_session = DBSession
    
    price = 24.08
