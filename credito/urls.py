from django.urls import path
from . import views


urlpatterns = [
    path('pagos/create/', views.PostPagosView.as_view()),
    path('pagos/list/', views.GetPagosView.as_view())
]


