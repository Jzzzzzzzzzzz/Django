from .views import index,top_sellers,advertisements_post
from django.urls import path

urlpatterns = [
    path('',index,name='main-page'),
    path('top-sellers/',top_sellers,name='top-sellers'),
    path("advertisement-post/",advertisements_post,name="adv-post")#name для указа в шаблонах
]