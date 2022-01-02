from cornice import Service
from financial_system.api import API_V1_PATH
from financial_system.models import DBSession
from financial_system.models.dolar import DolarPrice
from financial_system.api.schemas import DolarSchema

from pyramid.httpexceptions import HTTPOk, HTTPBadRequest



dolar = Service(name='Dolar View', path=API_V1_PATH + '/dolar/{id}', description='Get Test Name')

dolar_collection = Service(name='Dolars View', path=API_V1_PATH + '/dolars', description='Get Test Name')


@dolar.get()
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

    return [{}]
