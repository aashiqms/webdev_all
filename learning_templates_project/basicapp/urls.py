from django.conf.urls import url
from basicapp import views
from django.urls import path


# template tagging django will automatically look for app_name

app_name = 'basicapp'


urlpatterns = [
    path('relative/', views.relative, name='relative' ),
    
    path('other/', views.other, name='other' ),
    
]