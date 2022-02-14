
from django.urls import path

from .views import manifest, service_worker, offline

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    path(r'^serviceworker\.js$', service_worker, name='serviceworker'),
    path(r'^manifest\.json$', manifest, name='manifest'),
    path('^offline/$', offline, name='offline')
]
