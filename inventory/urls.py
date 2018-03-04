from django.urls import path
from . import views

app_name='inventory'

urlpatterns = [
	path('<str:table_name>/<int:idn>/comment/', views.comment, name = 'comment'),
	path('<str:folder>/<int:idn>/file/', views.file, name='file'),
	path('<str:folder>/<int:idn>/image/', views.image, name='image'),
	path('sensor', views.sensor, name='sensor'),
	path('pcb', views.pcb, name='pcb'),
	path('plate', views.plate, name='plate'),
	path('module', views.module, name='module'),
	path('', views.sensor, name='index'),
]
