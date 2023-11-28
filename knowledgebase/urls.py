from . import views
from django.urls import path

urlpatterns = [
    # path('', views.VideoList.as_view(), name='index')
    path('', views.index, name='index'),
]