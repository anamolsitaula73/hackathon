from django.contrib import admin
from .models import VenueOwner
from django.core.mail import send_mail
# venues/admin.py
from django.contrib import admin
from .models import Venue, PricingPackage, Booking

class VenueOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'business_registration_number', 'verified']
    list_filter = ['verified']
    actions = ['verify_owners']

    def email(self, obj):
        return obj.user.email

    def verify_owners(self, request, queryset):
        queryset.update(verified=True)
        for owner in queryset:
            send_mail(
                'Registration Verified',
                'Your registration has been verified.',
                'eventgenius888@gmail.com',
                [owner.user.email],
                fail_silently=False,
            )

    verify_owners.short_description = 'Verify selected venue owners'

admin.site.register(VenueOwner, VenueOwnerAdmin)



class PricingPackageInline(admin.TabularInline):
    model = PricingPackage
    extra = 1

class VenueAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address', 'contact_email','contact_num','zip_code', 'average_cost_per_person', 'available_slots','total_slots','occupancy')
    search_fields = ('name', 'address')
    inlines = [PricingPackageInline]




class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'venue', 'date', 'contact_email','time', 'number_of_guests', 'booked_at')
    list_filter = ('venue', 'date', 'user')
    search_fields = ('venue__name', 'user__username', 'date')

admin.site.register(Booking, BookingAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(PricingPackage)


