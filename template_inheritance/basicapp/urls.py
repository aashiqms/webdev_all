from django.conf.urls import url
from basicapp import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'basicapp'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]