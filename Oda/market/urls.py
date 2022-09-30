from django.contrib import admin
from django.urls import path
from market import views


app_name = 'market'
urlpatterns =[

    path('', views.MarketLV.as_view(), name='index'),

    path('cate/<int:cate>/', views.MarketCate, name='market_cate_list'),

    path('<int:pk>/', views.MarketDV.as_view(), name='market_detail'),
]