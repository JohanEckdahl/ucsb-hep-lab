from django.db import models
from django.utils import timezone



class Hardware(models.Model):

	def __str__(self): return self.__class__.__name__ +' '+str(self.id)


	def location(self):
		table_name = self.table_name		
		item_id = self.id
		if table_name != 'module':		
			try:
				name = '{}_id'.format(table_name)
				object = Module.objects.get(**{name:self})
				table_name = 'module'
				item_id = object.id
			except:
				pass		
		shipments = Shipped_item.objects.filter(item_table_name = table_name,\
					item_id = item_id).values_list('shipment_id', flat=True)
		location = Shipment.objects.filter(pk__in = shipments).order_by('-date')[0].recipient
		return location		
	
	class Meta:
		abstract= True


class Sensor(Hardware):
	table_name = 'sensor'
	identifier = models.CharField(max_length=20, blank=True, null=True, unique=True)
	type = models.CharField(max_length=20)
	size = models.IntegerField()
	channels = models.IntegerField()
	manufacturer = models.CharField(max_length=20)


	
class Plate(Hardware):
	table_name = 'plate'
	identifier = models.CharField(max_length=20, blank=True, null=True, unique=True)
	material = models.CharField(max_length=20)
	nom_thickness = models.FloatField(blank=True, null=True)
	min_thickness = models.FloatField(blank=True, null=True)
	max_thickness = models.FloatField(blank=True, null=True)
	flatness = models.FloatField(blank=True, null=True)
	size = models.FloatField()
	manufacturer = models.CharField(max_length=20, blank=True, null=True)


class Pcb(Hardware):
	table_name = 'pcb'
	identifier = models.CharField(max_length=20, blank=True, null=True, unique=True)
	thickness = models.FloatField(blank=True, null=True)
	flatness = models.FloatField(blank=True, null=True)
	size = models.FloatField()
	channels = models.IntegerField()
	bonded_skirocs = models.IntegerField(blank=True, null=True)
	manufacturer = models.CharField(max_length=20, blank=True, null=True)


class Module(Hardware):
	table_name = 'module'
	thickness = models.FloatField(blank=True, null=True)
	sensor = models.OneToOneField('Sensor', models.DO_NOTHING, blank=True, null=True, unique=True)
	pcb = models.OneToOneField('Pcb', models.DO_NOTHING, blank=True, null=True, unique=True)
	plate = models.OneToOneField('Plate', models.DO_NOTHING, blank=True, null=True, unique=True)
	barcode = models.CharField(max_length=50, blank=True, null=True)
	tray_number = models.IntegerField(blank=True, null=True)
	position = models.IntegerField(blank=True, null=True)
	kapton = models.CharField(max_length =1 )
	sensor_error_x = models.FloatField(blank=True, null=True)
	sensor_error_y = models.FloatField(blank=True, null=True)
	sensor_error_theta = models.FloatField(blank=True, null=True)
	pcb_error_x = models.FloatField(blank=True, null=True)
	pcb_error_y = models.FloatField(blank=True, null=True)
	pcb_error_theta = models.FloatField(blank=True, null=True)
	



class Shipment(models.Model):
	def __str__(self): return str(self.date)+' '+self.actor+' to '+self.recipient
	actor = models.CharField(max_length=50, blank=False)
	recipient = models.CharField(max_length=50, blank=False)
	date = models.DateField(blank=True, null=True)


class Shipped_item(models.Model):
	tables = (('module', 'module'),
			('sensor', 'sensor'),
			('pcb', 'pcb'),
			('plate', 'plate'),
			)
	shipment= models.ForeignKey('Shipment', models.DO_NOTHING, blank=False, null=False)
	item_table_name = models.CharField(max_length=20, choices=tables, blank = False)
	item_id = models.IntegerField(blank=False)


class Comment(models.Model):
	username = models.CharField(max_length=50, blank=False)
	datetime = models.DateTimeField(default=timezone.now, blank=False)	
	body = models.TextField(max_length=1000, blank=False)
	table = models.CharField(max_length=20, blank=False)
	table_id = models.IntegerField(blank=False)
	


