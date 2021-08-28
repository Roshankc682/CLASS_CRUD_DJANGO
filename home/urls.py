from django.urls import path
from home.views import *

app_name = 'books'
urlpatterns = [
    path('books/',BookListAll.as_view(),name="books-list"),

    path('books/<int:id>/details',BookDetail.as_view(),name="books-single"),
    # path('books/<int:pk>/details',BookDetail.as_view(),name="books-single"),

    path('books/create',BookCreate.as_view(),name="books-create"),
    path('books/<int:id>/update',BookUpdate.as_view(),name="books-update"),
    path('books/<int:id>/delete',BookDelete.as_view(),name="book-delete"),
]