from django.urls import path
from . import views


urlpatterns = [
    path('almacen/create/', views.PostAlmacenView.as_view()),
    path('almacen/list/', views.GetAlmacenView.as_view()),
]