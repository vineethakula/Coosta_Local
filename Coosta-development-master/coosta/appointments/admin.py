from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(OpenHouse)
admin.site.register(OpenHouseRSVP)
admin.site.register(OwnerAvailability)
admin.site.register(AppointmentRequest)