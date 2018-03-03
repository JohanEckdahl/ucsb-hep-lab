from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from django.views import generic
import os
from .forms import CommentForm
from django.views.generic.edit import FormView
from django.conf import settings
from .models import *
from .tables import SensorTable, PlateTable, ModuleTable, PcbTable




def image(request, folder, idn):
	path= "{}/component_images/{}/{}/".format(settings.MEDIA_ROOT, folder, idn) 
	try:
		images = os.listdir(path)
	except:
		images = False
	return render(request, 'inventory/image.html', {'images' : images, 'path': path})

def file(request, folder, idn):
	path= "{}/files/{}/{}/".format(settings.MEDIA_ROOT, folder, idn) 
	try:
		files = os.listdir(path)
	except:
		files = False
	return render(request, 'inventory/file.html', {'files' : files, 'path': path})
	


def comment(request, table_name, idn):
	comments = Comment.objects.filter(table=table_name, table_id =idn)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.table = table_name
			comment.table_id = idn
			#comment.published_date = timezone.now()
			comment.save()
	else:	
		form = CommentForm()
	return render(request, 'inventory/comment_form.html', {'comments':comments, 'form':form})


### Tables

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

### Don't need it?
class IndexView(generic.ListView):
	template_name = 'inventory/base.html'
	context_object_name = 'all_components'

	def get_queryset(self):
		return Sensor.objects.order_by('id')

class SensorDetailView(generic.DetailView):
	model = Sensor	
	template_name = 'inventory/detail.html'
class PcbDetailView(generic.DetailView):
	model = Pcb	
	template_name = 'inventory/detail.html'
class PlateDetailView(generic.DetailView):
	model = Plate	
	template_name = 'inventory/detail.html'
class ModuleDetailView(generic.DetailView):
	model = Module	
	template_name = 'inventory/detail.html'


