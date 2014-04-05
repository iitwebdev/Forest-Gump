from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view2(request):
    return {'project': 'MyProject'}

@view_config(route_name='registration', renderer='templates/regist.jinja2')
def my_view(request):
    return {'project': 'MyProject'}


