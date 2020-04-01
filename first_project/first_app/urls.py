from django.conf.urls import url
from first_app import views
from django.urls import include, path


urlpatterns = [
    path('', views.index, name='index'),
]