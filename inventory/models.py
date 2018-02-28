from django.db import models



class Hardware(models.Model):

	def get_location(self, component_id, name):
		if name == 'Module':
			a = Shipped_item.objects.filter(item_id=component_id, item_table_name=name)
		else:
			pass

		return a
	
#	class Meta:
#		abstract = True



class Sensor(models.Model):
	identifier = models.CharField(max_length=20, blank=True, null=True, unique=True)
	type = models.CharField(max_length=20)
	size = models.IntegerField()
	channels = models.IntegerField()
	manufacturer = models.CharField(max_length=20)

	def __str__(self):
		return self.__class__.__name__+' '+str(self.id)
	
	def class_name(self):
		return self.__class__.__name__
	
class Plate(models.Model):
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
	

	
class Pcb(models.Model):
	identifier = models.CharField(max_length=20, blank=True, null=True, unique=True)
	thickness = models.FloatField(blank=True, null=True)
	flatness = models.FloatField(blank=True, null=True)
	size = models.FloatField()
	channels = models.IntegerField()
	bonded_skirocs = models.IntegerField(blank=True, null=True)
	manufacturer = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.__class__.__name__+' '+str(self.id)


class Module(Hardware):
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
	location = get_location(self, 1, 'Module')

	def __str__(self):
		return self.__class__.__name__+' '+str(self.id)


class Shipment(models.Model):
	actor = models.CharField(max_length=50, blank=False)
	recipient = models.CharField(max_length=50, blank=False)
	date = models.DateField(blank=True, null=True)

class Shipped_item(models.Model):
	tables = (('Module', 'Module'),
			('Sensor', 'Sensor'),
			('Pcb', 'PCB'),
			('Plate', 'Plates'),
			)
	shipment= models.ForeignKey('Shipment', models.DO_NOTHING, blank=False, null=False)
	item_table_name = models.CharField(max_length=20, choices=tables, blank = False)
	item_id = models.IntegerField(blank=False)






