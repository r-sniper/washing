from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [

    # / - Home Page
    url(r'^$', views.home_page, name='home_page'),
    # /get_customer
    url(r'^get_customer/$', views.get_customer, name='get_customer'),
    # /get_reports
    url(r'^reports/$', views.get_reports, name='get_reports'),
    # /new_order
    url(r'^new_order/$', views.new_order, name='new_order'),
]
