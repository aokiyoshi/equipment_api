from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class ViewSetPagination(PageNumberPagination):
    """
    Класс пагинатора, чтобы подмешивать его в другие.
    """
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class ViewSetMixin:
    """
    Ограничения и пагинатор выделил в миксин.
    """
    permission_classes = [permissions.IsAuthenticated]
    paginations_class = ViewSetPagination
