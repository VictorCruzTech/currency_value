import logging
import transaction

from os import name
from cornice import Service
from financial_system.api import API_V1_PATH
from financial_system.models import DBSession
from financial_system.models.euro import EuroPrice
from financial_system.api.schemas import EuroSchema

from pyramid.httpexceptions import HTTPOk, HTTPBadRequest, HTTPCreated
from cornice.validators import marshmallow_body_validator

logger = logging.getLogger()


euro_resource = Service(name='euro View', path=API_V1_PATH + '/euro/{id}', description='Get an especific euro price')
euro_collection = Service(name='euros View', path=API_V1_PATH + '/euros', description='List all euros price')


@euro_resource.get()
def get_euro(request):
    euro = DBSession.query(EuroPrice).filter_by(id=request.matchdict["id"]).first()
    
    if euro:
        return HTTPOk(json=EuroSchema().dump(euro))

    return HTTPBadRequest()

@euro_collection.get()
def get_euros(request):
    euros = DBSession.query(EuroPrice).all()
    
    if euros:
        return HTTPOk(json=EuroSchema(many=True).dump(euros))

    return []


@euro_collection.post(schema=EuroSchema, validators=(marshmallow_body_validator,))
def post_euro_price(request):
    euro_value = request.validated["price"]
    
    euro_price = EuroPrice(price=euro_value)
    
    try:    
        DBSession.add(euro_price)
        DBSession.flush()
        transaction.commit()
        
        logger.info("Success to create a Euro Price register")
        return HTTPCreated()
    except:
        logger.error("Error to create a new Euro Price.")
        return HTTPBadRequest()
