from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('registration', '/registration')
    config.add_route('search', '/search')
    config.add_route('profile', '/profile')
    config.add_route('trees', '/profile/trees')
    config.add_route('about', '/about')
    config.scan()
    return config.make_wsgi_app()
