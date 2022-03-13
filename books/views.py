from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    
    
class BookDetailView(DetailView): # new
    model = Book
    template_name = 'books/book_detail.html'      
    