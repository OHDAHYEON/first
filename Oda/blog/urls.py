from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    # 예시 : blog/
    path('', views.PostLV.as_view(), name='index'),

    # 예시 : blog/post/ (same as /blog/)
    path('post/', views.PostLV.as_view(), name='post_list'),

    # 예시 : blog/post/django-example/슬러그-슬러그-슬러그
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name = 'post_detail'),

    # 예시 : blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    
    # 예시 : blog/archive/2022/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # 예시 : blog/archive/2022/9월
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # 예시 : blog/archive/2022/9월/16/
    path('archive/<int:year>/<str:month>/<int:day>', views.PostDAV.as_view(), name='post_day_archive'),

    # 예시 : blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    # Example : /blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # Example : /blog/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    path('search/', views.SearchFormView.as_view(), name='search'),


    path('add/', views.PostCreateView.as_view(), name='add'),
    path('change/', views.PostChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]
