from django.contrib import admin
from customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","mobile","address","date")

# Register your models here.
admin.site.register(Customer,CustomerAdmin)