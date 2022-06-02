from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('<int:user_id>/reviews', views.reviews, name='reviews'),
    path('register', views.register, name='register'),
]
