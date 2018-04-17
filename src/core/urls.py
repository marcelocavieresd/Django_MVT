from django.conf.urls import url
import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),  
    url(r'^crear_licencia/$', views.crear_licencia, name='crear_licencia')   
]