from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from django.views.generic.edit import CreateView
from django.views import generic


from .models import Sensor, Plate, Module, Pcb
from .tables import SensorTable, PlateTable, ModuleTable, PcbTable


class IndexView(generic.ListView):
	template_name = 'inventory/base.html'
	context_object_name = 'all_components'

	def get_queryset(self):
		return Sensor.objects.order_by('id')

def sensor(request):
	title = 'Sensors'
	table = SensorTable(Sensor.objects.all(), order_by="-id")
	RequestConfig(request, paginate=False, ).configure(table)
	return render(request, 'inventory/inventory.html', {'table': table, 'title' : title})

def module(request):
	title = 'Modules'
	table = ModuleTable(Module.objects.all(), order_by="-id")
	RequestConfig(request, paginate=False, ).configure(table)
	return render(request, 'inventory/inventory.html', {'table': table, 'title' : title})

def pcb(request):
	title = 'PCBs'
	table = PcbTable(Pcb.objects.all(), order_by="-id")
	RequestConfig(request, paginate=False, ).configure(table)
	return render(request, 'inventory/inventory.html', {'table': table, 'title' : title})

def plate(request):
	title = 'Plate'
	table = PlateTable(Plate.objects.all(), order_by="-id")
	RequestConfig(request, paginate=False, ).configure(table)
	return render(request, 'inventory/inventory.html', {'table': table, 'title' : title})

