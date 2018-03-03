from django.urls import path
from . import views

app_name='inventory'

urlpatterns = [
	path('<str:table_name>/<int:idn>/comment/', views.comment, name = 'comment'),
	path('<str:folder>/<int:idn>/file/', views.file, name='file'),
	path('<str:folder>/<int:idn>/image/', views.image, name='image'),	
	path('plate/<int:pk>/', views.PlateDetailView.as_view(), name='detail'),
	path('module/<int:pk>/', views.ModuleDetailView.as_view(), name='detail'),
	path('pcb/<int:pk>/', views.PcbDetailView.as_view(), name='detail'),
	path('sensor/<int:pk>/', views.SensorDetailView.as_view(), name='detail'),
	path('sensor', views.sensor, name='sensor'),
	path('pcb', views.pcb, name='pcb'),
	path('plate', views.plate, name='plate'),
	path('module', views.module, name='module'),
	path('', views.sensor, name='index'),
    #path('', views.IndexView.as_view(), name='index'),
]
