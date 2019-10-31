from django.urls import path

from . import views

urlpatterns = [
    path('',views.feeds,name = 'feeds'),
    path('answers/',views.answers,name = 'answers'),
    path('questions/',views.questions,name = 'questions'),
    path('logout/',views.logout_handler,name = 'logout_handler'),
    path('answer/<int:q_id>',views.answer_handler,name = 'answer_handler'),
    path('delete/<int:q_id>',views.q_delete,name = 'q_delete'),
    path('bookmark/<int:a_id>',views.bookmark ,name = 'bookmark'),
    path('upvote/<int:a_id>',views.upvote ,name = 'upvote'),
]
