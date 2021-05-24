
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add,name='add'),
path('delete/<int:taskid>/', views.delete,name='delete'),
path('update/<int:taskid>/', views.update,name='update'),
path('abcd/', views.TaskListview.as_view(),name='abcd'),
path('detail/<int:pk>/', views.TaskDetailView.as_view(),name='detail'),
path('edit/<int:pk>/', views.TaskUpdateView.as_view(),name='edit'),
path('remove/<int:pk>/', views.TaskDeleteView.as_view(),name='remove'),
]