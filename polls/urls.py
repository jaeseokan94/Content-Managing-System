from django.conf.urls import patterns, url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.contrib import admin





from . import views


admin.autodiscover()

app_name='polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    # ex: /polls/5/
    url(r'^language/$', views.language_list, name='language_list'),
    url(r'^language/(?P<language_name>[a-zA-Z0-9]+)', views.language_detail, name='language_detail'),
    url(r'^topics/$', views.topic_list, name='topic_list'),
    #url(r'^list/$', 'list', name='list'),
    url(r'^situationalVideo/$', views.situational_video_list),
    url(r'^situationalVideo/(?P<pk>[0-9]+)/$', views.situational_video_detail),
]


if not settings.DEBUG:
    urlpatterns += patterns(
'',
    (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )  

