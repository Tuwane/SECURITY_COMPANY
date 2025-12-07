from django.urls import path
from . import views 

app_name = 'guards'

urlpatterns = [
    path('', views.guards_list, name='guard_list'),
    path('add/', views.add, name='add_guard'),
    path('<int:id>/', views.profiles, name='guard_profile'),
]
