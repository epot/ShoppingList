from django.conf.urls import patterns, url

from shopping import views

urlpatterns = patterns('',
    url(r'^$', views.recipe_list, name='recipe_list'),
    # ex: /recipe/5/
    url(r'^(?P<recipe_id>\d+)/$', views.recipe_detail, name='recipe_detail'),
    
    url(r'^recipe/new$', views.RecipeCreate.as_view(), name='recipe_new'),
    url(r'^recipe/edit/(?P<pk>\d+)$', views.RecipeUpdate.as_view(), name='recipe_edit'),
    url(r'^recipe/delete/(?P<pk>\d+)$', views.RecipeDelete.as_view(), name='recipe_delete'),
    
    # ex: /recipe/5/addelement/
    url(r'^recipe/(?P<recipe_id>\d+)/remove_element/(?P<element_id>\d+)/$', views.remove_element, name='remove_element'),
    url(r'^recipe/(?P<recipe_id>\d+)/add_element/$', views.add_element, name='add_element'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'shopping/login.html'
    }),
                       
    url(r'^list/$', views.shopping_list, name='list_list'),
    url(r'^list/(?P<list_id>\d+)/$', views.shoppinglist_detail, name='shoppinglist_detail'),
    url(r'^list/new$', views.ShoppingListCreate.as_view(), name='list_new'),
    url(r'^list/edit/(?P<pk>\d+)$', views.ShoppingListUpdate.as_view(), name='list_edit'),
    url(r'^list/delete/(?P<pk>\d+)$', views.ShoppingListDelete.as_view(), name='list_delete'),
    
    url(r'^ingredient/$', views.ingredient_list, name='ingredient_list'),
    url(r'^ingredient/new$', views.IngredientCreate.as_view(), name='ingredient_new'),
    url(r'^ingredient/edit/(?P<pk>\d+)$', views.IngredientUpdate.as_view(), name='ingredient_edit'),
    url(r'^ingredient/delete/(?P<pk>\d+)$', views.IngredientDelete.as_view(), name='ingredient_delete'),
)