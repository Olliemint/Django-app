from django.urls import path,re_path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.news_of_day,name='NewsToday'),
    path('archives/<past_date>/',views.past_days_news,name = 'pastNews'),
    path('search/', views.search_results, name='search_results'),
    re_path(r'article/(\d+)',views.article,name ='article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)