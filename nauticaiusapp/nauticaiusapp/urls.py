from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from npcs import views

router = routers.DefaultRouter()
router.register(r'npcs', views.NpcView, 'npcs')

urlpatterns = [
    #path('npcs/', include('npcs.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]