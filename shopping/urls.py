from django.conf.urls import patterns, url

from shopping import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /recipe/5/
    url(r'^(?P<recipe_id>\d+)/$', views.recipe_detail, name='recipe_detail'),
    # ex: /recipe/5/addelement/
    url(r'^(?P<recipe_id>\d+)/addelement/$', views.addelement, name='addelement'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'shopping/login.html'
    }),
)