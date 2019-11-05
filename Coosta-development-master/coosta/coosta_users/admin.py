from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserProfile)
admin.site.register(NonPreApprovedUser)
admin.site.register(PreApprovedUser)
admin.site.register(Documents)
admin.site.register(PreApprovedDocuments)
