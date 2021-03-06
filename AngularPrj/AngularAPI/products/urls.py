from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/$', views.product_list),
    url(r'^products/(?P<pk>[0-9]+)$', views.product_detail),
    url(r'^products/price/(?P<price>[0-9]+)/$', views.product_list_price),
]