from django.urls import path, include
from . views import BookListView, login_view
urlpatterns = [
    path("books/", BookListView.as_view(), name='booklist' ),
    path("login/", login_view)
]



