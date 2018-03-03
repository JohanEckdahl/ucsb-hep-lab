from django.db import models
from django.utils import timezone

'''
class Hardware(models.Model):

	@property
	def location(self):
		item_table_name = 'pcb'
		class_name = Pcb
		item_id = self.id
		if item_table_name != 'module':
			object = class_name.objects.get(pk = item_id)
			try:
				name = '{}_id'.format(item_table_name)
				object = Module.objects.get(**{name:object})
				item_table_name = 'module'
				item_id = object.id
			except:
				g=1
			
		a = Shipped_item.objects.filter(item_table_name = item_table_name, item_id = item_id).values_list('shipment_id', flat=True)
		self._location = Shipment.objects.filter(pk__in = a).order_by('-date')[0].recipient
		return self._location
	
	class Meta:
		abstract= True


'''

class Hardware(models.Model):
	def image_links(self):
		path= "{}/component_images/{}/{}/".format(settings.MEDIA_ROOT, self.table_name, self.id) 
		try:
			images = os.listdir(path)
		except:
			images = False
		
		return images
		
	
	class Meta:
		abstract= True


class Sensor(Hardware):
	table_name='sensor'
	identifier = models.CharField(max_length=20, blank=True, null=True, unique=True)
	type = models.CharField(max_length=20)
	size = models.IntegerField()
	channels = models.IntegerField()
	manufacturer = models.CharField(max_length=20)

	def __str__(self):
		return self.__class__.__name__+' '+str(self.id)
	
	@property
	def location(self):
		item_table_name = 'sensor'
		class_name = Sensor
		item_id = self.id
		if item_table_name != 'module':
			object = class_name.objects.get(pk = item_id)
			try:
				name = '{}_id'.format(item_table_name)
				object = Module.objects.get(**{name:object})
				item_table_name = 'module'
				item_id = object.id
			except:
				g=1
			
		a = Shipped_item.objects.filter(item_table_name = item_table_name, item_id = item_id).values_list('shipment_id', flat=True)
		self._location = Shipment.objects.filter(pk__in = a).order_by('-date')[0].recipient
		return self._location



class Plate(models.Model):
	table_name = 'plate'
	identifier = models.CharField(max_length=20, blank=True, null=True, unique=True)
	material = models.CharField(max_length=20)
	nom_thickness = models.FloatField(blank=True, null=True)
	min_thickness = models.FloatField(blank=True, null=True)
	max_thickness = models.FloatField(blank=True, null=True)
	flatness = models.FloatField(blank=True, null=True)
	size = models.FloatField()
	manufacturer = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.__class__.__name__+' '+str(self.id)
	
	@property
	def location(self):
		item_table_name = 'plate'
		class_name = Plate
		item_id = self.id
		if item_table_name != 'module':
			object = class_name.objects.get(pk = item_id)
			try:
				name = '{}_id'.format(item_table_name)
				object = Module.objects.get(**{name:object})
				item_table_name = 'module'
				item_id = object.id
			except:
				g=1
			
		a = Shipped_item.objects.filter(item_table_name = item_table_name, item_id = item_id).values_list('shipment_id', flat=True)
		self._location = Shipment.objects.filter(pk__in = a).order_by('-date')[0].recipient
		return self._location

	
class Pcb(models.Model):
	table_name = 'pcb'
	identifier = models.CharField(max_length=20, blank=True, null=True, unique=True)
	thickness = models.FloatField(blank=True, null=True)
	flatness = models.FloatField(blank=True, null=True)
	size = models.FloatField()
	channels = models.IntegerField()
	bonded_skirocs = models.IntegerField(blank=True, null=True)
	manufacturer = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.__class__.__name__+' '+str(self.id)

	@property
	def location(self):
		item_table_name = 'pcb'
		class_name = Pcb
		item_id = self.id
		if item_table_name != 'module':
			object = class_name.objects.get(pk = item_id)
			try:
				name = '{}_id'.format(item_table_name)
				object = Module.objects.get(**{name:object})
				item_table_name = 'module'
				item_id = object.id
			except:
				g=1
			
		a = Shipped_item.objects.filter(item_table_name = item_table_name, item_id = item_id).values_list('shipment_id', flat=True)
		self._location = Shipment.objects.filter(pk__in = a).order_by('-date')[0].recipient
		return self._location


class Module(models.Model):
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
	


	def __str__(self):
		return self.__class__.__name__+' '+str(self.id)

	@property
	def location(self):
		item_table_name = 'module'
		class_name = Module
		item_id = self.id
		if item_table_name != 'module':
			object = class_name.objects.get(pk = item_id)
			try:
				name = '{}_id'.format(item_table_name)
				object = Module.objects.get(**{name:object})
				item_table_name = 'module'
				item_id = object.id
			except:
				g=1
			
		a = Shipped_item.objects.filter(item_table_name = item_table_name, item_id = item_id).values_list('shipment_id', flat=True)
		self._location = Shipment.objects.filter(pk__in = a).order_by('-date')[0].recipient
		return self._location
	


class Shipment(models.Model):
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
	


