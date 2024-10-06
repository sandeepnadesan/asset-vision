from django.urls import path
from . import views
from django.urls import re_path

from .views import ListView, SearchResultsView

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index1'),
    path('search/', SearchResultsView.as_view(), name='search_result'),
    re_path(r'^inventorys/$', views.InventoryListView.as_view(), name='inventory'),
    re_path(r'^devices/$', views.DeviceListView.as_view(), name='devices'),
    re_path(r'^device/(?P<pk>\d+)$', views.DeviceDetailView.as_view(), name='device-detail'),
    re_path(r'^customers/$', views.CustomerListView.as_view(), name='customers'),
    re_path(r'^customer/(?P<pk>\d+)$', views.CustomerDetailView.as_view(), name='customer_detail'),
    re_path(r'^trackers/$', views.TrackerListView.as_view(), name='trackers'),
    re_path(r'^tracker/(?P<pk>\d+)$', views.TrackerDetailView.as_view(), name='tracker_detail'),

]