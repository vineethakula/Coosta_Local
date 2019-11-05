from django.contrib import admin

from flags.models import FlaggedProperty, FlagType

admin.site.register(FlagType)
admin.site.register(FlaggedProperty)
