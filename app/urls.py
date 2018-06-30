from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import shuttletracker.views

# Examples:
# url(r'^$', 'app.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', shuttletracker.views.index, name='index'),
    url(r'^json', shuttletracker.views.jsontest, name='json'),
]
