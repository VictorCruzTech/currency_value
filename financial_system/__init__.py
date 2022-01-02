from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        # config.include('pyramid_jinja2')
        
        config.include("pyramid_celery")
        config.configure_celery("development.ini")
        
        # config.include('.routes')
        config.include('.models')
        
        config.add_route('health', '/health')
        
        config.include("cornice")
        config.include(".api")
        config.scan()
    return config.make_wsgi_app()
