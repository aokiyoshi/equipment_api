from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'equipment-type', views.EquipmentTypeViewSet)


urlpatterns = [
    path('', views.EquipmentView.as_view()),
    path('equipment/', views.EquipmentView.as_view()),
    path('equipment-types/', views.EquipmentTypeView.as_view()),

    path('equipment/<int:pk>/', views.EquipmentEditView.as_view()),
    path('equipment-type/<int:pk>/', views.EquipmentTypeEditView.as_view()),

    path('equipment/new/', views.EquipmentCreateView.as_view()),
    path('equipment-type/new/', views.EquipmentTypeCreateView.as_view()),

    path('search/<str:kw>', views.EquipmentSearchView.as_view()),

    path('api/', include(router.urls)),

    path('accounts/', include('django.contrib.auth.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
