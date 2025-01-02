from django.db import models

# Create your models here.




class Server_1(models.Model):
    """
    !Desc:
        - This Model is for OS Data Storage of Server-1.
    """
    datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    cpu_percent = models.FloatField(null=True)
    cpu_count = models.FloatField(null=True)
    cpu_freq_current = models.FloatField(null=True)
    getloadavg_1min = models.FloatField(null=True)
    getloadavg_5min = models.FloatField(null=True)
    getloadavg_15min = models.FloatField(null=True)
    virtual_memory_total = models.FloatField(null=True)
    virtual_memory_used = models.FloatField(null=True)
    virtual_memory_available = models.FloatField(null=True)
    virtual_memory_free = models.FloatField(null=True)
    virtual_memory_percent = models.FloatField(null=True)
    swap_memory_total = models.FloatField(null=True)
    swap_memory_used = models.FloatField(null=True)
    swap_memory_free = models.FloatField(null=True)
    swap_memory_percent = models.FloatField(null=True)
    disk_usage_total = models.FloatField(null=True)
    disk_usage_used = models.FloatField(null=True)
    disk_usage_free = models.FloatField(null=True)
    disk_usage_percent = models.FloatField(null=True)
    net_io_counters_lo_bytes_sent = models.FloatField(null=True)
    net_io_counters_lo_bytes_recv = models.FloatField(null=True)
    net_io_counters_eth0_bytes_sent = models.FloatField(null=True)
    net_io_counters_eth0_bytes_recv = models.FloatField(null=True)

