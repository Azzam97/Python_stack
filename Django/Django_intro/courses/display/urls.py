from django.urls import path
from . import views


urlpatterns =[
    path('', views.index),
    path('create_course', views.create_course),
    path('desc/<int:id>', views.desc),
    path('destroy/<int:id>', views.destroy)
]