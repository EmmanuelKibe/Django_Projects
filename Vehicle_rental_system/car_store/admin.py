from django.contrib import admin
from .models import Cars
from .models import Size

# Register your models here.
class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'price')
    search_fields = ('name', 'model')
    list_filter = ('year',)

admin.site.register(Size)
admin.site.register(Cars, CarsAdmin)
admin.site.site_header = "Vehicle Rental System Admin"