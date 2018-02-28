from django.urls import path
from . import views

app_name='inventory'

urlpatterns = [
	path('sensor', views.sensor, name='sensor'),
	path('pcb', views.pcb, name='pcb'),
	path('plate', views.plate, name='plate'),
	path('module', views.module, name='module'),
	path('', views.sensor, name='index'),
    #path('', views.IndexView.as_view(), name='index'),
]
