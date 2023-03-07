
from django.urls import path
from xss import views

urlpatterns = [
    path("",views.home,name='home'),
    path("network",views.network,name='network'),
    path("scan",views.scan,name='scan'),
    path("showdetail",views.showdetail,name='detail')

  
]
