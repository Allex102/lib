from django.urls import path
from django.views.generic import TemplateView

from .views import BookListView, BookDetailView, book_search

urlpatterns = [
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book/<str:slug>', BookDetailView.as_view(), name='book'),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('contacts/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    # path('search/', Search.as_view(), name='search')
    path('search/', book_search, name='search')
]
