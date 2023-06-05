from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('greeting/<str:name>', views.greetings),
    path('<int:id>/<str:name>', views.id_number)
]