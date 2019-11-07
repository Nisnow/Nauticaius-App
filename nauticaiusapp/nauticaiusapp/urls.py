from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('npcs/', include('npcs.urls')),
    path('admin/', admin.site.urls),
]