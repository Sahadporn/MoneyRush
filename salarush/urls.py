from django.urls import path, include

from salarush import views

app_name = 'salarush'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.AddView.as_view(), name='table'),
    path('add_item/', views.add_item, name='add_item'),
    path('subtract_item/', views.subtract_item, name='subtract_item')
]
