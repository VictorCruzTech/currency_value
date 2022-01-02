from pyramid.response import Response
from pyramid.view import view_config


API_V1_PATH = "/api/v1"


@view_config(route_name="health")
def health(request):
    return Response("OK")


def includeme(config):
    settings = config.get_settings()