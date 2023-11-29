from django.urls import path
from . import views

urlpatterns = [
    path('get/<int:pk>', views.get_rec),
    path('add/', views.add_rec),
    path('del/', views.del_rec),

]
