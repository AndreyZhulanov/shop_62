from django.urls import path

from . import views


app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete),
    path('buy/<int:id>', views.buy),
]
