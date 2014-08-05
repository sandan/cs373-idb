from django.conf.urls import patterns, include, url
from django.contrib import admin
from haystack.views import SearchView
from myapp.views import DateRangeSearchForm
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^search/', SearchView(form_class=DateRangeSearchForm)),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('myapp.urls')),
)
