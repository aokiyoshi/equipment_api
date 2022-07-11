import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from requests import request
from rest_framework import viewsets

from .models import Equipment, EquipmentType
from .serializers import EquipmentSerializer, EquipmentTypeSerializer
from .utils import *

from django.db.models import Q

# Api


class EquipmentViewSet(ViewSetMixin, viewsets.ModelViewSet):
    """
    Вью сет для оборудования, перегружен кверисет и сериализатор
    """
    queryset = Equipment.objects.all().order_by('-created_at')
    serializer_class = EquipmentSerializer


class EquipmentTypeViewSet(ViewSetMixin, viewsets.ModelViewSet):
    """
    Вью сет для типов оборудования, перегружен кверисет и сериализатор
    """
    queryset = EquipmentType.objects.all().order_by('-created_at')
    serializer_class = EquipmentTypeSerializer

# List Views


@method_decorator(login_required, name='dispatch')
class EquipmentView(ListView):
    """
    Представление для оборудования на основе ListView
    """
    model = Equipment


@method_decorator(login_required, name='dispatch')
class EquipmentTypeView(ListView):
    """
    Представление для типов оборудования на осное ListView
    """
    model = EquipmentType


# Edit Views
@method_decorator(login_required, name='dispatch')
class EquipmentEditView(UpdateView):
    """
    Редактирование: перегружаем модель, поля и редирект
    Перегружен метод валидации, если форма валидна, то выполняется доп. проверка
    на паттерн серийного номера и у родительского метода вызывается form_invalid.
    """
    model = Equipment
    fields = ['name', 'manufacturer',
              'equipment_type', 'description', 'serial']
    success_url = '/equipment/'

    def form_valid(self, form):
        if not re.match(r'^[a-zA-Z0-9-_@]*$', form.cleaned_data['serial']):
            return super().form_invalid(form)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EquipmentTypeEditView(UpdateView):
    """
    Редактирование: перегружаем модель, поля и редирект
    """
    model = EquipmentType
    fields = ['name', 'description']
    success_url = '/equipment-types/'


# Create Views
@method_decorator(login_required, name='dispatch')
class EquipmentCreateView(CreateView):
    """
    Создание: перегружаем модель, поля и редирект
    """
    model = Equipment
    fields = ['name', 'manufacturer',
              'equipment_type', 'description', 'serial']
    success_url = '/equipment/'

    def form_valid(self, form):
        if not re.match(r'^[a-zA-Z0-9-_@]*$', form.cleaned_data['serial']):
            return super().form_invalid(form)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EquipmentTypeCreateView(CreateView):
    """
    Создание: перегружаем модель, поля и редирект
    """
    model = EquipmentType
    fields = ['name', 'description']
    success_url = '/equipment-types/'

# Примечание в классах редактирования осонзанно пропущены поля с ссылками на шаблоны
# Django их выводит из название модели + _prefix

class EquipmentSearchView(ListView):
    model = Equipment

    def get_queryset(self):
        keywd = self.kwargs['kw']
        return Equipment.objects.filter(
            Q(name__icontains=keywd)
        )