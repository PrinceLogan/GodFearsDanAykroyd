from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.get_deicide, name='get_deicide'),
    url(r'^about_us$', views.about_us, name='about_us'),
    url(r'^history$', views.history, name='history'),
]

