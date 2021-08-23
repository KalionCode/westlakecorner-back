from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexPagView.as_view(), name='index'),
]