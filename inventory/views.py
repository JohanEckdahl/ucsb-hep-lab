import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from .forms import CommentForm
from .models import *
from .tables import *




def image(request, folder, idn):
	path = "component_images/{}/{}/".format(folder, idn) 
	os_path = "{}{}".format(settings.MEDIA_ROOT, path)
	web_path = "files/media/{}".format(path)
	try:
		images = os.listdir(os_path)
	except:
		images = False
	return render(request, 'inventory/image.html', {'images' : images, 'path': web_path})



def file(request, folder, idn):
	path= "files/{}/{}/".format(folder, idn) 
	os_path = "{}{}".format(settings.MEDIA_ROOT, path)
	web_path = "files/media/{}".format(path)
	try:
		files = os.listdir(os_path)
	except:
		files = False
	return render(request, 'inventory/file.html', {'files' : files, 'path': web_path})
	
def comment(request, table_name, idn):
	comments = Comment.objects.filter(table=table_name, table_id = idn).order_by('-datetime')
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.table = table_name
			comment.table_id = idn
			comment.datetime = timezone.now()
			comment.save()
	else:	
		form = CommentForm()
	return render(request, 'inventory/comment_form.html', {'comments':comments, 'form':form})


#----------#
#  Tables  #
#----------#

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

