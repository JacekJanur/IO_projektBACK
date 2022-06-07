from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('<int:game_id>/image', views.image, name='image'),
    path('<int:game_id>/reviews', views.reviews, name='reviews'),
]
