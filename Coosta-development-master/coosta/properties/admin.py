from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(Images)
admin.site.register(PropertyStatus)
admin.site.register(ShortListedProperty)
admin.site.register(Parcel)