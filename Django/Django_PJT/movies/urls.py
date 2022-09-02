from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<pk>/', views.detail, name="detail"),
    path('<pk>/delete/', views.delete, name="delete"),
    path('<pk>/edit/', views.edit, name="edit"),
    path('<pk>/update/', views.update, name="update"),
]
