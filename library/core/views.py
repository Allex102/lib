from django.db.models import Q
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Authors, Readers, Outs, Books

class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'
    queryset = Books.objects.all().order_by('name')
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Books
    template_name = 'book.html'
    slug_field = 'slug'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def book_search(request):
    book = request.GET.get('book')
    author = request.GET.get('author')
    object = Books.objects.filter(Q(name__icontains=book) | Q(author_id__fullname=author))
    context = {'book_list': object}
    return render(request=request, template_name='search_book.html', context=context)