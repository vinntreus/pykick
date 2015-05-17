from django.conf.urls import url

urlpatterns = [
    url(r'^create/', 'candidate.views.create', name='create_candidate'),
    url(r'^(?P<candidate_id>\d+)/update/(?P<field>\w+)/',
        'candidate.views.update', name='update_candidate'),
    url(r'^(?P<candidate_id>\d+)/', 'candidate.views.index', name='candidate'),
]
