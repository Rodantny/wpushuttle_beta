from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import template.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', template.views.index, name='index'),
    url(r'^json', template.views.jsontest, name='json'),
]
