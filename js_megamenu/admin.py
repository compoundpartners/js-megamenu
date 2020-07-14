from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import MegamenuExtension


class MegamenuExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(MegamenuExtension, MegamenuExtensionAdmin)
