from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [

    # / - Home Page
    url(r'^$', views.home_page, name='home_page'),
    # /get_customer
    url(r'^get_customer/$', views.get_customer, name='get_customer'),
]
