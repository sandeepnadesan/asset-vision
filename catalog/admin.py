from datetime import date
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .resources import DevicelistResource, AssettagResource
from .models import Customer, Model, Device, Type, Tracker, Archive, Inventory, Location, Department

# Register your models here.
admin.site.register(Model)
admin.site.register(Type)

# Define the admin class for Tracker
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes', 'customer', 'cus2', 'equip', 'credate', 'deptout', 'deptin')
    fields = [('name', 'notes'), ('deptout', 'deptin'), ('equip', 'equip1'), 'credate', ('customer', 'cus2')]
    search_fields = ['name', 'credate']

admin.site.register(Tracker, TrackerAdmin)

# Admin class for Customer with import/export functionality
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'department', 'location')
    fields = ['first_name', 'last_name', 'department', 'location']
    search_fields = ['first_name', 'last_name', 'department']

admin.site.register(Customer, CustomerAdmin)

# Admin class for Device with import/export functionality
class DeviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('hostname', 'model', 'customer', 'serialn', 'type', 'tag', 'buydate', 'warranty', 'status', 'substatus', 'modified')
    fields = ['hostname', ('model', 'serialn'), ('type', 'buydate'), ('customer', 'location'), ('tag', 'warranty'), ('status', 'substatus'), 'cost', 'notes']
    search_fields = ['hostname', 'model__name', 'customer__last_name', 'serialn', 'tag', 'type__type', 'substatus']
    resource_class = DevicelistResource

admin.site.register(Device, DeviceAdmin)

# Admin class for Archive with import/export functionality
class ArchiveAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('hostname', 'model', 'customer', 'serialn', 'type', 'tag', 'buydate', 'warranty', 'status', 'substatus', 'modified')
    fields = ['hostname', ('model', 'serialn'), ('type', 'buydate'), ('customer', 'location'), ('tag', 'warranty'), ('status', 'substatus'), 'cost', 'notes']
    search_fields = ['hostname', 'model__name', 'customer__last_name', 'serialn', 'tag', 'type__type', 'substatus']
    resource_class = DevicelistResource

admin.site.register(Archive, ArchiveAdmin)

# Admin class for Inventory with import/export functionality
class InventoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('num', 'snum')
    resource_class = AssettagResource

admin.site.register(Inventory, InventoryAdmin)

# Admin class for Location
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Location, LocationAdmin)

# Admin class for Department
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Department, DepartmentAdmin)
