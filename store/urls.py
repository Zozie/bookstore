from django.conf.urls import url
from views import store # index

urlpatterns = [
    url(r'^$', store, name='store'),
]
