from django.contrib import admin
from django.urls import path
from .views import SnackListView,SnackDetail

urlpatterns = [
    path('',SnackListView.as_view(),name='snacks'),
    path('<int:pk>',SnackDetail.as_view(),name='details')

]