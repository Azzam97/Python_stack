from django.urls import path
from . import views


app_name = "wall"
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('logout', views.logout),
    path('login', views.login),
    path('create_message', views.create_message),
    path('create_comment/<int:id>', views.create_comment),
    path('delete_message/<int:id>', views.delete)
]