# owner/models.py
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class VenueOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_registration_number = models.CharField(max_length=100)
    business_registration_photo = models.ImageField(upload_to='business_registrations/')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    contact_email = models.EmailField(unique=True)
    zip_code = models.CharField(max_length=10,default=44207)  # New field for zip code
    average_cost_per_person = models.DecimalField(max_digits=10, decimal_places=2,default=0)  
    total_slots = models.PositiveIntegerField(default=0)  # New field for available slots
    occupancy = models.PositiveIntegerField(default=0) 
    contact_num = models.PositiveIntegerField(default=0) 
    
    image = models.ImageField(upload_to='venue_images/', null=True, blank=True)
    available_slots = models.PositiveIntegerField(editable=False)  # Non-editable field

    def save(self, *args, **kwargs):
        self.available_slots = self.total_slots - self.occupancy
        super().save(*args, **kwargs)  # New field for available slots


    


    def __str__(self):
        return self.name

    @staticmethod
    def recommend_venues(event_type, location, budget):
        venues = Venue.objects.filter(packages__price__lte=budget)
        if location:
            venues = venues.filter(address__icontains=location)
        return venues.distinct()

class PricingPackage(models.Model):
    id = models.AutoField(primary_key=True)
    venue = models.ForeignKey(Venue, related_name='packages', on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return f'{self.package_name} - {self.venue.name}'


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    contact_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False) 
    checked_out = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Booking {self.id} for {self.venue.name}'
