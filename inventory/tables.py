import django_tables2 as tables
from .models import Sensor, Plate, Pcb, Module

class SensorTable(tables.Table):
	class Meta:
		model=Sensor
		attrs = {'class':'table table-striped'}
		fields = ('id', 'identifier', 'type', 'size', 'channels', 'manufacturer', 'location')

class PlateTable(tables.Table):
	class Meta:
		model=Plate
		attrs = {'class':'table table-striped'}
		fields = ('id', 'identifier', 'nom_thickness', 'min_thickness', 'max_thickness', 'flatness', 'size', 'manufacturer', 'location')

class PcbTable(tables.Table):
	class Meta:
		model=Pcb
		attrs = {'class':'table table-striped'}
		fields = ('id', 'identifier', 'size', 'channels', 'manufacturer', 'location')

class ModuleTable(tables.Table):
	class Meta:
		model=Module
		attrs = {'class':'table table-striped'}
		fields = ('id', 'sensor', 'pcb', 'plate', 'thickness', 'location')
