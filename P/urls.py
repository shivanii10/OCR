from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^translated/$', views.translated, name='translated'),
    url(r'^extracted/$', views.extracted, name='extracted'),

]