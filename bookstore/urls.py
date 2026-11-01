from django.urls import path, include
from .views import BookListView, login_view, AuthorView, RegisterView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("books/", BookListView.as_view(), name="booklist"),
    path("login/", login_view),
    path("author/", AuthorView.as_view(), name="author_view"),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
