from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # creates a link of the form http://127.0.0.1:8000/post/1/ with name post_detail, pk = primary key
]