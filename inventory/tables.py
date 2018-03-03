import django_tables2 as tables
from .models import Sensor, Plate, Pcb, Module



comment_button = '<a href="{{record.table_name}}/{{record.id}}/comment" class="btn btn-default glyphicon glyphicon-comment"></a>'
image_button = '<a href="{{record.table_name}}/{{record.id}}/image" class="btn btn-default glyphicon glyphicon-picture"></a>'
file_button = '<a href="{{record.table_name}}/{{record.id}}/file" class="btn btn-default glyphicon glyphicon-folder-open"></a>'


class Master(tables.Table):
	location = tables.Column(orderable=False)
	misc = tables.TemplateColumn('{}{}{}'.format(comment_button, image_button, file_button), orderable=False)
		

class SensorTable(Master):
		
	component = 'sensor'
	id = tables.TemplateColumn('<a href="/'+component+'/{{record.id}}">{{record.id}}</a>')
	class Meta:
		model=Sensor
		attrs = {'class':'table table-striped'}
		fields = ('id', 'identifier', 'type', 'size', 'channels', 'manufacturer', 'location','misc')


class PlateTable(Master):
	component='plate'
	id = tables.TemplateColumn('<a href="/'+component+'/{{record.id}}">{{record.id}}</a>')
	class Meta:
		model=Plate
		attrs = {'class':'table table-striped'}
		fields = ('id', 'identifier', 'nom_thickness', 'min_thickness', 'max_thickness', 'flatness', 'size', 'manufacturer', 'location')

class PcbTable(Master):
	component='pcb'
	id = tables.TemplateColumn('<a href="/'+component+'/{{record.id}}">{{record.id}}</a>')
	class Meta:
		model=Pcb
		attrs = {'class':'table table-striped'}
		fields = ('id', 'identifier', 'size', 'channels', 'manufacturer', 'location')

class ModuleTable(Master):
	component='module'
	id = tables.TemplateColumn('<a href="/'+component+'/{{record.id}}">{{record.id}}</a>')
	class Meta:
		model=Module
		attrs = {'class':'table table-striped'}
		fields = ('id', 'sensor', 'pcb', 'plate', 'thickness', 'location')

