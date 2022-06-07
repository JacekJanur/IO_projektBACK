from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('quickstart/', include('quickstart.urls')),
    path('users/', include('users.urls')),
    path('genres/', include('genres.urls')),
    path('reviews/', include('reviews.urls')),
    path('games/', include('games.urls')),
    path('comments/', include('comments.urls')),
    path('admin/', admin.site.urls),
]