from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import dhiren_web.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dhiren', dhiren_web.views.me, name='me'),
    url(r'^resume', dhiren_web.views.dhiren, name='dhiren'),
]
