from django.contrib import admin
from .models import Route

class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'starting_point', 'destination', 'route_data')
    search_fields = ['route_name', 'starting_point', 'destination']
    list_filter = ['route_name', 'destination']
    
    # Make route_name the link to the detailed object
    list_display_links = ('route_name',)

    # Optionally add a route data preview
    def route_data_preview(self, obj):
        return str(obj.route_data)[:50]  # Display the first 50 characters of the route data
    route_data_preview.short_description = 'Route Data Preview'

admin.site.register(Route, RouteAdmin)
