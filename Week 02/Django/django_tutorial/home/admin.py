from django.contrib import admin

from .models import Departments, Doctors,Booking

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')
    list_filter = ('booking_date', 'booked_on')
    search_fields = ('p_name', 'p_phone', 'p_email', 'doc_name')
    ordering = ('booking_date', 'booked_on')
    date_hierarchy = 'booked_on'
    list_per_page = 10


admin.site.register(Booking)
