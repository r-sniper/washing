from django.conf.urls import url

from . import views

app_name = 'home'


urlpatterns = [

    # / - Home Page
    url(r'^$', views.home_page, name='home_page'),
    # orders page
    url(r'^orders/$', views.orders, name='orders'),
    # /get_customer
    url(r'^clothwise/$', views.clothwise, name='clothwise'),
    # /get_customer
    url(r'^expenses/$', views.expenses, name='expenses'),
    # /get_customer
    url(r'^get_customer/$', views.get_customer, name='get_customer'),
    # /get_reports
    url(r'^reports/$', views.get_reports, name='get_reports'),
    # /new_order
    url(r'^new_order/(?P<customer_id>[0-9]+)/$', views.new_order, name='new_order'),
    # / register customer
    url(r'^register_customer/$', views.customer_registration, name='register_customer'),
    # /change_status
    url(r'^change_status/$', views.change_status, name='change_status'),
    # / register customer
    url(r'^daywise_excel/$', views.day_excel, name='daywise_excel'),
    # / General Excel
    url(r'^general_excel/(?P<type>[\w]+)$', views.general_excel, name='general_excel'),
    url(r'^general_excel/$', views.general_excel, name='general_excel'),

]
