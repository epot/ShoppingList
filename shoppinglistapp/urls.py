from django.conf.urls import patterns, url

from shoppinglistapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /recipe/5/
    url(r'^(?P<recipe_id>\d+)/$', views.recipe_detail, name='detail'),
)