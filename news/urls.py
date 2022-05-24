from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.news_of_day,name='NewsToday'),
    path('archives/<past_date>/',views.past_days_news,name = 'pastNews') 
]