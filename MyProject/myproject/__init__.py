#-*- coding: utf-8 -*-
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.config import Configurator
from sqlalchemy import create_engine
from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.pool import NullPool
from .models import (
    DBSession,
    Base,
    )
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from myproject.models import get_user
#from .security import groupfinder

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    #config = Configurator(
        #settings=settings,
       # authentication_policy=SessionAuthenticationPolicy())
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=get_user, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('registration', '/registration')
    config.add_route('search', '/search')
    config.add_route('profile', '/profile')
    config.add_route('trees', '/trees')
    config.add_route('about', '/about')
    config.add_route('add', '/add')
    config.scan()
    return config.make_wsgi_app()
