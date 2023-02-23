from django.urls import path
from .views import get_average_rating,book_review

urlpatterns = [
    path('average-rating/', get_average_rating, name='average-rating'),
    path('book_review/',book_review,name='book-review'),
]

