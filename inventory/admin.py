from django.contrib import admin
from .models import Sensor, Module, Plate, Pcb, Plate, Shipment, Shipped_item

class SensorAdmin(admin.ModelAdmin):
	list_display = ('id', 'identifier', 'type')
	list_filter = ['id', 'identifier', 'type']

class ModuleAdmin(admin.ModelAdmin):
	list_display = ('id', 'sensor', 'pcb', 'plate')
	list_filter = ['id',]


class PcbAdmin(admin.ModelAdmin):
	list_display = ('id', 'identifier', )
	list_filter = ['id',]


class PlateAdmin(admin.ModelAdmin):
	list_display = ('id', 'identifier', 'nom_thickness')
	list_filter = ['id',]

class ShipmentAdmin(admin.ModelAdmin):
	list_display = ('id', 'actor', 'recipient', 'date')
	list_filter = ['id',]

class Shipped_itemAdmin(admin.ModelAdmin):
	list_display = ('id', 'shipment', 'item_table_name', 'item_id')
	list_filter = ['id',]





admin.site.register(Sensor, SensorAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Pcb, PcbAdmin)
admin.site.register(Plate, PlateAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Shipped_item, Shipped_itemAdmin)
