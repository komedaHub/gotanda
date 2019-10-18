#from django.contrib import admin
from django.urls import path
from . import views
from .views import OmikujiViewSet,OmikujiItemViewSet
from rest_framework import routers

app_name = 'omikuji'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('<int:id>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
]

router = routers.DefaultRouter()
router.register(r'omikujiitems', OmikujiItemViewSet)
router.register(r'omikujis', OmikujiViewSet)
# router.register(r'omikujiitems', OmikujiViewSet)
