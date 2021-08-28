from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from django.urls import reverse
from home.models  import *
from home.forms import BookForm

class BookListAll(ListView):
    template_name = 'book_list.html'
    queryset = Book.objects.all()


class BookDetail(DetailView):
    template_name = 'book_detail.html'
    # queryset = Book.objects.all()
    # this is for  id 
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book,id=id_)

class BookCreate(CreateView):
    template_name = 'book_create.html'
    form_class = BookForm
    queryset = Book.objects.all()

    def form_valid(self,form):
        return super().form_valid(form)
    
    # or
    # def get_success_url(self):
    #     return "/books/"

class BookUpdate(UpdateView):
    template_name = 'book_create.html'
    form_class = BookForm
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book,id=id_)
    def form_valid(self,form):
        return super().form_valid(form)
    

class BookDelete(DeleteView):
    template_name = 'book_delete.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book,id=id_)
    def get_success_url(self):
        return reverse("books:books-list")