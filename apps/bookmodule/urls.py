from django.urls import path
from .views import index, list_books, aboutus

app_name = 'books'  # تأكد من وجود `app_name`

urlpatterns = [
    path('', index, name='index'),  # تعديل الاسم ليكون "index" بدون "books."
    path('list/', list_books, name='list_books'),
    path('about/', aboutus, name='aboutus'),
]
