from django.urls import path, include
from . views import BookListView, login_view, AuthorView


urlpatterns = [
    path("books/", BookListView.as_view(), name='booklist' ),
    path("login/", login_view),
    path("author/", AuthorView.as_view(), name="author_view")

]
