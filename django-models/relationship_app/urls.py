from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'), 
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]
