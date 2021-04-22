from django.urls import path  
from . import views
urlpatterns = [
    path('courses', views.index),
    path('course/create', views.create),
    path('course/edit/<str:id>', views.edit),
    path('course/delete/<str:id>', views.destroy),
    path('course/comments/<str:id>', views.comments),
    path('course/comments/<str:id>/create', views.commcreate),
]
