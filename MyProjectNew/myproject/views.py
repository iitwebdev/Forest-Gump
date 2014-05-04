#-*- coding: utf-8 -*-
from pyramid.view import view_config, forbidden_view_config
from pyramid.security import remember, authenticated_userid, forget
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from myproject.models import register, login, add_guy, all_guys, add_guys_relation


@forbidden_view_config()
def forbidden_view(request):
    # do not allow a user to login if they are already logged in
    if authenticated_userid(request):
        return HTTPForbidden()
    loc = request.route_url('login', _query=(('next', request.path),))
    return HTTPFound(location=loc)

@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view_home(request):
    nxt = request.params.get('next') or request.route_url('profile')
    did_fail = False
    if 'email' in request.POST:
        user = login(request.POST["email"], request.POST["password"])
        if user:
            headers = remember(request, user.id)
            return HTTPFound(location=nxt, headers=headers)
        else:
            did_fail = True
    return {
        'email': "",
        'next': nxt,
        'failed_attempt': did_fail,
    }

@view_config(route_name='registration', renderer='templates/regist.jinja2')
def my_view(request):
    nxt = request.params.get('next') or request.route_url('profile')
    did_fail = False

    if 'e-mail' in request.POST:
        user = register(
            request.POST["login"], request.POST["e-mail"],
            request.POST["password"]
        )
        if user:
            headers = remember(request, user.id)
            return HTTPFound(location=nxt, headers=headers)
        else:
            did_fail = True
    return {
        'login': "",
        'next': nxt,
        'failed_attempt': did_fail,
    }

@view_config(route_name='search', renderer='templates/search.jinja2')
def my_view_search(request):
    return {'project': 'MyProject'}

@view_config(route_name='profile', renderer='templates/profile.jinja2')
def my_view_profile(request):
    return {'project': 'MyProject'}

@view_config(route_name='about', renderer='templates/about.jinja2')
def my_view_about(request):
    return {'project': 'MyProject'}

@view_config(route_name='trees', renderer='templates/my_trees.jinja2')
def my_view_trees(request):
    return {'project': 'MyProject'}

@view_config(route_name='add', renderer='templates/add_tree.jinja2')
def my_view_add_tree(request):
    did_fail = False
    guys = all_guys()
    if 'surname' in request.POST:
        guy = add_guy(
            request.POST["surname"], request.POST["name"],
            request.POST["middle_name"]
        )
        if guy:
            guys = all_guys()
            headers = remember(request, guy.id)
            #return HTTPFound(headers=headers)
        else:
            did_fail = True
    if 'people1' in request.POST:
        rel = add_guys_relation(request.POST["people1"], request.POST["people2"], request.POST["relations"])
    return {
        'failed_attempt': did_fail,
        'relations': ["Mother", "Son", "Sister", "Uncle", "Grandmother"],
        'guys': guys
    }