from django.urls import path
from . import views


urlpatterns = [
    path('almacen/', views.AlmacenView.as_view()),
]