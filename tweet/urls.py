
from django.urls import path, include
from . import views



urlpatterns = [

    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('update/<int:pk>/', views.update_tweet, name='update_tweet'),
    path('delete/<int:pk>/', views.delete_tweet, name='delete_tweet'),

] 