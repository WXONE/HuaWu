from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'cases',views.CaseViewSet)

urlpatterns = [
    path(r'^', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('filetest/', views.upload_file, name='filetest'),

]