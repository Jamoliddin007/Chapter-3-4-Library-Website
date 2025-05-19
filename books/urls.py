from django.urls import path
from .views import BookListView
from .api_views import BookListAPIView

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path("books/", BookListAPIView.as_view(), name="book_list_api"),
]

