from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'sidekick.views.home', name='home'),
    url(r'^candidate/', include('candidate.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'sidekick.views.login', name='login'),
    url(r'^logout/', 'sidekick.views.logout', name='logout'),
    url(r'^profile/', 'sidekick.views.profile', name='profile'),
]
