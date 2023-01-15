from django.urls import path
from book.views import BookViewSet

urlpatterns = [
    path('', BookViewSet.as_view(), name='book')
]