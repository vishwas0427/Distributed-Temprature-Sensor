from django.db import models

# Create your models here.

class num_of_channel(models.Model):
    total_channel = models.CharField(max_length=5)

class channel_config(models.Model):
    channel_num = models.CharField(max_length=5)
    fiber_len = models.CharField(max_length=10)

class zone_config(models.Model):
    channel_num = models.CharField(max_length=5)
    zone_name = models.CharField(max_length=40)
    start_dist = models.CharField(max_length=30)
    end_dist = models.CharField(max_length=30)
    temp_orange_alarm_max = models.CharField(max_length=30)
    temp_orange_alarm_min = models.CharField(max_length=30)
    temp_red_alarm_max = models.CharField(max_length=30)
    temp_red_alarm_min = models.CharField(max_length=30)

class channel_1_graph_data(models.Model):
    # No_fiber=models.CharField(max_length=50000)
    # Broken_fiber=models.CharField(max_length=50000)
    temprature_curve_x_axis=models.CharField(max_length=50000)
    temprature_curve_y_axis=models.CharField(max_length=50000)

class channel_2_graph_data(models.Model):
    # No_fiber=models.CharField(max_length=50000)
    # Broken_fiber=models.CharField(max_length=50000)
    temprature_curve_x_axis=models.CharField(max_length=50000)
    temprature_curve_y_axis=models.CharField(max_length=50000)
class channel_3_graph_data(models.Model):
    # No_fiber=models.CharField(max_length=50000)
    # Broken_fiber=models.CharField(max_length=50000)
    temprature_curve_x_axis=models.CharField(max_length=50000)
    temprature_curve_y_axis=models.CharField(max_length=50000)
class channel_4_graph_data(models.Model):
    # No_fiber=models.CharField(max_length=50000)
    # Broken_fiber=models.CharField(max_length=50000)
    temprature_curve_x_axis=models.CharField(max_length=50000)
    temprature_curve_y_axis=models.CharField(max_length=50000)