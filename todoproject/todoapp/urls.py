from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('done/<int:taskid>', views.delete, name='delete'),
    path('update/<int:taskid>', views.update, name='update'),
    path('cbvhome/', views.TaskListView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='cbvdelete'),


]
