#-*- coding: utf-8 -*-
from pyramid.view import view_config, forbidden_view_config
from pyramid.response import FileResponse
from pyramid.security import remember, authenticated_userid, forget
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from myproject.models import add_guy, add_guys_relation, \
    del_all_tables, login, register, get_user, all_guys, all_users, all_rels

@forbidden_view_config()
def forbidden_view(request):
    # do not allow a user to login if they are already logged in
    if authenticated_userid(request):
        return HTTPForbidden()
    loc = request.route_url('login', _query=(('next', request.path),))
    return HTTPFound(location=loc)


def get_current_user(request):
    id_ = authenticated_userid(request)
    print("in views", id_)
    user = get_user(id_, request)
    return user

@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view_home(request):
    #del_all_tables()
    nxt = request.route_url('profile')
    did_fail = False
    if 'email' in request.POST:
        user = login(request.POST["email"], request.POST["password"])
        if user:
            print("in home: ", user.id)
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
            request.POST["password"], request.POST['sex']
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
    try:
        user = get_current_user(request)
    except:
        return {}
    return {'name': user.name,
            'email': user.email,
            'sex': user.sex
    }

@view_config(route_name='about', renderer='templates/about.jinja2')
def my_view_about(request):
    return {'project': 'MyProject'}

@view_config(route_name='trees', renderer='templates/my_trees.jinja2')
def my_view_trees(request):
    return {'project': 'MyProject'}

@view_config(route_name='add', renderer='templates/add_tree.jinja2')
def my_view_add_tree(request):
    did_fail = False
    persons = all_guys()
    if 'surname' in request.POST:
        guy = add_guy(
            request.POST["surname"], request.POST["name"],
            request.POST["middle_name"], request.POST["birth"], request.POST['end'], request.POST["birthplace"]
        )
        if guy:
            persons = all_guys()
            if 'person' in request.POST:
                add_guys_relation(request.POST["person"], guy, request.POST["relations"])
        else:
            did_fail = True
    relations = all_rels()
    return {
        'failed_attempt': did_fail,
        'relations': [u"Супруг", u"Родитель"],
        'guys': persons,
        'dict_relations': relations
    }