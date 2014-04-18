from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view_home(request):
    return {'project': 'MyProject'}

@view_config(route_name='registration', renderer='templates/regist.jinja2')
def my_view(request):
    return {'project': 'MyProject'}

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