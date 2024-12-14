from django.contrib import admin
from .models import Route, BusStop

class BusStopInline(admin.TabularInline):
    model = BusStop
    extra = 1  # Number of empty forms to display initially
    fields = ('lat', 'lon')  # Specify fields to show in the inline form

class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'starting_point', 'destination')
    inlines = [BusStopInline]
    search_fields = ('name', 'starting_point', 'destination')  # Add search functionality
    list_filter = ('starting_point', 'destination')  # Add filter options

admin.site.register(Route, RouteAdmin)
