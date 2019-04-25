from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url('v1.0/wind/', view.wind),
]