from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

from world.views import IndexView,MapaDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'world.views.index', name='index'),
    url(r'^$',IndexView.as_view()),
    url(r'^mapa/(?P<pk>[-\w]+)/$', MapaDetailView.as_view()),
)
