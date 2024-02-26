"""
URL configuration for dts_ver_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dts_ver_2_models import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashbord_fun, name='dashboard'),
    path('dashboard_page', views.dashbord_fun, name='Go_to_dashboard'),
    path('configuration_page', views.configure_page_fun, name='Go_to_configuration'),
    path('report_page', views.report_page, name='Go_to_report'),
    path('get_zone_config_data/',views.get_zone_config,name='get-zone-config-data'),
    path('insert_zone_config/', views.db_insert_zone_config_data, name='insert_zone_config'),
    path('default_Data/', views.default_data, name='default_data'),
    # path('default_end_Data/', views.default_end_data, name='default_end_data'),
    path('get_end_dist/',views.get_end_dist, name='get_end_dist'),
    path('update_channel_Config/', views.update_channel_config, name='update_channel_config'),
    path('channel_1', views.channel_1, name='channel_1'),
    path('channel_2', views.channel_2, name='channel_2'),
    path('channel_3', views.channel_3, name='channel_2'),
    path('channel_4', views.channel_4, name='channel_2'),
    path('delete_Data/', views.delete_Data, name='delete_data'),
    path('graph_data/', views.algo_graph, name='graph_data'),
    path('alarms', views.alarms, name='alarms'),
#   path('HTML1', views.html1, name='alarms'),
]
    
