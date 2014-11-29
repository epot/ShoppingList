from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings

from social.backends.utils import load_backends

from shopping import views

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'shopping/login.html',
        'extra_context':{'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)}
    }),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/shopping/accounts/login'}),
    
    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^$', views.home, name='home'),
    url(r'^recipe/$', views.recipe_list, name='recipe_list'),
    # ex: /recipe/5/
    url(r'^recipe/(?P<recipe_id>\d+)/$', views.recipe_detail, name='recipe_detail'),
    
    url(r'^recipe/new$', login_required(views.RecipeCreate.as_view()), name='recipe_new'),
    url(r'^recipe/edit/(?P<pk>\d+)$', login_required(views.RecipeUpdate.as_view()), name='recipe_edit'),
    url(r'^recipe/details/(?P<recipe_id>\d+)$', views.recipe_details, name='recipe_details'),
    url(r'^recipe/delete/(?P<pk>\d+)$', login_required(views.RecipeDelete.as_view()), name='recipe_delete'),
    
    # ex: /recipe/5/addelement/
    url(r'^recipe/(?P<recipe_id>\d+)/element/edit/(?P<recipeelement_id>\d+)/$', views.element_edit, name='element_edit'),
    url(r'^recipe/(?P<recipe_id>\d+)/element/remove/(?P<recipeelement_id>\d+)/$', views.element_remove, name='element_remove'),
    
    
    url(r'^meal/$', views.meal_list, name='meal_list'),
    url(r'^meal/edit/(?P<meal_id>\d+)$', views.meal_list, name='meal_list'),
    url(r'^meal/form/(?P<meal_id>\d+)$', views.meal_form, name='meal_form'),
    #url(r'^meal/edit/(?P<pk>\d+)$', views.meal_edit, name='meal_edit'),
    url(r'^meal/delete/(?P<meal_id>\d+)$', views.meal_delete, name='meal_delete'),

    url(r'^list/$', views.shopping_list, name='list_list'),
    url(r'^list/(?P<list_id>\d+)/$', views.shoppinglist_detail, name='shoppinglist_detail'),
    url(r'^list/new$', login_required(views.ShoppingListCreate.as_view()), name='list_new'),
    url(r'^list/edit/(?P<pk>\d+)$', login_required(views.ShoppingListUpdate.as_view()), name='list_edit'),
    url(r'^list/delete/(?P<pk>\d+)$', login_required(views.ShoppingListDelete.as_view()), name='list_delete'),
    
    url(r'^ingredient/$', views.ingredient_list, name='ingredient_list'),
    url(r'^ingredient/new$', login_required(views.IngredientCreate.as_view()), name='ingredient_new'),
    url(r'^ingredient/edit/(?P<pk>\d+)$', login_required(views.IngredientUpdate.as_view()), name='ingredient_edit'),
    url(r'^ingredient/delete/(?P<pk>\d+)$', login_required(views.IngredientDelete.as_view()), name='ingredient_delete'),
)