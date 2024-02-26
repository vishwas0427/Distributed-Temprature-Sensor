from django.shortcuts import render
from django.http import JsonResponse
from .models import num_of_channel, channel_config, zone_config,channel_1_graph_data,channel_2_graph_data,channel_3_graph_data,channel_4_graph_data
from dts_ver_2_models.dts_algo import dts_algo_fun
from threading import Thread
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.html import json_script
import json

th = Thread(target=dts_algo_fun)
th.daemon = True
th.start()

def dashbord_fun(request):
    # zone_config_data = list(zone_config.objects.all().values())
    # print(zone_config_data)

    return render(request,'dashboard.html',)
def html1(request):
    return render(request,'HTML1.html',)
def go_dashbord_fun(request):

    return render(request,'dashboard.html')
def report_page(request):
    return render(request,'report.html')

def configure_page_fun(request):
    channel_automate()
    zone_start_dist_automate()
    return render(request,'configuration.html')

def get_zone_config(request):
    zone_config_data = list(zone_config.objects.all().values())
    # print(zone_config_data) 
    zone_config_data = sorted(zone_config_data, key=lambda x: float(x['channel_num']))
    return JsonResponse({'zone_config_data':zone_config_data})

def db_insert_zone_config_data(request):
    if request.method == 'POST':
        try:
            get_zone_list = request.POST.getlist('zone_config_list[]') 
            save_zone_config = zone_config(channel_num=get_zone_list[0], zone_name=get_zone_list[1], start_dist=get_zone_list[2], end_dist=get_zone_list[3], 
                                           temp_orange_alarm_max=get_zone_list[4], temp_orange_alarm_min=get_zone_list[5], temp_red_alarm_max=get_zone_list[6], temp_red_alarm_min=get_zone_list[7])    
            save_zone_config.save()
            return JsonResponse({'success': True, 'message': 'Data inserted successfully'})  
        except:
            return JsonResponse({'success': False, 'message': 'Data inserted failed'})
        
def channel_automate() :
    get_ch_auto = list(channel_config.objects.all().values())
    if len(get_ch_auto) == 0:
        ch_1 = channel_config(channel_num='1',fiber_len='5000')
        ch_1.save()
        ch_1 = channel_config(channel_num='2',fiber_len='5000')
        ch_1.save()
        ch_1 = channel_config(channel_num='3',fiber_len='5000')
        ch_1.save()
        ch_1 = channel_config(channel_num='4',fiber_len='5000')
        ch_1.save()

def default_data(request):
    data=list(channel_config.objects.values('fiber_len').order_by('id'))
    get_channel_fiber = [item['fiber_len'] for item in data]
    return JsonResponse({'get_channel_fiber':get_channel_fiber,})

def zone_start_dist_automate() :
    get_start_dist =list(zone_config.objects.all().values())
    # sorted_data = sorted(get_start_dist, key=lambda x: int(x['channel_num']))
    # print(get_start_dist)""
    if len(get_start_dist) == 0:
        ch = zone_config(channel_num='1',start_dist='0',end_dist='0')
        ch.save()
        ch = zone_config(channel_num='2',start_dist='0',end_dist='0')
        ch.save()
        ch = zone_config(channel_num='3',start_dist='0',end_dist='0')
        ch.save()
        ch = zone_config(channel_num='4',start_dist='0',end_dist='0')
        ch.save()

def get_last_displayed_data(request):
    channel_num = request.GET.get('channel_num')  
    # Fetch the last displayed data for the selected channel
    last_displayed_data = zone_config.objects.filter(channel_num=channel_num).last()  
    # Prepare the data to be sent as a JSON response
    data = {
        'fiber_length': last_displayed_data.fiber_length if last_displayed_data else 0,
    }
    return JsonResponse(data)

def get_end_dist(request):
    channel_num = request.GET.get('channel_num')
    latest_zone = zone_config.objects.filter(channel_num=channel_num).latest('id')
    data = {'end_dist': latest_zone.end_dist}
    return JsonResponse(data)


def update_channel_config(request):
    global get_fiber_len,get_channel_num
    if request.method == 'POST':
        get_channel_num=request.POST.get('channel_num')
        get_fiber_len=request.POST.get('fiber_len')
        channel_obj = channel_config.objects.get(channel_num=get_channel_num)           #update -id to channel_num
        channel_obj.fiber_len = get_fiber_len
        channel_obj.save()
        return render(request,'configuration.html')
    
def channel_1(request):
    return render(request,'channel 1.html')
def channel_2(request):
    return render(request,'channel 2.html')
def channel_3(request):
    return render(request,'channel 3.html')
def channel_4(request):
    return render(request,'channel 4.html')

def delete_Data(request):
    if request.method == 'POST':
        selectedValue = request.POST.get('selectedValue')
        matching_entries = zone_config.objects.filter(channel_num=str(selectedValue))
        if matching_entries.exists():
            last_matching_entry = matching_entries.last()
            last_matching_entry.delete()
            print(f"Deleted the last entry with 'channel_num' equal to {selectedValue}")
        else:
            print(f"No entries found with 'channel_num' equal to {selectedValue}")

    return render(request, 'configuration.html')


def algo_graph(request):
    a=list(channel_1_graph_data.objects.all().values())[:-2]
    # print(a)
    a1=list(channel_2_graph_data.objects.all().values())[:-2]
    a2=list(channel_3_graph_data.objects.all().values())[:-2]
    a3=list(channel_4_graph_data.objects.all().values())[:-2]
    zonedata=list(zone_config.objects.all().values())
    All_channels=[list(channel_1_graph_data.objects.all().values())[:-2],list(channel_2_graph_data.objects.all().values())[:-2],
                  list(channel_3_graph_data.objects.all().values())[:-2],list(channel_4_graph_data.objects.all().values())[:-2]]
    # print(zonedata)
    ch1_x_data=[item['temprature_curve_x_axis'] for item in a]
    ch1_y_data=[item['temprature_curve_y_axis'] for item in a]
    ch2_x_data=[item['temprature_curve_x_axis'] for item in a1]
    ch2_y_data=[item['temprature_curve_y_axis'] for item in a1]
    ch3_x_data=[item['temprature_curve_x_axis'] for item in a2]
    ch3_y_data=[item['temprature_curve_y_axis'] for item in a2]
    ch4_x_data=[item['temprature_curve_x_axis'] for item in a3]
    ch4_y_data=[item['temprature_curve_y_axis'] for item in a3]
    return JsonResponse({'ch1_x_data':ch1_x_data,'ch1_y_data':ch1_y_data,
                         'ch2_x_data':ch2_x_data,'ch2_y_data':ch2_y_data,
                         'ch3_x_data':ch3_x_data,'ch3_y_data':ch3_y_data,
                         'ch4_x_data':ch4_x_data,'ch4_y_data':ch4_y_data,
                        'zonedata': zonedata, 'All_channels': All_channels
                        })


    return render(request, 'channel 1.html', {'zonedata_json': zonedata_json,
        'All_channels_json': All_channels_json})

# ===============================ALARM=======================================

def alarms(request):    
    return render(request, 'alarms.html')
