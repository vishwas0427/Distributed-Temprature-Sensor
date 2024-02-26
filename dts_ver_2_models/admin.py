from django.contrib import admin
from .models import num_of_channel,channel_config,zone_config,channel_1_graph_data,channel_2_graph_data,channel_3_graph_data,channel_4_graph_data

# Register your models here.


class num_of_channel_admin(admin.ModelAdmin):
    list_disp = tuple("total_channel")


class channel_config_admin(admin.ModelAdmin):
    list_display = ("channel_num", "fiber_len")

class zone_config_admin(admin.ModelAdmin):
    list_display = ("channel_num", "zone_name", "start_dist", "end_dist", "temp_orange_alarm_max", "temp_orange_alarm_min", 
                    "temp_red_alarm_max", "temp_red_alarm_min")
    

class channel_1_graph_data_admin(admin.ModelAdmin):
    list_display=('temprature_curve_x_axis','temprature_curve_y_axis')

class channel_2_graph_data_admin(admin.ModelAdmin):
    list_display=('temprature_curve_x_axis','temprature_curve_y_axis')

class channel_3_graph_data_admin(admin.ModelAdmin):
    list_display=('temprature_curve_x_axis','temprature_curve_y_axis')

class channel_4_graph_data_admin(admin.ModelAdmin):
    list_display=('temprature_curve_x_axis','temprature_curve_y_axis')            

admin.site.register(num_of_channel,num_of_channel_admin)
admin.site.register(channel_config,channel_config_admin)
admin.site.register(zone_config,zone_config_admin)
admin.site.register(channel_1_graph_data,channel_1_graph_data_admin)
admin.site.register(channel_2_graph_data,channel_2_graph_data_admin)
admin.site.register(channel_3_graph_data,channel_3_graph_data_admin)
admin.site.register(channel_4_graph_data,channel_4_graph_data_admin)
