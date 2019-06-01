from django.contrib import admin

from .models import Hitter


@admin.register(Hitter)
class HitterAdmin(admin.ModelAdmin):
    pass
