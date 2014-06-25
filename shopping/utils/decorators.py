'''
Created on 25 juin 2014

@author: epot
'''

from functools import wraps
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.decorators import available_attrs
from django.utils.encoding import force_str
from django.utils.six.moves.urllib.parse import urlparse
from django.shortcuts import resolve_url
from django.shortcuts import get_object_or_404

from shopping.models import Recipe, ShoppingList

def user_owns(klass, parameter_name, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user owns an instance of the given class,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    parameter_name matches the view_func parameter that should be an id of class 'klass'

    This is highly inspired from the user_passes_test of django.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            obj = get_object_or_404(klass, pk=kwargs[parameter_name])
            if request.user in obj.owners.all():
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            # urlparse chokes on lazy objects in Python 3, force to str
            resolved_login_url = force_str(
                resolve_url(login_url or settings.LOGIN_URL))
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator

def user_owns_recipe(login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    return user_owns(Recipe, 'recipe_id')

def user_owns_shopping_list(login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    return user_owns(ShoppingList, 'list_id')