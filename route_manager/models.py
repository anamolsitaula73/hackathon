from django.db import models

class Route(models.Model):
    route_name = models.CharField(max_length=255)
    starting_point = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    route_data = models.TextField()

    def __str__(self):
        return self.route_name



class BusStop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='bus_stops')
    name = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"

# Bus Model
class Bus(models.Model):
    number_plate = models.CharField(max_length=15)
    driver_name = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Bus {self.number_plate} - Driver: {self.driver_name}"
