from django.urls import path
from .views import chapters_list, create_chapter, update_chapter, delete_chapter

app_name = 'book'

urlpatterns = [
    path('', chapters_list, name='chapters_list'),
    path('new', create_chapter, name='create_chapter'),
    path('edit/<int:id>/', update_chapter, name='update_chapter'),
    path('delete/<int:id>', delete_chapter, name='delete_chapter'),

]