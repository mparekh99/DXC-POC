"""
Urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addItem', views.addItem, name='addItem'),
  path('update/<int:id>', views.update, name='update'),
  path('update/updateItem/<int:id>', views.updateItem, name='updateItem'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('deleteAll', views.deleteAll, name='deleteAll'),
  path('numDays', views.projectedData, name='numDays'),
  path('upload/', views.upload_file, name='upload'), 
  
]