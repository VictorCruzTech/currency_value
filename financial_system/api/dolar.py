import logging
import transaction

from os import name
from cornice import Service
from financial_system.api import API_V1_PATH
from financial_system.models import DBSession
from financial_system.models.dolar import DolarPrice
from financial_system.api.schemas import DolarSchema

from pyramid.httpexceptions import HTTPOk, HTTPBadRequest, HTTPCreated
from cornice.validators import marshmallow_body_validator


logger = logging.getLogger()


dolar_resource = Service(name='Dolar View', path=API_V1_PATH + '/dolar/{id}', description='Get an especific dolar price')
dolar_collection = Service(name='Dolars View', path=API_V1_PATH + '/dolars', description='List all dolars price')


@dolar_resource.get()
def get_dolar(request):
    dolar = DBSession.query(DolarPrice).filter_by(id=request.matchdict["id"]).first()
    
    if dolar:
        return HTTPOk(json=DolarSchema().dump(dolar))

    return HTTPBadRequest()

@dolar_collection.get()
def get_dolars(request):
    dolars = DBSession.query(DolarPrice).all()
    
    if dolars:
        return HTTPOk(json=DolarSchema(many=True).dump(dolars))

    return []


@dolar_collection.post(schema=DolarSchema, validators=(marshmallow_body_validator,))
def post_dolar_price(request):
    dolar_value = request.validated["price"]
    
    dolar_price = DolarPrice(price=dolar_value)
    
    try:    
        DBSession.add(dolar_price)
        DBSession.flush()
        transaction.commit()
        
        logger.info("Success to create a Dolar Price register.")
        return HTTPCreated()
    except:
        logger.error("Error to create a new Dolar Price.")
        return HTTPBadRequest()
