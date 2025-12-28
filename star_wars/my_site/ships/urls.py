from django.urls import path
from . import views

app_name = "ships"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ship_id>/', views.details, name='details'),
]