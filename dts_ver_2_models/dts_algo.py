import socket
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dts_ver_2.settings')
django.setup()

from .models import *

def dts_algo_fun():

    host = '192.168.1.120'
    port = 2404

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, port))
        
    while True:
        try:
            msg_r = s.recv(99999)
            main_list = []
            
            for i in range(len(msg_r)):
                int_val = msg_r[i]
                main_list.append(int_val) 
                
            #------------------------------------------------------- faulty alarm ---------------------------------------------------------

            if len(main_list)==19:
                #--------------------------------------------- Store No Fiber Data .....
                if main_list[5] == 1:
                    #print("channel : "+str(main_list[3])+" has no fiber.")
                    #----------------- Channel 1 .....
                    if int(main_list[3]) == 1:
                        print("channel : 1 has no fiber.")
                        validate_ch_1_db_data = channel_1_graph_data.objects.all()
                        if len(validate_ch_1_db_data) != 0:
                            validate_ch_1_db_data.delete()
                            
                        save_db_data = channel_1_graph_data(temprature_curve_x_axis=0, temprature_curve_y_axis=0 )
                        save_db_data.save()
                    
                    #----------------- Channel 2 .....
                    if int(main_list[3]) == 2:
                        print("channel : 2 has no fiber.")
                        validate_ch_2_db_data = channel_2_graph_data.objects.all()
                        if len(validate_ch_2_db_data) != 0:
                            validate_ch_2_db_data.delete()
                            
                        save_db_data = channel_2_graph_data(temprature_curve_x_axis=0, temprature_curve_y_axis=0 )
                        save_db_data.save()
                        
                    #----------------- Channel 3 .....
                    if int(main_list[3]) == 3:
                        print("channel : 3 has no fiber.")
                        validate_ch_3_db_data = channel_3_graph_data.objects.all()
                        if len(validate_ch_3_db_data) != 0:
                            validate_ch_3_db_data.delete()
                            
                        save_db_data = channel_3_graph_data(temprature_curve_x_axis=0, temprature_curve_y_axis=0 )
                        save_db_data.save()
                        
                    #----------------- Channel 4 .....
                    if int(main_list[3]) == 4:
                        print("channel : 4 has no fiber.")
                        
                        validate_ch_4_db_data = channel_4_graph_data.objects.all()
                        if len(validate_ch_4_db_data) != 0:
                            validate_ch_4_db_data.delete()
                            
                        save_db_data = channel_4_graph_data(temprature_curve_x_axis=0, temprature_curve_y_axis=0 )
                        save_db_data.save()
                
                #--------------------------------------------- Store Broken Fiber Data .....
                elif main_list[5] == 2:
                    #print("channel : "+str(main_list[3])+" has broken fiber.")
                    #----------------- Channel 1 .....
                    if int(main_list[3]) == 1:
                        print("channel : 1 has Broken fiber.")
                    
                    #----------------- Channel 2 .....
                    if int(main_list[3]) == 2:
                        print("channel : 2 has Broken fiber.")
                        
                    #----------------- Channel 3 .....
                    if int(main_list[3]) == 3:
                        print("channel : 3 has Broken fiber.")
                        
                    #----------------- Channel 4 .....
                    if int(main_list[3]) == 4:
                        print("channel : 4 has Broken fiber.")
                
            else:                                         # ----- get a temperature data .....
                get_ch_num = main_list[3]
                
                final_list = main_list[5:-2]
                        
                temp_list = []             # use for store data indicator's
                main_data_list = []        # use for store real data's.
                
                find_detect_data_num = 0
                for i in range(len(final_list)):
                    if i == find_detect_data_num:
                        data = final_list[find_detect_data_num]
                        temp_list.append(data)
                        find_detect_data_num+=2
                    
                    else:
                        data = final_list[i]
                        main_data_list.append(data)
                
                store_db_data_list = []
                x_data_temp_num = 1
                #print("first val of temp list : "+str(main_data_list[0]))
                for i in range(len(temp_list)):
                    #indexing = temp_list[i]
                    if temp_list[i] == 4:
                        con_to_hex = hex(main_data_list[i])
                        con_to_ls = con_to_hex.split('0x')
                        final_hex_val = con_to_ls[1]
                        #print("final hex val : "+str(final_hex_val))
                        test_hex = int(final_hex_val,16)
                        try:
                            if int(test_hex)<10:
                                final_hex_val = '0'+str(test_hex)
                            elif final_hex_val == 'a':
                                final_hex_val = '0a'
                            elif final_hex_val == 'b':
                                final_hex_val = '0b'
                            elif final_hex_val == 'c':
                                final_hex_val = '0c'
                            elif final_hex_val == 'd':
                                final_hex_val = '0d'
                            elif final_hex_val == 'e':
                                final_hex_val = '0e'
                            elif final_hex_val == 'f':
                                final_hex_val = '0f'
                        except:
                            #print("--------------------------- data was not added------------------")
                            pass
                        final_val = '0x04'+final_hex_val
                        #print(final_val)
                        a = int(final_val,16)
                        #print(a)
                        b = 1000
                        c = a-b
                        final_data = str(c/10)
                        
                        x_data = 0.8*x_data_temp_num
                        x_data = str("{:.2f}".format(x_data))
                        
                        temp_temperature_data = [x_data,final_data]
                        store_db_data_list.append(temp_temperature_data)
                        x_data_temp_num +=1
                    
                    elif temp_list[i] == 5:
                        con_to_hex = hex(main_data_list[i])
                        con_to_ls = con_to_hex.split('0x')
                        final_hex_val = con_to_ls[1]
                        test_hex = int(final_hex_val,16)
                        try:
                            if int(test_hex)<10:
                                final_hex_val = '0'+str(test_hex)
                            elif final_hex_val == 'a':
                                final_hex_val = '0a'
                            elif final_hex_val == 'b':
                                final_hex_val = '0b'
                            elif final_hex_val == 'c':
                                final_hex_val = '0c'
                            elif final_hex_val == 'd':
                                final_hex_val = '0d'
                            elif final_hex_val == 'e':
                                final_hex_val = '0e'
                            elif final_hex_val == 'f':
                                final_hex_val = '0f'
                        except:
                            pass
                        final_val = '0x04'+final_hex_val
                        #print(final_val)
                        a = int(final_val,16)
                        b = 1000
                        c = a-b
                        final_data = c/10
                        final_data = str(25.5+final_data)
                        
                        x_data = 0.8*x_data_temp_num
                        x_data = str("{:.2f}".format(x_data))
                        
                        temp_temperature_data = [x_data,final_data]
                        store_db_data_list.append(temp_temperature_data)
                        x_data_temp_num +=1
                        
                    elif temp_list[i] == 6:
                        con_to_hex = hex(main_data_list[i])
                        con_to_ls = con_to_hex.split('0x')
                        final_hex_val = con_to_ls[1]
                        test_hex = int(final_hex_val,16)
                        try:
                            if int(test_hex)<10:
                                final_hex_val = '0'+str(test_hex)
                            elif final_hex_val == 'a':
                                final_hex_val = '0a'
                            elif final_hex_val == 'b':
                                final_hex_val = '0b'
                            elif final_hex_val == 'c':
                                final_hex_val = '0c'
                            elif final_hex_val == 'd':
                                final_hex_val = '0d'
                            elif final_hex_val == 'e':
                                final_hex_val = '0e'
                            elif final_hex_val == 'f':
                                final_hex_val = '0f'
                        except:
                            pass
                        final_val = '0x04'+final_hex_val
                        #print(final_val)
                        a = int(final_val,16)
                        b = 1000
                        c = a-b
                        final_data = c/10
                        final_data = str(51+final_data)
                        
                        x_data = 0.8*x_data_temp_num
                        x_data = str("{:.2f}".format(x_data))
                        
                        csv_list_data = [x_data,final_data]
                        store_db_data_list.append(csv_list_data)
                        x_data_temp_num +=1
                    
                    elif temp_list[i] == 3 :
                        x_data_temp_num +=1
                        
                        
                #------------------------------- Store Temperature Data In DataBase .....
                
                if int(get_ch_num) == 1:
                    # print("channel 1 store_db_data_list : "+str(store_db_data_list))
                    
                    validate_ch_1_db_data = channel_1_graph_data.objects.all()
                    if len(validate_ch_1_db_data) != 0:
                        validate_ch_1_db_data.delete()
                    
                    ch_1_instance = [channel_1_graph_data(temprature_curve_x_axis=get_d[0], temprature_curve_y_axis=get_d[1]) for get_d in store_db_data_list]
                    channel_1_graph_data.objects.bulk_create(ch_1_instance)
                    
                    print("-------------------- channel 1 data insertion complate .....")
                
                
                if int(get_ch_num) == 2:
                    # print("channel 2 store_db_data_list : "+str(store_db_data_list))
                    
                    validate_ch_2_db_data = channel_2_graph_data.objects.all()
                    if len(validate_ch_2_db_data) != 0:
                        validate_ch_2_db_data.delete()
                        
                    ch_2_instance = [channel_2_graph_data(temprature_curve_x_axis=get_d[0], temprature_curve_y_axis=get_d[1]) for get_d in store_db_data_list]
                    channel_2_graph_data.objects.bulk_create(ch_2_instance)
                    # print("-------------------- channel 2 data insertion complate .....")
                
                
                if int(get_ch_num) == 3:
                    # print("channel 3 store_db_data_list : "+str(store_db_data_list))
                    
                    validate_ch_3_db_data = channel_3_graph_data.objects.all()
                    if len(validate_ch_3_db_data) != 0:
                        validate_ch_3_db_data.delete()
                        
                    ch_3_instance = [channel_3_graph_data(temprature_curve_x_axis=get_d[0], temprature_curve_y_axis=get_d[1]) for get_d in store_db_data_list]
                    channel_3_graph_data.objects.bulk_create(ch_3_instance)
                    # print("-------------------- channel 3 data insertion complate .....")
                
                
                if int(get_ch_num) == 4:
                    # print("channel 4 store_db_data_list : "+str(store_db_data_list))
                    
                    validate_ch_4_db_data = channel_4_graph_data.objects.all()
                    if len(validate_ch_4_db_data) != 0:
                        validate_ch_4_db_data.delete()
                        
                    ch_4_instance = [channel_4_graph_data(temprature_curve_x_axis=get_d[0], temprature_curve_y_axis=get_d[1]) for get_d in store_db_data_list]
                    channel_4_graph_data.objects.bulk_create(ch_4_instance)
                    # print("-------------------- channel 4 data insertion complate .....")
                    
                #------------------------------- Store Broken Position In Database .....
                
                # if int(get_ch_num) == 1:
                #     broken_fiber_data = [str(store_db_data_list[-1][0]),str(store_db_data_list[-1][1])]
                #     print("ch 1 broken fiber position : "+str(broken_fiber_data))
                
                # if int(get_ch_num) == 2:
                #     broken_fiber_data = [str(store_db_data_list[-1][0]),str(store_db_data_list[-1][1])]
                #     print("ch 2 broken fiber position : "+str(broken_fiber_data))
                    
                # if int(get_ch_num) == 3:
                #     broken_fiber_data = [str(store_db_data_list[-1][0]),str(store_db_data_list[-1][1])]
                #     print("ch 3 broken fiber position : "+str(broken_fiber_data))
                    
                # if int(get_ch_num) == 4:
                #     broken_fiber_data = [str(store_db_data_list[-1][0]),str(store_db_data_list[-1][1])]
                #     print("ch 4 broken fiber position : "+str(broken_fiber_data))

        except:
            pass
                
