from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snakes', views.snakes,name='snakes'),
    path('add-snake', views.add,name='add-snake'),
    path('edit-snake/<int:id>', views.edit,name='edit-snake'),   
    path('delete-snake/<int:id>', views.delete,name='delete-snake')
]