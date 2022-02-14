from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('app-pages/', views.appPage, name='app-page'),
    path('app-components/', views.appComponent, name='app-component'),
    path('accordion/', views.accordion, name='accordion'),
    path('index/', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('chat/', views.chat, name='chat'),
]