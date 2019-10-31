from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.editprofile , name = 'editprofile'),
    path('bookmarks',views.bookmarks ,name = 'bookmarks'),
]
