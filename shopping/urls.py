from django.conf.urls import patterns, url

from shopping import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /recipe/5/
    url(r'^(?P<recipe_id>\d+)/$', views.recipe_detail, name='recipe_detail'),
    
    url(r'^new$', views.RecipeCreate.as_view(), name='recipe_new'),
    url(r'^edit/(?P<pk>\d+)$', views.RecipeUpdate.as_view(), name='recipe_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.RecipeDelete.as_view(), name='recipe_delete'),
    
    # ex: /recipe/5/addelement/
    url(r'^(?P<recipe_id>\d+)/remove_element/(?P<element_id>\d+)/$', views.remove_element, name='remove_element'),
    url(r'^(?P<recipe_id>\d+)/add_element/$', views.add_element, name='add_element'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'shopping/login.html'
    }),
)