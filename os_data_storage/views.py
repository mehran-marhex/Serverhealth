from django.shortcuts import render
from django.http import HttpResponse
from .models import Server_1
import psutil
import time

# Create your views here.

def index(request):

    return HttpResponse(f"<h1 style='font-size: 60px;'>This is Server  *** 1 ***</h1>")




def os_data_storage():

    def data_getter_saver():
        # ========================<<   CPU   >>=========================
        # cpu_times = psutil.cpu_times()
        cpu_percent = psutil.cpu_percent()
        cpu_count = psutil.cpu_count()
        # cpu_count_logical = psutil.cpu_count(logical=True)
        # cpu_stats = psutil.cpu_stats()
        cpu_freq_current = psutil.cpu_freq().current

        getloadavg_1min = psutil.getloadavg()[0]
        getloadavg_5min = psutil.getloadavg()[1]
        getloadavg_15min = psutil.getloadavg()[2]

        # ========================<<   Memory   >>=========================
        # virtual_memory = psutil.virtual_memory()
        virtual_memory_total = psutil.virtual_memory().total
        virtual_memory_used = psutil.virtual_memory().used
        virtual_memory_available = psutil.virtual_memory().available
        virtual_memory_free = psutil.virtual_memory().free
        virtual_memory_percent = psutil.virtual_memory().percent

        # swap_memory = psutil.swap_memory()
        swap_memory_total = psutil.swap_memory().total
        swap_memory_used = psutil.swap_memory().used
        swap_memory_free = psutil.swap_memory().free
        swap_memory_percent = psutil.swap_memory().percent

        # ========================<<   Disks   >>=========================
        # disk_partitions = psutil.disk_partitions()
        # disk_usage = psutil.disk_usage('/')
        disk_usage_total = psutil.disk_usage('/').total
        disk_usage_used = psutil.disk_usage('/').used
        disk_usage_free = psutil.disk_usage('/').free
        # disk_io_counters = psutil.disk_io_counters(perdisk=False)
        disk_usage_percent = psutil.disk_usage('/').percent
        # ========================<<   Network   >>=========================
        # net_io_counters = psutil.net_io_counters(pernic=True)
        # net_io_counters_lo = psutil.net_io_counters(pernic=True)['lo']
        net_io_counters_lo_bytes_sent = psutil.net_io_counters(pernic=True)['lo'].bytes_sent
        net_io_counters_lo_bytes_recv = psutil.net_io_counters(pernic=True)['lo'].bytes_recv
        # net_io_counters_eth0 = psutil.net_io_counters(pernic=True)['eth0']
        net_io_counters_eth0_bytes_sent = psutil.net_io_counters(pernic=True)['eth0'].bytes_sent
        net_io_counters_eth0_bytes_recv = psutil.net_io_counters(pernic=True)['eth0'].bytes_recv
        # net_connections = psutil.net_connections(kind='tcp')
        # net_if_addrs = psutil.net_if_addrs()
        # net_if_stats = psutil.net_if_stats()
        # ========================<<   Sensors   >>=========================
        # sensors_temperatures = psutil.sensors_temperatures()
        # sensors_fans = psutil.sensors_fans()
        # sensors_battery = psutil.sensors_battery()
        # ========================<<   Other System Info   >>=========================
        # users = psutil.users()
        # boot_time = psutil.boot_time()

        

        Server_1.objects.create(
            cpu_percent = cpu_percent,
            cpu_count = cpu_count,
            cpu_freq_current = cpu_freq_current,
            getloadavg_1min = getloadavg_1min,
            getloadavg_5min = getloadavg_5min,
            getloadavg_15min = getloadavg_15min,
            virtual_memory_total = virtual_memory_total,
            virtual_memory_used = virtual_memory_used,
            virtual_memory_available = virtual_memory_available,
            virtual_memory_free = virtual_memory_free,
            virtual_memory_percent = virtual_memory_percent,
            swap_memory_total = swap_memory_total,
            swap_memory_used = swap_memory_used,
            swap_memory_free = swap_memory_free,
            swap_memory_percent = swap_memory_percent,
            disk_usage_total = disk_usage_total,
            disk_usage_used = disk_usage_used,
            disk_usage_free = disk_usage_free,
            disk_usage_percent = disk_usage_percent,
            net_io_counters_lo_bytes_sent = net_io_counters_lo_bytes_sent,
            net_io_counters_lo_bytes_recv = net_io_counters_lo_bytes_recv,
            net_io_counters_eth0_bytes_sent = net_io_counters_eth0_bytes_sent,
            net_io_counters_eth0_bytes_recv = net_io_counters_eth0_bytes_recv,
        )



        
    while True:
        data_getter_saver()
        time.sleep(1)





    # print(f"""
    #     ========================<<   CPU   >>=========================
    #     cpu_percent : {cpu_percent} 
    #     cpu_count: {cpu_count}
    #     cpu_freq: {cpu_freq_current}
    #
    #     getloadavg_1min: {getloadavg_1min}
    #     getloadavg_5min: {getloadavg_5min}
    #     getloadavg_15min: {getloadavg_15min}
    #
    #
    #     ========================<<   Memory   >>=========================
    #     virtual_memory_total: {virtual_memory_total}
    #     virtual_memory_used: {virtual_memory_used}
    #     virtual_memory_available: {virtual_memory_available}
    #     virtual_memory_free: {virtual_memory_free}
    #     virtual_memory_percent: {virtual_memory_percent}
    #
    #     swap_memory_total: {swap_memory_total}
    #     swap_memory_used: {swap_memory_used}
    #     swap_memory_free: {swap_memory_free}
    #     swap_memory_percent: {swap_memory_percent}
    #
    #     ========================<<   Disks   >>=========================
    #     disk_usage_total: {disk_usage_total}.
    #     disk_usage_used: {disk_usage_used}
    #     disk_usage_free: {disk_usage_free}
    #     disk_usage_percent: {disk_usage_percent}
    #
    #     ========================<<   Network   >>=========================
    #     net_io_counters_lo_bytes_sent: {net_io_counters_lo_bytes_sent}
    #     net_io_counters_lo_bytes_recv: {net_io_counters_lo_bytes_recv}
    #     net_io_counters_eth0_bytes_sent: {net_io_counters_eth0_bytes_sent}
    #     net_io_counters_eth0_bytes_recv: {net_io_counters_eth0_bytes_recv}
    #
    # """)

   












