from django.contrib import admin
from .models import TicketMoel


@admin.register(TicketMoel)
class TicketAdmin(admin.ModelAdmin):
    pass
