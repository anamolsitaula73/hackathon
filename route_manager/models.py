# route_manager/models.py
from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    starting_point = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class BusStop(models.Model):
    route = models.ForeignKey(Route, related_name='bus_stops', on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Bus Stop'
        verbose_name_plural = 'Bus Stops'

    def __str__(self):
        return f"Bus Stop at ({self.lat}, {self.lon})"


# Bus Model
class Bus(models.Model):
    number_plate = models.CharField(max_length=15)
    driver_name = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Bus {self.number_plate} - Driver: {self.driver_name}"
